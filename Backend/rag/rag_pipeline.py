from .transcript import get_transcript
from .splitter import split_text
from .embedder import embeddings
from .Vectorstore import save_index, get_index
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate

llm_endpoint = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
    temperature=0.2
)
model = ChatHuggingFace(llm=llm_endpoint)

prompt = PromptTemplate(
    template="""
    Use ONLY this transcript context to answer.

    Context:
    {context}

    Question:
    {question}
    """,
    input_variables=["context", "question"]
)

def build_index(video_id):
    text = get_transcript(video_id)
    if not text:
        return False

    chunks = split_text(text)
    index = FAISS.from_documents(chunks, embeddings)
    save_index(video_id, index)
    return True


def answer_question(video_id, question):
    index = get_index(video_id)
    if not index:
        return None

    retriever = index.as_retriever(search_kwargs={"k": 4})
    docs = retriever.invoke(question)

    context = "\n\n".join(d.page_content for d in docs)

    final_prompt = prompt.format(context=context, question=question)

    response = model.invoke(final_prompt)

    return {
        "answer": response.content,
        "chunks_used": len(docs)
    }

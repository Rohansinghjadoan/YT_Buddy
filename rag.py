from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter   
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint,HuggingFaceEmbeddings
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser 
from langchain_core.runnables import RunnableParallel,RunnablePassthrough,RunnableLambda

load_dotenv()

llm1 = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
    temperature=0.2
)
model1 = ChatHuggingFace(llm=llm1)

yt_video_id = "Gfr50f6ZBvo"
try:

   
    ytt_api=YouTubeTranscriptApi()
    transcript_list=ytt_api.fetch(video_id=yt_video_id,languages=['en'])


    transcript=" ".join(chunk.text for chunk in transcript_list)
    #print (transcript)
except TranscriptsDisabled:
    print("No captions available for this video.")


## indexing

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.create_documents([transcript])


embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
vector_store=FAISS.from_documents(chunks,embedding_model)



## retrival

retriver=vector_store.as_retriever(search_type='similarity',search_kwargs={'k':4})



## Augmentation

prompt = PromptTemplate(
    template="""
      You are a helpful assistant.
      Answer ONLY from the provided transcript context.
      If the context is insufficient, just say you don't know.

      {context}
      Question: {question}
    """,
    input_variables = ['context', 'question']
)
question          = "is the topic of nuclear fusion discussed in this video? if yes then what was discussed"
retrieved_docs    = retriver.invoke(question)
#print(retrieved_docs)

context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
#print(context_text)

final_prompt = prompt.invoke({"context": context_text, "question": question})
#print(final_prompt)

## generation
answer=model1.invoke(final_prompt)
#print(answer.content)

def format_docs(retrieved_docs):
  context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
  return context_text

parallel_chain = RunnableParallel({
    'context': retriver | RunnableLambda(format_docs),
    'question': RunnablePassthrough()
})
##print(parallel_chain.invoke('who is Demis'))
parser = StrOutputParser()
main_chain = parallel_chain | prompt | model1 | parser

print(main_chain.invoke('Can you summarize the video'))











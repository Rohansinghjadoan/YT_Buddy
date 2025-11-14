from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter   
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint,HuggingFaceEmbeddings
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser 
from langchain_core.runnables import RunnableParallel

load_dotenv()

llm1 = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)
model1 = ChatHuggingFace(llm=llm1)

yt_video_id = "Gfr50f6ZBvo"
try:

    # MUST PASS A LIST
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

print(vector_store.index_to_docstore_id)


    

    #


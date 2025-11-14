from fastapi import FastAPI
from routers.transcript_routes import router as transcript_router
from routers.index_routes import router as index_router
from routers.query_routes import router as query_router

app = FastAPI(title="YT Buddy Backend")

app.include_router(transcript_router, prefix="/transcript")
app.include_router(index_router, prefix="/index")
app.include_router(query_router, prefix="/ask")

@app.get("/")
def home():
    return {"message": "YT Buddy Backend Running!"}

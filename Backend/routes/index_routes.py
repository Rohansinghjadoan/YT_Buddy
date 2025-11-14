from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from rag.rag_pipeline import build_index

router = APIRouter()

class VideoRequest(BaseModel):
    video_id: str

@router.post("/")
def build(req: VideoRequest):
    ok = build_index(req.video_id)
    if not ok:
        raise HTTPException(400, "Transcript missing")
    return {"message": "Index built successfully!"}

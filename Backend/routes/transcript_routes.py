from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from rag.transcript import get_transcript

router = APIRouter()

class VideoRequest(BaseModel):
    video_id: str

@router.post("/")
def fetch_transcript(req: VideoRequest):
    transcript = get_transcript(req.video_id)
    if transcript is None:
        raise HTTPException(404, "Transcript not available")
    return {"video_id": req.video_id, "transcript_snippet": transcript[:500]}

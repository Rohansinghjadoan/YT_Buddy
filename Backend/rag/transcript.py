from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id: str):
    try:
        data = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
        return " ".join(x["text"] for x in data)
    except:
        return None

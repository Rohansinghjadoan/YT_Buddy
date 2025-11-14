from langchain_community.vectorstores import FAISS

index_cache = {}

def save_index(video_id, index):
    index_cache[video_id] = index

def get_index(video_id):
    return index_cache.get(video_id)

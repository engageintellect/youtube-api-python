import os
import requests
from dotenv import load_dotenv

load_dotenv()

search_term='sveltekit'

def search_youtube(query, max_results=25):
    API_KEY = os.getenv("YOUTUBE_API_KEY")
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&type=video&key={API_KEY}&maxResults={max_results}&order=date"
    response = requests.get(url)
    results = response.json()["items"]
    return results



results = search_youtube("sveltekit")
for result in results:
    video_id = result["id"]["videoId"]
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    print(result["snippet"]["publishedAt"], result["snippet"]["title"], video_url)


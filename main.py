import requests

search_term = 'turbo sveltekit'

def search_youtube(query, max_results=25):
    API_KEY = "AIzaSyCSis_YjZDjyGgNvXSZPaYiZ-3oZ165SNo"
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&type=video&key={API_KEY}&maxResults={max_results}&order=date"
    response = requests.get(url)
    results = response.json()["items"]
    return results

results = search_youtube(search_term)
for result in results:
    print(result["snippet"]["publishedAt"], result["snippet"]["title"])


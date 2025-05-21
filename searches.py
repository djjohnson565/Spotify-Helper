#Tools for searching in the Spotify Database

from requests import get
import json

def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = token
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]

    if len(json_result) == 0:
        print("No Artist Found\n")
        return None
    
    return json_result[0]

def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = token
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result
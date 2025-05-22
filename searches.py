#Tools for searching in the Spotify Database


from requests import get
import json


# Search for an artist
#
# PARAMETERS
# token (dict): token for making requests
# artist_name (string): input string for artist name
#
# Returns a dictionary corresponding to the best matching search result
# Retuns None on an unsuccessful search
#
def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers=token)
    json_result = json.loads(result.content)["artists"]["items"]

    if len(json_result) == 0:
        return None
    
    return json_result[0]


# Get top 10 songs for an artist
#
# PARAMETERS
# token (dict): token for making requests
# artist_id (string): input string that is the artist id on spotify
#
# Returns a list corresponding to the top 10 tracks of the artist
# Retuns None on an unsuccessful search
#
def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    result = get(url, headers=token)
    json_result = json.loads(result.content)["tracks"]

    if len(json_result) == 0:
        return None

    return json_result
# Spotify-Helper
# Created by github.com/djjohnson565
# https://github.com/djjohnson565/Spotify-Helper

from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json
from searches import *


# Create token
def get_token(client_id, client_secret):
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token


# Create authentication header for the token
def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def main():
    load_dotenv()
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    token = get_token(client_id, client_secret)
    artist = input("What artist do you want to search?: ")
    search_result = search_for_artist(get_auth_header(token), artist)
    if(search_result == None):
        return
    print(f"Artist Found: {search_result['name']}")
    artist_id = search_result["id"]
    songs = get_songs_by_artist(get_auth_header(token), artist_id)
    print(f"Type of songs: {type(songs)}")
    for i, song, in enumerate(songs):
        print(f"{i + 1}. {song['name']}")

if __name__ == "__main__":
    main()
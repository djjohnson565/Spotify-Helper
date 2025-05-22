# Spotify-Helper
# Created by github.com/djjohnson565
# https://github.com/djjohnson565/Spotify-Helper

from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json
from searches import *
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from autoqueues import *
import time


def program_loop(sp, prev_track):
    cur_track = get_current_track(sp.current_playback())[2]
    if(cur_track != prev_track):
        prev_track = cur_track
        auto_queue(sp, cur_track)
    else:
        cur_track = get_current_track(sp.current_playback())
        print(f"Track: {cur_track[0]}")
        print(f"Artist: {cur_track[1]}")
        print(f"URI: {cur_track[2]}")
        time.sleep(5)


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

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id = os.getenv("CLIENT_ID"),
    client_secret = os.getenv("CLIENT_SECRET"),
    redirect_uri="http://127.0.0.1:8000/callback",
    scope="user-read-playback-state%20user-modify-playback-state"
    ))

    run = True
    prev_track = None

    # You must send an interrupt (Ctrl+C) to kill the program in terminal
    while(run):
        program_loop(sp, prev_track)

if __name__ == "__main__":
    main()
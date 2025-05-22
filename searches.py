#Tools for searching in the Spotify Database


from requests import get
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth


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


# Search for a track
#
# PARAMETERS
# token (dict): token for making requests
# track_name (string): input string for track name
# artist_name (string) (optional): input string for artist name
#
# Returns the best corresponding track in the search result
# Retuns None on an unsuccessful search
#
def search_for_track(token, track_name, artist_name=None):
    url = "https://api.spotify.com/v1/search"

    if artist_name:
        query = f"?q=track:{track_name} artist:{artist_name}&type=track&limit=1"
    else:
        query = f"?q=track:{track_name}&type=track&limit=1"

    query_url = url + query
    result = get(query_url, headers=token)
    json_result = json.loads(result.content)["tracks"]["items"]

    if len(json_result) == 0:
        return None

    return json_result[0]


# Get up to 25 albums for an artist
#
# PARAMETERS
# token (dict): token for making requests
# artist_id (string): input string that is the artist id on spotify
#
# Returns a list corresponding to the most relevent (up to) 25 albums of the artist
# Retuns None on an unsuccessful search
#
def get_albums_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/albums?country=US&limit=25"
    result = get(url, headers=token)
    json_result = json.loads(result.content)["items"]

    if len(json_result) == 0:
        return None

    return json_result


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


# Add a track to the user's Spotify queue
#
# PARAMETERS
# token (dict): token for making requests
# track_uri (string): the full Spotify URI of the track
#
# Returns True on success, False on failure
#
def add_track_to_queue(token, track_uri):
    url = f"https://api.spotify.com/v1/me/player/queue?uri={track_uri}"
    result = get(url, headers=token)

    if result.status_code == 204:
        return True
    else:
        print(f"Failed to add track to queue: {result.status_code} - {result.text}")
        return False


# Get current track playing on Spotify account
#
# PARAMETERS
# playback: request for getting current playing song
#
# Returns list with song title, artist name, and track uri
# Returns None, None, None if no song is currently playing
#
def get_current_track(playback):
    if playback and playback['is_playing']:
        track = playback['item']
        name = track['name']
        artists = [artist['name'] for artist in track['artists']]
        return name, artists, track['uri']
    return None, None, None
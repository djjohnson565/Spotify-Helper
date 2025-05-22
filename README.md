# ![alt text](./images/sh.png "Spotify-Helper") 

# Spotify-Helper

Spotify-Helper is a tool designed to work alongside Spotify. It is currently in development, and new features will be added and listed here as they become available.

## Disclaimer

This software is **not affiliated with**, **endorsed by**, or **sponsored by Spotify, Inc.**. It is an independent project created by [djjohnson565](https://github.com/djjohnson565).  

Spotify is a registered trademark of Spotify, Inc. and is used for identification purposes only. This project is intended to work alongside the Spotify platform, but it does not have any official relationship with Spotify.  

Please refer to Spotify's official website and terms of service for more information about their services.

## Setup

### Create a Spotify App
Currently this application is not web hosted, and will need to be run entirely on your system. In the future, this process will be more streamlined and you will not need to go through this process. First, create a Spotify account and then visit [Spotify for Developers](https://developer.spotify.com/). Create the app through their guidelines, you can set the redirect uri to whatever you want, for example, "http://127.0.0.1:8000/callback". Next, copy your Client ID and Client Secret, and place them in a .env file.
> [!CAUTION]
> **DO NOT** share your Client ID or Client Secret with anybody.

### Create a .env File
Insert the following text into your .env file, and place it in this directory.
```python
CLIENT_ID = "YOUR CLIENT ID"
CLIENT_SECRET = "YOUR CLIENT SECRET"
REDIRECT_URI = "http://127.0.0.1:8000/callback"
```

### Authenticate Your App
Visit this link so Spotify-Helper can work alongside your Spotify account.
```
https://accounts.spotify.com/authorize?client_id=YOUR_CLIENT_ID&response_type=code&redirect_uri=YOUR_REDIRECT_URI&scope=user-read-playback-state%20user-modify-playback-state&show_dialog=true

```

### You Are Good To Go!
Have fun playing around with Spotify-Helper!

## Patch Notes

### v0.1.0 5/22/2025

First production release!

- Please read the setup instructions
- Can auto-queue songs from a predefined dictionary (Ex. "We Will Rock You / We Are The Champions")
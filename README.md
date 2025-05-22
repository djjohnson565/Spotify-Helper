# ![alt text](./images/logo.png "Spotify-Helper") Spotify-Helper

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

### You Are Good To Go!
Have fun playing around with Spotify-Helper!

## Patch Notes

### v0.0.2 5/22/2025

- Setup instructions
- Improved documentation

### v0.0.1 5/21/2025

- Prompts user for an artist and will display found artist and top 10 tracks.

### v0.0.0 5/20/2025

- Initial commit.
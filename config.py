import os
from dotenv import load_dotenv

load_dotenv()


SPOTIFY_SEARCH_URL = "https://api.spotify.com/v1/search"
YOUTUBE_PLAYLIST_ID = "YOUR-YOUTUBE-PLAYLIST-ID" #Not the whole link, just the ID, for example: https://music.youtube.com/playlist?list=RDCLAK5uy_mAN54iG7e4mH1GxlhPRHopQCW5eXg17LI&playnext=1&si=dxWjVRNpch85-WDL becomes: this is the ID --> RDCLAK5uy_mAN54iG7e4mH1GxlhPRHopQCW5eXg17LI <-- this is the ID
SPOTIFY_PLAYLIST_URL= "https://api.spotify.com/v1/playlists/YOUR-PLAYLIST-ID/tracks" # Same as above, just the ID. https://open.spotify.com/playlist/4dmXcDsH30Jd7G8MFuhKWk becomes: --> 4dmXcDsH30Jd7G8MFuhKWk <-- this is the ID so you change "YOUR-PLAYLIST-ID" to "4dmXcDsH30Jd7G8MFuhKWk"

SPOTIFY_AUTH_TOKEN = os.getenv("SPOTIFY_AUTH_TOKEN")

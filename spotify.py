import requests
from urllib.parse import quote_plus
from ytmusicapi import YTMusic
from config import SPOTIFY_SEARCH_URL , SPOTIFY_AUTH_TOKEN, YOUTUBE_PLAYLIST_ID, SPOTIFY_PLAYLIST_URL


headers = {
    "Authorization": "Bearer " + SPOTIFY_AUTH_TOKEN,
    "Content-Type": "application/json"
}




ytmusic = YTMusic()
content = ytmusic.get_playlist(YOUTUBE_PLAYLIST_ID)


playlistContent = {}
def getPlaylist():
    for track in content.get("tracks", []):
        title = track.get("title")
        artists = [artist["name"] for artist in track.get("artists", [])]
        # print(f"Song: {title}, Artist(s): {', '.join(artists)}")
        playlistContent.update({title: artists})

getPlaylist()

spotifyUrls= []
def searchSongsOnSpotify():
    for song, artist in playlistContent.items():
       
        currentSong = f"{song} {', '.join(artist)}"
      
        finalInput = quote_plus(currentSong)
      
        url = SPOTIFY_SEARCH_URL + "?q=" + finalInput + "&type=track"

       
        response = requests.get(url, headers=headers)
        
      
        if response.status_code == 200:
            data = response.json()  
            spotifyUrls.append(data["tracks"]["items"][0]["external_urls"]["spotify"])
        else:
            print(f"Request failed with status code {response.status_code}")

searchSongsOnSpotify()


def checkIfSongAlreadyInPlaylist():
    playlistUrl = SPOTIFY_PLAYLIST_URL
    response = requests.get(playlistUrl, headers=headers)
    if response.status_code == 200:
        data = response.json()
        for item in data["items"]:
            track = item["track"]
            trackUrl = track["external_urls"]["spotify"]            
            if trackUrl in spotifyUrls:
                print(f"{trackUrl} is already in the playlist. Not adding it again...")
                spotifyUrls.remove(trackUrl)
    else:
        print(f"Request failed with status code {response.status_code}")

checkIfSongAlreadyInPlaylist()
finalSpotifyUrls = []

for url in spotifyUrls:
    newUrl = url.replace("https://open.spotify.com/track/", "spotify:track:")
    finalSpotifyUrls.append(newUrl)

# print(finalSpotifyUrls)

def AddSongsToSpotifyPlaylist():
    
    playlist_url = SPOTIFY_PLAYLIST_URL


   
    data = {
        "uris": finalSpotifyUrls,  
        "position": 0  
    }

  
    response = requests.post(playlist_url, headers=headers, json=data)

  
    if response.status_code == 201:
        print("Tracks added successfully.")
    else:
        print(f"Request failed with status code {response.status_code}: {response.text}")


AddSongsToSpotifyPlaylist()


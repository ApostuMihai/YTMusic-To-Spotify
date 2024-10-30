# YouTube Music to Spotify

# Installation
 
1. Have Python installed on your system
2. Clone this repo
3. Install dependencies with `py -m pip install -r requirements.txt`
4. Add the necessary authorization token in the `.env` file
5. Run the script with `py spotify.py`
6. Enjoy your new playlist, this time on Spotify!

# How to get your authorization token
1. Head to [Spotify developer portal](https://developer.spotify.com/)
2. Log in and then click on "See it in action"
3. On the left there's going to be some JavaScript code with a token: const token = "....". Copy that token and add it in your .env file.
4. For YouTube/Spotify playlists you just get the id from their respective URLs.
5. If you generate an authorization token for Spotify by making a POST request with your client ID and client secret it won't have permission to add songs to a playlist. That's why you need this token. 
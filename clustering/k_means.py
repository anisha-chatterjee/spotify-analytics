import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-top-read"
OAuth = SpotifyOAuth(
        scope=scope,         
        redirect_uri='http://localhost:8888/callback',
        username= 'anishachatty')
sp = spotipy.Spotify(auth_manager=OAuth)

print(sp.current_user_top_tracks())
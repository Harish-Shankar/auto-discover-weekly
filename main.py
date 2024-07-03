import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import datetime

load_dotenv()

client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')
user_id = os.getenv('SPOTIPY_USER_ID')
discover_weekly_playlist_id = os.getenv('SPOTIPY_DISCOVER_WEEKLY_PLAYLIST_ID')
target_playlist_id = os.getenv('SPOTIPY_TARGET_PLAYLIST_ID')

spotifyClient = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope="playlist-modify-public"))


def get_discover_weekly_playlist(playlistID):
    res = spotifyClient.playlist_tracks(playlistID)
    trackIDs = [item['track']['id'] for item in res['items']]
    return trackIDs


def add_tracks(trackIDs, playlistID):
    spotifyClient.playlist_add_items(playlistID, trackIDs)


def update_playlist():
    trackIDs = get_discover_weekly_playlist(discover_weekly_playlist_id)
    add_tracks(trackIDs, target_playlist_id)
    print(f"{len(trackIDs)} tracks added")


if datetime.datetime.today().weekday() == 1:
    update_playlist()

#Credit to Cameron Watts for this tutorial https://towardsdatascience.com/extracting-song-data-from-the-spotify-api-using-python-b1e79388d50 where most of this is lifted from.
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import S

c_id = ""
c_s = ""

if c_id == "":
    c_id = input("Please provide a spotify client id:\n")
if c_s == "":
    c_s = input("Please procide a spotify client secret:\n")

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=c_id, client_secret=c_s))
playlist_parsed = []


def find_playlist(playlist_id):
    playlist_uri = playlist_id.split("/")[-1].split("?")[0]
    spotify_playlist_data = sp.playlist_tracks(playlist_uri)

    tracks = spotify_playlist_data["items"]
    while spotify_playlist_data["next"]:
        spotify_playlist_data = sp.next(spotify_playlist_data)
        tracks.extend(spotify_playlist_data["items"])


    for track in tracks:
        track_name = track["track"]["name"]
        artist_name = track["track"]["artists"][0]["name"]
        playlist_parsed.append((track_name, artist_name))
    return playlist_parsed

def find_track(track_id):
    track_uri = track_id.split("/")[-1].split("?")[0]
    track = sp.track(track_uri)
    track_name = track["name"]
    artist_name = track["artists"][0]["name"]
    return (track_name, artist_name)

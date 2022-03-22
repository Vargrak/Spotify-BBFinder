import SpotifyFind
import BCFind
import requests
import csv
import client



def Spotify_BBFinder():
    print("Welcome to Spotify-BBFinder")
    selection = input("Please Select whether you would like to find: 1.Singular Track, 2.Tracks in a Playlist\n")

    if selection == "1":
        track_id = input("Please enter a track url. Right click on track -> Share -> Copy Song Link\n")
        track = SpotifyFind.find_track(track_id)
        BC_url = BCFind.find_bandcamp(track[0], track[1])
        return_list = [f"{track[0]},{track[1]},{BC_url}"]


    elif selection == "2":
        playlist_id = input("Please enter a playlist url. Right click on playlist -> Share -> Copy Playlist Link\n")
        playlist_parsed = SpotifyFind.find_playlist(playlist_id)
        
        return_list = []
        session = requests.session()
        for song in playlist_parsed:
            BC_url = BCFind.find_bandcamp(song[0], song[1], session)
            return_list.append(f"{song[0]},{song[1]},{BC_url}")
        
    else:
        Spotify_BBFinder()

    with open('Search_Results', 'a') as file:
        file.write('\n'.join(return_list))

Spotify_BBFinder()
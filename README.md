# Spotify-BBFinder
Tool for finding spotify songs on bandcamp. (Beatborp not implemented because it's API is inaccessable to me.)
### Meant for personal use, it requires an API Client ID and API Key currently

Uses Spotipy and some regex to grab songs in spotify from Bandcamp.
Output is a CSV-like format.
Works VERY slowly when regexing through bandcamp as it uses requests and parses the html. (If you think it's stuck, don't worry it's just running very slowly :) )

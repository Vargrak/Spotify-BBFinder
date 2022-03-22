import requests
import regex

def find_bandcamp(track, artist, session):
    track = track.replace(" ", "+")
    input_link = f'https://bandcamp.com/search?q={track}&item_type=t&from=results'

    page = session.get(input_link).text
    bandcamp_match = regex.search(f".*\Khttps.*by {artist}\\n", page, flags=regex.S|regex.I)
    if bandcamp_match == None:
        return "Not Found"
    search_chunk = bandcamp_match[0].replace('<div class="subhead">', '')
    if search_chunk == None:
        return "Not Found"
    url = regex.search('http.*(?=".*)', search_chunk)[0]
    return url
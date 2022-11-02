import spotipy
import requests
from spotipy.oauth2 import SpotifyClientCredentials
import re


ac_uri = "spotify:artist:4kwxTgCKMipBKhSnEstNKj?si=hYX6qZhUThmkqS6Iktd-0Q"

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
results = spotify.artist_top_tracks(ac_uri)
print("Getting top tracks for Animal Collective...\n\n")
for track in results['tracks'][:15]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()
#result = re.findall("My Girls", results)

urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'

artist = spotify.artist(urn)
for k, v in artist.items():
    print("{} : {}\n".format(k,v))

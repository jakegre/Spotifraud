import spotipy
import requests
from spotipy.oauth2 import SpotifyClientCredentials
ac_uri = "spotify:artist:4kwxTgCKMipBKhSnEstNKj?si=hYX6qZhUThmkqS6Iktd-0Q"
lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
results = spotify.artist_top_tracks(ac_uri)

for track in results['tracks'][:15]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()
'''
urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'

artist = spotify.artist(urn)
print(artist)

user = spotify.user('plamere')
print(user)

headers = {
    'Authorization': 'Bearer {token}'.format(token=spotify)
}
# base URL of all Spotify API endpoints
BASE_URL = 'https://api.spotify.com/v1/'

# Track ID from the URI
track_id = '6y0igZArWVi6Iz0rj35c1Y'

# actual GET request with proper header
r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
r = r.json()
print(r)
'''

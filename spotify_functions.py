# Authorization
import os
from dotenv import load_dotenv

# Spotify API
import spotipy

def authorize_user(ID, SECRET, URI, SCOPE):
    
    """
    Builds spotipy object by authorizing user. Authorization keys must be stored in a .env file.

    Params:
    --------
    ID: client id
    SECRET: client secret
    URI: redirect uri (configure on Spotify's developer dashboard)
    SCOPE: scope of query

    Return:
    --------
    Spotipy object

    """

    assert len(ID)>0, 'Please provide a spotify client id'
    assert len(SECRET)>0, 'Please provide a spotify client secret code'

    sp = spotipy.Spotify(
        auth_manager=spotipy.SpotifyOAuth(
            client_id=ID,
            client_secret=SECRET,
            redirect_uri=URI,
            scope=SCOPE, open_browser=True),
            requests_timeout=20, retries=10)
    form_conn = sp.artist('spotify:artist:3jOstUTkEu2JkjvRdBA5Gu')
    print('Authorization Sucessful!')
    return sp

def get_top_artists(sp_object, top_limit):

    """
    Retrieves specified number of top artists from current user (short term)

    Params:
    --------
    sp_object: Spotipy object
    top_limit: Number of top artists

    Return:
    --------
    List of top n artist names and uri

    """

    top_artist_names = []
    top_uri = []
    results = sp_object.current_user_top_artists(limit=top_limit, offset=0, time_range='medium_term')
    for item in results['items'][:top_limit]:
        top_artist_names.append(item['name'])
        top_uri.append(item['uri'])
    return top_artist_names, top_uri

def get_top_cover_art(sp_object, top_uri, top_limit=1):

    """
    Retrieves cover art links for specified artists

    Params:
    --------
    sp_object: Spotipy object
    top_uri: list of top artists uri
    top_limit: Number of top songs

    Return:
    --------
    List of links for top song album covers

    """

    top_cover_art_links = []

    for artist_uri in top_uri:
        result = sp_object.artist_top_tracks(artist_uri)
        for track in result['tracks'][:top_limit]:
            track_name = track['name']
            cover_art_url = track['album']['images'][0]['url']
            top_cover_art_links.append(cover_art_url)
    # print(result)
    return top_cover_art_links
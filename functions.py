CLIENT_ID = "4109b2d9f5014671863bb2df1d1fbdd3"
CLIENT_SECRET = "5cb719fae80c4191a9c0b288f51bfe50"
import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,
                                                           client_secret=CLIENT_SECRET))
def get_artist_id(artist_name):
    result = sp.search(q=artist_name, limit=1, type='artist')
    if result['artists']['items']:
        return result['artists']['items'][0]['id']
    else:
        return None

def get_top_tracks(artist_name):
    # Dummy data for demonstration
    if artist_name == "Los Fabulosos Cadillacs":
        return ["Matador", "Vasos Vacíos", "Mal Bicho", "Siguiendo la Luna", "El Genio del Dub"]
    elif artist_name == "Manu Chao":
        return ["Me Gustas Tú", "Bongo Bong", "Clandestino", "Desaparecido", "La Vida Tómbola"]
    elif artist_name == "Muchachito Bombo Infierno":
        return ["Visto lo Visto", "Ojalá Estuvieras Muerto", "La Quema", "Soy Caminante", "Paquito Tarantino"]
    else:
        return []

def find_related_artists_list(artist_names_list):
    related_artists_list = []
    for artist_name in artist_names_list:
        artist_id = get_artist_id(artist_name)
        if artist_id:
            related_artists = sp.artist_related_artists(artist_id)['artists']
            related_artists_list.append([artist['name'] for artist in related_artists][:5])
        else:
            related_artists_list.append([])
    return related_artists_list
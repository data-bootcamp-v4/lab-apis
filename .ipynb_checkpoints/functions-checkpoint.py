import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials
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
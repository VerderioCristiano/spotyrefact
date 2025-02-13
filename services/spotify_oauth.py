import spotipy
from spotipy.oauth2 import SpotifyOAuth

#le tue credenziali le trovi nella dashboard di prima
SPOTIFY_CLIENT_ID = "79c5d462922a41dca468f6b71d00a504"
SPOTIFY_CLIENT_SECRET = "438ce2ed191742d3a0891ca9134def1a"
SPOTIFY_REDIRECT_URI = "https://verderiocri-spotyrefact-5t0uigz2rmf.ws-eu117.gitpod.io/callback" #dopo il login andiamo qui e va modificato
 #dopo il login andiamo qui

#config SpotifyOAuth per l'autenticazione e redirect uri
sp_oauth = SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-read-private", #permessi x informazioni dell'utente
    show_dialog=True #forziamo la richiesta di inserire new credenziali
)

def get_spotify_object (token_info):
    return spotipy.Spotify(auth=token_info['access_token'])
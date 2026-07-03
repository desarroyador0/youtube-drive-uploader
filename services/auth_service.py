import os
import pickle

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from config import config


SCOPES = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/youtube.upload"
]

TOKEN_PATH = "credentials/token.json"
CLIENT_SECRET = "credentials/client_secret.json"


def obtener_credenciales():

    creds = None

    # ==========================
    # 1. Cargar token existente
    # ==========================
    if os.path.exists(TOKEN_PATH):
        with open(TOKEN_PATH, "rb") as token:
            creds = pickle.load(token)

    # ==========================
    # 2. Refrescar token
    # ==========================
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())

    # ==========================
    # 3. Login inicial
    # ==========================
    if not creds or not creds.valid:

        flow = InstalledAppFlow.from_client_secrets_file(
            CLIENT_SECRET,
            SCOPES
        )

        creds = flow.run_local_server(port=0)

        with open(TOKEN_PATH, "wb") as token:
            pickle.dump(creds, token)

    return creds
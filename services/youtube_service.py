import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

from services.auth_service import obtener_credenciales
from config import config


def autenticar_youtube():

    creds = obtener_credenciales()

    return build("youtube", "v3", credentials=creds)


def subir_video(ruta):

    youtube = autenticar_youtube()
    titulo = os.path.splitext(os.path.basename(ruta))[0]
    request_body = {
        "snippet": {
            "title": titulo,
            "description": config.YOUTUBE_DESCRIPTION,
            "tags": config.YOUTUBE_TAGS,
            "categoryId": config.YOUTUBE_CATEGORY
        },
        "status": {
            "privacyStatus": config.YOUTUBE_PRIVACY
        }
        
    }

    media = MediaFileUpload(ruta, chunksize=-1, resumable=True)

    request = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=media
    )

    response = None

    while response is None:
        status, response = request.next_chunk()

        if status:
            print(f"Subiendo... {int(status.progress() * 100)}%")

    return response["id"]
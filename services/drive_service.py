from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

from services.auth_service import obtener_credenciales

import os
import io


# ==========================
# AUTENTICACIÓN DRIVE
# ==========================
def autenticar_drive():

    creds = obtener_credenciales()

    return build("drive", "v3", credentials=creds)


# ==========================
# LISTAR VIDEOS
# ==========================
def obtener_videos(servicio, folder_id):

    resultados = servicio.files().list(
        q=f"'{folder_id}' in parents and trashed = false",
        fields="files(id, name, createdTime)",
        orderBy="createdTime asc"
    ).execute()

    archivos = resultados.get("files", [])

    videos = [
        f for f in archivos
        if f["name"].lower().endswith((".mp4", ".mov", ".avi", ".mkv"))
    ]

    return videos


# ==========================
# DESCARGAR VIDEO
# ==========================
def descargar_video(servicio, file_id, file_name, download_folder):

    os.makedirs(download_folder, exist_ok=True)

    ruta = os.path.join(download_folder, file_name)

    request = servicio.files().get_media(fileId=file_id)

    with open(ruta, "wb") as f:

        downloader = MediaIoBaseDownload(f, request)

        done = False

        while not done:
            status, done = downloader.next_chunk()

            if status:
                print(f"Descargando... {int(status.progress() * 100)}%")

    return ruta


# ==========================
# MOVER A "SUBIDOS"
# ==========================
def mover_a_subidos(servicio, file_id, folder_destino):

    archivo = servicio.files().get(
        fileId=file_id,
        fields="parents"
    ).execute()

    padres = ",".join(archivo.get("parents", []))

    servicio.files().update(
        fileId=file_id,
        addParents=folder_destino,
        removeParents=padres,
        fields="id, parents"
    ).execute()

    print("📦 Archivo movido a Subidos")
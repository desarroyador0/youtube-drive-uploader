from services.drive_service import (
    autenticar_drive,
    obtener_videos,
    descargar_video,
    mover_a_subidos
)

from services.youtube_service import subir_video

from config import config
from utils.logger import logger
from utils.file_manager import eliminar_archivo


def main():

    logger.info("🚀 Sistema iniciado")

    try:
        # ==========================
        # CONECTAR DRIVE
        # ==========================
        drive = autenticar_drive()

        # ==========================
        # OBTENER VIDEOS
        # ==========================
        videos = obtener_videos(
            drive,
            config.DRIVE_FOLDER_ID
        )

        if not videos:
            logger.warning("📂 No hay videos")
            return

        # Tomamos el más antiguo
        video = videos[0]

        logger.info(f"🎬 Video encontrado: {video['name']}")

        # ==========================
        # DESCARGAR VIDEO
        # ==========================
        ruta = descargar_video(
            drive,
            video["id"],
            video["name"],
            config.DOWNLOAD_FOLDER
        )

        logger.info(f"📥 Descargado en: {ruta}")

        # ==========================
        # SUBIR A YOUTUBE
        # ==========================
        logger.info("⬆️ Subiendo a YouTube...")

        video_id = subir_video(ruta)

        logger.info(f"✅ Video subido: {video_id}")

        # ==========================
        # MOVER EN DRIVE (SUBIDOS)
        # ==========================
        mover_a_subidos(
            drive,
            video["id"],
            config.DRIVE_UPLOADED_FOLDER_ID
        )

        logger.info("📦 Movido a carpeta Subidos")

        # ==========================
        # LIMPIEZA LOCAL
        # ==========================
        eliminar_archivo(ruta)

        logger.info("🧹 Limpieza local completada")

        logger.info("🎉 PROCESO FINALIZADO CON ÉXITO")

    except Exception as e:
        logger.error(f"❌ Error en el sistema: {e}")


if __name__ == "__main__":
    main()
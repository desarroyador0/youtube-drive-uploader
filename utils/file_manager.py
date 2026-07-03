import os
import glob


def eliminar_archivo(ruta):

    if os.path.exists(ruta):
        os.remove(ruta)
        print(f"🗑️ Archivo eliminado: {ruta}")


def limpiar_carpeta(download_folder):

    archivos = glob.glob(os.path.join(download_folder, "*"))

    for archivo in archivos:
        try:
            os.remove(archivo)
            print(f"🧹 Eliminado: {archivo}")
        except Exception as e:
            print(f"⚠️ No se pudo eliminar {archivo}: {e}")
from services.ai_service import generar_metadata

metadata = generar_metadata(
    "Tina_teaches_number_one_202607090130.mp4"
)

print(metadata)
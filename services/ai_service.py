import json

from google import genai

from config import config


client = genai.Client(
    api_key=config.GEMINI_API_KEY
)


def generar_metadata(nombre_archivo):

    prompt = f"""
Eres un experto en YouTube SEO y contenido infantil.

El canal se llama "InfantEnglish".

El personaje principal es Tina, una elefante animada que enseña inglés a niños hispanohablantes mediante videos muy cortos.

El nombre del archivo es:

{nombre_archivo}

Reglas:

1. Elimina la extensión (.mp4, .mov, etc.).
2. Elimina cualquier fecha u hora al final del nombre.
   Ejemplo:
   Tina_teaches_number_one_202607090130
   debe interpretarse como:
   Tina teaches number one
3. Interpreta el tema del video.
4. Genera un título atractivo en español.
5. El título debe ser corto, natural y pensado para YouTube Shorts.
6. Genera una descripción de máximo 2 oraciones.
7. La descripción debe invitar a aprender inglés de forma divertida.
8. Finaliza con exactamente 7 hashtags relacionados con:
   - aprender inglés
   - niños
   - educación
   - InfantEnglish
   - Tina
   - el tema del video

IMPORTANTE:

Responde ÚNICAMENTE un JSON válido con este formato:

{{
    "titulo": "...",
    "descripcion": "..."
}}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json"
        }
    )

    return json.loads(response.text)
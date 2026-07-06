from google import genai

from config import config


client = genai.Client(
    api_key=config.GEMINI_API_KEY
)


def generar_descripcion(titulo):

    prompt = f"""
Eres el redactor del canal de YouTube "InfantEnglish".

El personaje principal es Tina, una elefante animada que enseña inglés a niños.

A partir del siguiente título:

{titulo}

Genera:

- Una descripción de máximo 2 oraciones.
- Que sea alegre, amigable y atrapante.
- Pensada para padres y niños.
- No uses demasiados emojis (máximo 2).
- Finaliza con exactamente 7 hashtags relacionados con:
    - inglés
    - niños
    - educación
    - InfantEnglish
    - Tina
    - el tema del video

Devuelve únicamente la descripción.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip()
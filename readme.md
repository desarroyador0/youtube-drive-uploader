# YouTube Drive Uploader

Automatiza la publicación de videos en YouTube a partir de una carpeta de Google Drive.

## Flujo

1. Busca videos en la carpeta "Pendientes".
2. Descarga el video más antiguo.
3. Lo publica en YouTube.
4. Mueve el archivo a la carpeta "Subidos".

## Tecnologías

- Python
- Google Drive API
- YouTube Data API v3
- GitHub Actions

## Configuración

1. Copiar:

```text
.env.example
```

como:

```text
.env
```

2. Completar las variables.

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Ejecutar:

```bash
python main.py
```
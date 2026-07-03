import logging
import os

from datetime import datetime


LOG_FOLDER = "logs"

os.makedirs(LOG_FOLDER, exist_ok=True)

LOG_FILE = os.path.join(
    LOG_FOLDER,
    f"{datetime.now().strftime('%Y-%m-%d')}.log"
)


logger = logging.getLogger("youtube_uploader")

logger.setLevel(logging.INFO)

logger.handlers.clear()


formatter = logging.Formatter(
    "[%(asctime)s] %(levelname)s - %(message)s",
    "%Y-%m-%d %H:%M:%S"
)


# ==========================
# Consola
# ==========================

console_handler = logging.StreamHandler()

console_handler.setFormatter(formatter)

logger.addHandler(console_handler)


# ==========================
# Archivo
# ==========================

file_handler = logging.FileHandler(
    LOG_FILE,
    encoding="utf-8"
)

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
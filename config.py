import os

from dotenv import load_dotenv


class Config:

    def __init__(self):

        load_dotenv()

        # ==========================
        # Google Drive
        # ==========================

        self.DRIVE_FOLDER_ID = os.getenv("DRIVE_FOLDER_ID")
        self.DRIVE_UPLOADED_FOLDER_ID = os.getenv("DRIVE_UPLOADED_FOLDER_ID")

        # ==========================
        # Descargas
        # ==========================

        self.DOWNLOAD_FOLDER = os.getenv(
            "DOWNLOAD_FOLDER",
            "downloads"
        )

        # ==========================
        # YouTube
        # ==========================

        self.YOUTUBE_PRIVACY = os.getenv(
            "YOUTUBE_PRIVACY",
            "private"
        )

        self.YOUTUBE_CATEGORY = os.getenv(
            "YOUTUBE_CATEGORY",
            "22"
        )
        # ==========================
        # Gemini
        # ==========================

        self.GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

        self.YOUTUBE_DESCRIPTION = os.getenv(
            "YOUTUBE_DESCRIPTION",
            ""
        )

        tags = os.getenv(
            "YOUTUBE_TAGS",
            ""
        )

        self.YOUTUBE_TAGS = [
            tag.strip()
            for tag in tags.split(",")
            if tag.strip()
        ]

        # ==========================
        # Scheduler
        # ==========================

        self.CHECK_INTERVAL_HOURS = float(
            os.getenv(
                "CHECK_INTERVAL_HOURS",
                "5"
            )
        )
        


config = Config()
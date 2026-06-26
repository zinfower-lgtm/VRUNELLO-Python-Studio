"""
VRUNELLO Creator Studio
Log Service
"""

from __future__ import annotations

import logging
from pathlib import Path


class LogService:

    LOG_DIR = Path("logs")
    LOG_FILE = LOG_DIR / "app.log"

    def __init__(self):

        self.LOG_DIR.mkdir(exist_ok=True)

        self.logger = logging.getLogger("VRUNELLO")

        if self.logger.handlers:
            return

        self.logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(message)s"
        )

        file_handler = logging.FileHandler(
            self.LOG_FILE,
            encoding="utf-8"
        )

        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

    def info(self, message: str):

        self.logger.info(message)

    def warning(self, message: str):

        self.logger.warning(message)

    def error(self, message: str):

        self.logger.error(message)

    def debug(self, message: str):

        self.logger.debug(message)
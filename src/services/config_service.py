"""
VRUNELLO Creator Studio
Config Service

프로그램 설정을 읽고 저장하는 서비스
"""

from __future__ import annotations

import json
from pathlib import Path


class ConfigService:

    CONFIG_DIR = Path("config")
    CONFIG_FILE = CONFIG_DIR / "settings.json"

    DEFAULT_CONFIG = {
        "theme": "dark",
        "language": "ko",
        "window_width": 1600,
        "window_height": 900,
        "last_project": "",
        "recent_projects": []
    }

    def __init__(self):

        self.CONFIG_DIR.mkdir(exist_ok=True)

        if not self.CONFIG_FILE.exists():
            self.save(self.DEFAULT_CONFIG)

    def load(self):

        try:

            with open(self.CONFIG_FILE, "r", encoding="utf-8") as f:
                return json.load(f)

        except (FileNotFoundError, json.JSONDecodeError):

            self.save(self.DEFAULT_CONFIG)

            return self.DEFAULT_CONFIG

    def save(self, data):

        with open(self.CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )
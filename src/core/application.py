"""
VRUNELLO Creator Studio
Application Core
"""

from src.services.config_service import ConfigService
from src.services.log_service import LogService
from src.core.event_bus import EventBus


class Application:

    def __init__(self):

        self.config = ConfigService()
        self.logger = LogService()
        self.events = EventBus()

        self.logger.info("Application Initialized")


app = Application()
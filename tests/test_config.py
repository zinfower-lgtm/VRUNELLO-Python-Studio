from src.services.config_service import ConfigService

config = ConfigService()

data = config.load()

print(data)
from src.services.log_service import LogService

log = LogService()

log.info("Application Started")
log.warning("Image Missing")
log.error("Gemini API Error")
log.info("Project Loaded")

print("Logger Test OK")
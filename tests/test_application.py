from src.core.application import app


print("Theme :", app.config.load()["theme"])

app.logger.info("Application Test")

def test(name):
    print(f"Event Received : {name}")

app.events.subscribe("test", test)

app.events.publish("test", "VRUNELLO")
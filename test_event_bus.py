from src.core.event_bus import EventBus

bus = EventBus()


def explorer(name):
    print(f"[Explorer] 프로젝트 생성 : {name}")


def logger(name):
    print(f"[Logger] 기록 완료 : {name}")


def status(name):
    print(f"[StatusBar] {name} Ready")


bus.subscribe("project_created", explorer)
bus.subscribe("project_created", logger)
bus.subscribe("project_created", status)

bus.publish("project_created", "Summer Escape")
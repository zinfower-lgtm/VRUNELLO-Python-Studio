"""
VRUNELLO Creator Studio
Event Bus
"""

from collections import defaultdict
from typing import Callable


class EventBus:

    def __init__(self):

        self._events = defaultdict(list)

    def subscribe(self, event_name: str, callback: Callable):

        self._events[event_name].append(callback)

    def publish(self, event_name: str, *args, **kwargs):

        for callback in self._events[event_name]:
            callback(*args, **kwargs)

    def unsubscribe(self, event_name: str, callback: Callable):

        if callback in self._events[event_name]:
            self._events[event_name].remove(callback)
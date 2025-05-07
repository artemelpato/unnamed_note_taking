from typing import Callable, Any

class Command:
    name: str
    callback: Callable[[Any], bool]

    def __init__(self) -> None:
        self.name = "unknown"
        self.callback = lambda x: True

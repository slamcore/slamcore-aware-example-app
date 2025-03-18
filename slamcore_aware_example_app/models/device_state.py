from enum import Enum


class DeviceState(str, Enum):
    ERROR = "error"
    LOCALISATION = "localisation"
    MAPPING = "mapping"
    OFFLINE = "offline"
    READY = "ready"
    STARTING = "starting"
    STOPPING = "stopping"

    def __str__(self) -> str:
        return str(self.value)

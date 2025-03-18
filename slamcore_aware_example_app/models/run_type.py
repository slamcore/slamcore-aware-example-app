from enum import Enum


class RunType(str, Enum):
    LOCALISATION = "localisation"
    MAPPING = "mapping"
    PASS_THROUGH = "pass through"

    def __str__(self) -> str:
        return str(self.value)

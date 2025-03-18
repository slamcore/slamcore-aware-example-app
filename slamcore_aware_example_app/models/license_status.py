from enum import Enum


class LicenseStatus(str, Enum):
    ACTIVE = "active"
    EXPIRED = "expired"
    INVALID = "invalid"
    MISSING_DEVICE = "missing_device"
    NOT_FOUND = "not_found"
    WRONG_DEVICE = "wrong_device"

    def __str__(self) -> str:
        return str(self.value)

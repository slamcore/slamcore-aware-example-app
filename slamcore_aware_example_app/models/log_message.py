from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LogMessage")


@_attrs_define
class LogMessage:
    """Log message.

    Attributes:
        severity (int): Log message severity.
        message (str): Log message content.
        timestamp (float): Log message timestamp.
    """

    severity: int
    message: str
    timestamp: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        severity = self.severity

        message = self.message

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "severity": severity,
                "message": message,
                "timestamp": timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        severity = d.pop("severity")

        message = d.pop("message")

        timestamp = d.pop("timestamp")

        log_message = cls(
            severity=severity,
            message=message,
            timestamp=timestamp,
        )

        log_message.additional_properties = d
        return log_message

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

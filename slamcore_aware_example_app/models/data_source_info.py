from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DataSourceInfo")


@_attrs_define
class DataSourceInfo:
    """
    Attributes:
        manufacturer (str):
        model (str):
        serial_number (str):
        firmware_version (str):
    """

    manufacturer: str
    model: str
    serial_number: str
    firmware_version: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        manufacturer = self.manufacturer

        model = self.model

        serial_number = self.serial_number

        firmware_version = self.firmware_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "manufacturer": manufacturer,
                "model": model,
                "serial_number": serial_number,
                "firmware_version": firmware_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        manufacturer = d.pop("manufacturer")

        model = d.pop("model")

        serial_number = d.pop("serial_number")

        firmware_version = d.pop("firmware_version")

        data_source_info = cls(
            manufacturer=manufacturer,
            model=model,
            serial_number=serial_number,
            firmware_version=firmware_version,
        )

        data_source_info.additional_properties = d
        return data_source_info

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

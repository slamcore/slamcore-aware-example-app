from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.data_source_info import DataSourceInfo


T = TypeVar("T", bound="SystemInfo")


@_attrs_define
class SystemInfo:
    """
    Attributes:
        software_version (str):
        cameras (list[DataSourceInfo]):
    """

    software_version: str
    cameras: list[DataSourceInfo]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        software_version = self.software_version

        cameras = []
        for cameras_item_data in self.cameras:
            cameras_item = cameras_item_data.to_dict()
            cameras.append(cameras_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "software_version": software_version,
                "cameras": cameras,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_source_info import DataSourceInfo

        d = dict(src_dict)
        software_version = d.pop("software_version")

        cameras = []
        _cameras = d.pop("cameras")
        for cameras_item_data in _cameras:
            cameras_item = DataSourceInfo.from_dict(cameras_item_data)

            cameras.append(cameras_item)

        system_info = cls(
            software_version=software_version,
            cameras=cameras,
        )

        system_info.additional_properties = d
        return system_info

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

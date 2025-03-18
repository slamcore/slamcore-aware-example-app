from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SlamMarkerFeatures")


@_attrs_define
class SlamMarkerFeatures:
    """SLAM marker related features.

    Attributes:
        detector (bool):
        database (bool):
    """

    detector: bool
    database: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        detector = self.detector

        database = self.database

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "detector": detector,
                "database": database,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        detector = d.pop("detector")

        database = d.pop("database")

        slam_marker_features = cls(
            detector=detector,
            database=database,
        )

        slam_marker_features.additional_properties = d
        return slam_marker_features

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

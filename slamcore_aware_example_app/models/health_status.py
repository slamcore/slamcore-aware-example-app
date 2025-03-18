from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.license_status import LicenseStatus

T = TypeVar("T", bound="HealthStatus")


@_attrs_define
class HealthStatus:
    """Device health status.

    Attributes:
        license_ (LicenseStatus): License status.

            Active: License is active
            Expired: License has expired
            Invalid: License file is invalid
            Not Found: License file not found
            Wrong Device: License file is for a different device
            Missing Device: Device information is not available
        camera (bool): Whether the camera connection is OK.
    """

    license_: LicenseStatus
    camera: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        license_ = self.license_.value

        camera = self.camera

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "license": license_,
                "camera": camera,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        license_ = LicenseStatus(d.pop("license"))

        camera = d.pop("camera")

        health_status = cls(
            license_=license_,
            camera=camera,
        )

        health_status.additional_properties = d
        return health_status

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

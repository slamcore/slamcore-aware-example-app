from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.device_state import DeviceState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.health_status import HealthStatus
    from ..models.slam_system_status import SlamSystemStatus


T = TypeVar("T", bound="DeviceStatus")


@_attrs_define
class DeviceStatus:
    """Device status.

    Attributes:
        state (DeviceState): Operation state of the Aware device.
        sessions (list[str]): List of available maps on the Slamcore Aware device.
        health (HealthStatus): Device health status.
        external_storage (bool): External storage is mounted.
        sloc_active (bool): SLOC sensor is activated.
        slam_state (None | SlamSystemStatus | Unset): Current status of the SLAM system.
    """

    state: DeviceState
    sessions: list[str]
    health: HealthStatus
    external_storage: bool
    sloc_active: bool
    slam_state: None | SlamSystemStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.slam_system_status import SlamSystemStatus

        state = self.state.value

        sessions = self.sessions

        health = self.health.to_dict()

        external_storage = self.external_storage

        sloc_active = self.sloc_active

        slam_state: dict[str, Any] | None | Unset
        if isinstance(self.slam_state, Unset):
            slam_state = UNSET
        elif isinstance(self.slam_state, SlamSystemStatus):
            slam_state = self.slam_state.to_dict()
        else:
            slam_state = self.slam_state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
                "sessions": sessions,
                "health": health,
                "external_storage": external_storage,
                "sloc_active": sloc_active,
            }
        )
        if slam_state is not UNSET:
            field_dict["slam_state"] = slam_state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.health_status import HealthStatus
        from ..models.slam_system_status import SlamSystemStatus

        d = dict(src_dict)
        state = DeviceState(d.pop("state"))

        sessions = cast(list[str], d.pop("sessions"))

        health = HealthStatus.from_dict(d.pop("health"))

        external_storage = d.pop("external_storage")

        sloc_active = d.pop("sloc_active")

        def _parse_slam_state(data: object) -> None | SlamSystemStatus | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                slam_state_type_0 = SlamSystemStatus.from_dict(data)

                return slam_state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SlamSystemStatus | Unset, data)

        slam_state = _parse_slam_state(d.pop("slam_state", UNSET))

        device_status = cls(
            state=state,
            sessions=sessions,
            health=health,
            external_storage=external_storage,
            sloc_active=sloc_active,
            slam_state=slam_state,
        )

        device_status.additional_properties = d
        return device_status

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

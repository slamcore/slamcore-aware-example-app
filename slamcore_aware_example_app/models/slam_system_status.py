from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.run_type import RunType

if TYPE_CHECKING:
    from ..models.slam_features import SlamFeatures


T = TypeVar("T", bound="SlamSystemStatus")


@_attrs_define
class SlamSystemStatus:
    """Slam system status.

    Attributes:
        run_uuid (UUID): UUID of the current SLAM run.
        start_time (datetime.datetime): Start time of the current SLAM run.
        mode (RunType): Type of SLAM run.
        input_map (str): Name of map used as input for SLAM.
        output_map (str): Name of map to be generated at the end of SLAM.
        features (SlamFeatures): SLAM features enabled for the current run.
    """

    run_uuid: UUID
    start_time: datetime.datetime
    mode: RunType
    input_map: str
    output_map: str
    features: SlamFeatures
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run_uuid = str(self.run_uuid)

        start_time = self.start_time.isoformat()

        mode = self.mode.value

        input_map = self.input_map

        output_map = self.output_map

        features = self.features.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "run_uuid": run_uuid,
                "start_time": start_time,
                "mode": mode,
                "input_map": input_map,
                "output_map": output_map,
                "features": features,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slam_features import SlamFeatures

        d = dict(src_dict)
        run_uuid = UUID(d.pop("run_uuid"))

        start_time = isoparse(d.pop("start_time"))

        mode = RunType(d.pop("mode"))

        input_map = d.pop("input_map")

        output_map = d.pop("output_map")

        features = SlamFeatures.from_dict(d.pop("features"))

        slam_system_status = cls(
            run_uuid=run_uuid,
            start_time=start_time,
            mode=mode,
            input_map=input_map,
            output_map=output_map,
            features=features,
        )

        slam_system_status.additional_properties = d
        return slam_system_status

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

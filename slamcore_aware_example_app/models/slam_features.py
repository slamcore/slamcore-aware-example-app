from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.slam_marker_features import SlamMarkerFeatures
    from ..models.slam_perception_features import SlamPerceptionFeatures


T = TypeVar("T", bound="SlamFeatures")


@_attrs_define
class SlamFeatures:
    """SLAM features enabled for the current run.

    Attributes:
        markers (Union['SlamMarkerFeatures', None]):
        perception (Union['SlamPerceptionFeatures', None]):
    """

    markers: Union["SlamMarkerFeatures", None]
    perception: Union["SlamPerceptionFeatures", None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.slam_marker_features import SlamMarkerFeatures
        from ..models.slam_perception_features import SlamPerceptionFeatures

        markers: None | dict[str, Any]
        if isinstance(self.markers, SlamMarkerFeatures):
            markers = self.markers.to_dict()
        else:
            markers = self.markers

        perception: None | dict[str, Any]
        if isinstance(self.perception, SlamPerceptionFeatures):
            perception = self.perception.to_dict()
        else:
            perception = self.perception

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "markers": markers,
                "perception": perception,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.slam_marker_features import SlamMarkerFeatures
        from ..models.slam_perception_features import SlamPerceptionFeatures

        d = dict(src_dict)

        def _parse_markers(data: object) -> Union["SlamMarkerFeatures", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                markers_type_0 = SlamMarkerFeatures.from_dict(data)

                return markers_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SlamMarkerFeatures", None], data)

        markers = _parse_markers(d.pop("markers"))

        def _parse_perception(data: object) -> Union["SlamPerceptionFeatures", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                perception_type_0 = SlamPerceptionFeatures.from_dict(data)

                return perception_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SlamPerceptionFeatures", None], data)

        perception = _parse_perception(d.pop("perception"))

        slam_features = cls(
            markers=markers,
            perception=perception,
        )

        slam_features.additional_properties = d
        return slam_features

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

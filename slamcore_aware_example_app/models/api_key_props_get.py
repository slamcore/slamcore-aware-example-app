import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="APIKeyPropsGet")


@_attrs_define
class APIKeyPropsGet:
    """
    Attributes:
        last_3_chars (str):
        expires_at (Union[None, datetime.datetime]):
        description (Union[None, str]):
    """

    last_3_chars: str
    expires_at: None | datetime.datetime
    description: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_3_chars = self.last_3_chars

        expires_at: None | str
        if isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        description: None | str
        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "last_3_chars": last_3_chars,
                "expires_at": expires_at,
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        last_3_chars = d.pop("last_3_chars")

        def _parse_expires_at(data: object) -> None | datetime.datetime:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = isoparse(data)

                return expires_at_type_0
            except:  # noqa: E722
                pass
            return cast(None | datetime.datetime, data)

        expires_at = _parse_expires_at(d.pop("expires_at"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        api_key_props_get = cls(
            last_3_chars=last_3_chars,
            expires_at=expires_at,
            description=description,
        )

        api_key_props_get.additional_properties = d
        return api_key_props_get

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

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileResp")


@_attrs_define
class FileResp:
    """
    Attributes:
        filename (str):
        bytes_ (int):
        purpose (str):
        id (UUID):
        created_at (datetime.datetime):
        expires_at (Union[None, Unset, datetime.datetime]):
        object_ (Union[Unset, str]):  Default: 'file'.
    """

    filename: str
    bytes_: int
    purpose: str
    id: UUID
    created_at: datetime.datetime
    expires_at: Union[None, Unset, datetime.datetime] = UNSET
    object_: Union[Unset, str] = "file"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filename = self.filename

        bytes_ = self.bytes_

        purpose = self.purpose

        id = str(self.id)

        created_at = self.created_at.isoformat()

        expires_at: Union[None, Unset, str]
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        object_ = self.object_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filename": filename,
                "bytes": bytes_,
                "purpose": purpose,
                "id": id,
                "created_at": created_at,
            }
        )
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if object_ is not UNSET:
            field_dict["object"] = object_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        filename = d.pop("filename")

        bytes_ = d.pop("bytes")

        purpose = d.pop("purpose")

        id = UUID(d.pop("id"))

        created_at = isoparse(d.pop("created_at"))

        def _parse_expires_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = isoparse(data)

                return expires_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        object_ = d.pop("object", UNSET)

        file_resp = cls(
            filename=filename,
            bytes_=bytes_,
            purpose=purpose,
            id=id,
            created_at=created_at,
            expires_at=expires_at,
            object_=object_,
        )

        file_resp.additional_properties = d
        return file_resp

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

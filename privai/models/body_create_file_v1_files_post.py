from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="BodyCreateFileV1FilesPost")


@_attrs_define
class BodyCreateFileV1FilesPost:
    """
    Attributes:
        file (File):
        extra_metadata (Union[None, Unset, str]):  Default: '{}'.
    """

    file: File
    extra_metadata: Union[None, Unset, str] = "{}"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_tuple()

        extra_metadata: Union[None, Unset, str]
        if isinstance(self.extra_metadata, Unset):
            extra_metadata = UNSET
        else:
            extra_metadata = self.extra_metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
            }
        )
        if extra_metadata is not UNSET:
            field_dict["extra_metadata"] = extra_metadata

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("file", self.file.to_tuple()))

        if not isinstance(self.extra_metadata, Unset):
            if isinstance(self.extra_metadata, str):
                files.append(("extra_metadata", (None, str(self.extra_metadata).encode(), "text/plain")))
            else:
                files.append(("extra_metadata", (None, str(self.extra_metadata).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = File(payload=BytesIO(d.pop("file")))

        def _parse_extra_metadata(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        extra_metadata = _parse_extra_metadata(d.pop("extra_metadata", UNSET))

        body_create_file_v1_files_post = cls(
            file=file,
            extra_metadata=extra_metadata,
        )

        body_create_file_v1_files_post.additional_properties = d
        return body_create_file_v1_files_post

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

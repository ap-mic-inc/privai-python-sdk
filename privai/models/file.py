import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.file_state import FileState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_metadata import FileMetadata


T = TypeVar("T", bound="File")


@_attrs_define
class File:
    """
    Attributes:
        id (UUID):
        created_at (datetime.datetime):
        filetype (str):
        state (FileState):
        metadata (Union[Unset, FileMetadata]):
        raw_file_url (Union[None, Unset, str]):
        parsed_result_url (Union[None, Unset, str]):
        chunks_url (Union[None, Unset, str]):
    """

    id: UUID
    created_at: datetime.datetime
    filetype: str
    state: FileState
    metadata: Union[Unset, "FileMetadata"] = UNSET
    raw_file_url: Union[None, Unset, str] = UNSET
    parsed_result_url: Union[None, Unset, str] = UNSET
    chunks_url: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        created_at = self.created_at.isoformat()

        filetype = self.filetype

        state = self.state.value

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        raw_file_url: Union[None, Unset, str]
        if isinstance(self.raw_file_url, Unset):
            raw_file_url = UNSET
        else:
            raw_file_url = self.raw_file_url

        parsed_result_url: Union[None, Unset, str]
        if isinstance(self.parsed_result_url, Unset):
            parsed_result_url = UNSET
        else:
            parsed_result_url = self.parsed_result_url

        chunks_url: Union[None, Unset, str]
        if isinstance(self.chunks_url, Unset):
            chunks_url = UNSET
        else:
            chunks_url = self.chunks_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "filetype": filetype,
                "state": state,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if raw_file_url is not UNSET:
            field_dict["raw_file_url"] = raw_file_url
        if parsed_result_url is not UNSET:
            field_dict["parsed_result_url"] = parsed_result_url
        if chunks_url is not UNSET:
            field_dict["chunks_url"] = chunks_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_metadata import FileMetadata

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        created_at = isoparse(d.pop("created_at"))

        filetype = d.pop("filetype")

        state = FileState(d.pop("state"))

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, FileMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = FileMetadata.from_dict(_metadata)

        def _parse_raw_file_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        raw_file_url = _parse_raw_file_url(d.pop("raw_file_url", UNSET))

        def _parse_parsed_result_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parsed_result_url = _parse_parsed_result_url(d.pop("parsed_result_url", UNSET))

        def _parse_chunks_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        chunks_url = _parse_chunks_url(d.pop("chunks_url", UNSET))

        file = cls(
            id=id,
            created_at=created_at,
            filetype=filetype,
            state=state,
            metadata=metadata,
            raw_file_url=raw_file_url,
            parsed_result_url=parsed_result_url,
            chunks_url=chunks_url,
        )

        file.additional_properties = d
        return file

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

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_counts import FileCounts
    from ..models.fileset_response_metadata_type_0 import FilesetResponseMetadataType0


T = TypeVar("T", bound="FilesetResponse")


@_attrs_define
class FilesetResponse:
    """
    Attributes:
        id (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        file_counts (FileCounts):
        object_ (Union[Unset, str]):  Default: 'fileset'.
        metadata (Union['FilesetResponseMetadataType0', None, Unset]):
        state (Union[Unset, str]):  Default: 'draft'.
        committed_at (Union[None, Unset, datetime.datetime]):
    """

    id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    file_counts: "FileCounts"
    object_: Union[Unset, str] = "fileset"
    metadata: Union["FilesetResponseMetadataType0", None, Unset] = UNSET
    state: Union[Unset, str] = "draft"
    committed_at: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.fileset_response_metadata_type_0 import FilesetResponseMetadataType0

        id = str(self.id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        file_counts = self.file_counts.to_dict()

        object_ = self.object_

        metadata: Union[None, Unset, dict[str, Any]]
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, FilesetResponseMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        state = self.state

        committed_at: Union[None, Unset, str]
        if isinstance(self.committed_at, Unset):
            committed_at = UNSET
        elif isinstance(self.committed_at, datetime.datetime):
            committed_at = self.committed_at.isoformat()
        else:
            committed_at = self.committed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "updated_at": updated_at,
                "file_counts": file_counts,
            }
        )
        if object_ is not UNSET:
            field_dict["object"] = object_
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if state is not UNSET:
            field_dict["state"] = state
        if committed_at is not UNSET:
            field_dict["committed_at"] = committed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_counts import FileCounts
        from ..models.fileset_response_metadata_type_0 import FilesetResponseMetadataType0

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        file_counts = FileCounts.from_dict(d.pop("file_counts"))

        object_ = d.pop("object", UNSET)

        def _parse_metadata(data: object) -> Union["FilesetResponseMetadataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = FilesetResponseMetadataType0.from_dict(data)

                return metadata_type_0
            except:  # noqa: E722
                pass
            return cast(Union["FilesetResponseMetadataType0", None, Unset], data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        state = d.pop("state", UNSET)

        def _parse_committed_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                committed_at_type_0 = isoparse(data)

                return committed_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        committed_at = _parse_committed_at(d.pop("committed_at", UNSET))

        fileset_response = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            file_counts=file_counts,
            object_=object_,
            metadata=metadata,
            state=state,
            committed_at=committed_at,
        )

        fileset_response.additional_properties = d
        return fileset_response

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

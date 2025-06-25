from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fileset_create_metadata_type_0 import FilesetCreateMetadataType0


T = TypeVar("T", bound="FilesetCreate")


@_attrs_define
class FilesetCreate:
    """
    Attributes:
        id (Union[None, UUID, Unset]):
        metadata (Union['FilesetCreateMetadataType0', None, Unset]):
        file_ids (Union[None, Unset, list[UUID]]):
    """

    id: Union[None, UUID, Unset] = UNSET
    metadata: Union["FilesetCreateMetadataType0", None, Unset] = UNSET
    file_ids: Union[None, Unset, list[UUID]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.fileset_create_metadata_type_0 import FilesetCreateMetadataType0

        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        metadata: Union[None, Unset, dict[str, Any]]
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, FilesetCreateMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        file_ids: Union[None, Unset, list[str]]
        if isinstance(self.file_ids, Unset):
            file_ids = UNSET
        elif isinstance(self.file_ids, list):
            file_ids = []
            for file_ids_type_0_item_data in self.file_ids:
                file_ids_type_0_item = str(file_ids_type_0_item_data)
                file_ids.append(file_ids_type_0_item)

        else:
            file_ids = self.file_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if file_ids is not UNSET:
            field_dict["file_ids"] = file_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fileset_create_metadata_type_0 import FilesetCreateMetadataType0

        d = dict(src_dict)

        def _parse_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_metadata(data: object) -> Union["FilesetCreateMetadataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = FilesetCreateMetadataType0.from_dict(data)

                return metadata_type_0
            except:  # noqa: E722
                pass
            return cast(Union["FilesetCreateMetadataType0", None, Unset], data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_file_ids(data: object) -> Union[None, Unset, list[UUID]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                file_ids_type_0 = []
                _file_ids_type_0 = data
                for file_ids_type_0_item_data in _file_ids_type_0:
                    file_ids_type_0_item = UUID(file_ids_type_0_item_data)

                    file_ids_type_0.append(file_ids_type_0_item)

                return file_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[UUID]], data)

        file_ids = _parse_file_ids(d.pop("file_ids", UNSET))

        fileset_create = cls(
            id=id,
            metadata=metadata,
            file_ids=file_ids,
        )

        fileset_create.additional_properties = d
        return fileset_create

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

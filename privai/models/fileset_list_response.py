from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fileset_response import FilesetResponse


T = TypeVar("T", bound="FilesetListResponse")


@_attrs_define
class FilesetListResponse:
    """
    Attributes:
        data (list['FilesetResponse']):
        has_more (bool):
        object_ (Union[Unset, str]):  Default: 'list'.
        first_id (Union[None, UUID, Unset]):
        last_id (Union[None, UUID, Unset]):
    """

    data: list["FilesetResponse"]
    has_more: bool
    object_: Union[Unset, str] = "list"
    first_id: Union[None, UUID, Unset] = UNSET
    last_id: Union[None, UUID, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        has_more = self.has_more

        object_ = self.object_

        first_id: Union[None, Unset, str]
        if isinstance(self.first_id, Unset):
            first_id = UNSET
        elif isinstance(self.first_id, UUID):
            first_id = str(self.first_id)
        else:
            first_id = self.first_id

        last_id: Union[None, Unset, str]
        if isinstance(self.last_id, Unset):
            last_id = UNSET
        elif isinstance(self.last_id, UUID):
            last_id = str(self.last_id)
        else:
            last_id = self.last_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "has_more": has_more,
            }
        )
        if object_ is not UNSET:
            field_dict["object"] = object_
        if first_id is not UNSET:
            field_dict["first_id"] = first_id
        if last_id is not UNSET:
            field_dict["last_id"] = last_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fileset_response import FilesetResponse

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = FilesetResponse.from_dict(data_item_data)

            data.append(data_item)

        has_more = d.pop("has_more")

        object_ = d.pop("object", UNSET)

        def _parse_first_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_id_type_0 = UUID(data)

                return first_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        first_id = _parse_first_id(d.pop("first_id", UNSET))

        def _parse_last_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_id_type_0 = UUID(data)

                return last_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        last_id = _parse_last_id(d.pop("last_id", UNSET))

        fileset_list_response = cls(
            data=data,
            has_more=has_more,
            object_=object_,
            first_id=first_id,
            last_id=last_id,
        )

        fileset_list_response.additional_properties = d
        return fileset_list_response

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

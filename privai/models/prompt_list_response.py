from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.prompt_list_response_data_item import PromptListResponseDataItem


T = TypeVar("T", bound="PromptListResponse")


@_attrs_define
class PromptListResponse:
    """
    Attributes:
        object_ (str):
        data (list['PromptListResponseDataItem']):
        first_id (Union[None, UUID]):
        last_id (Union[None, UUID]):
        has_more (bool):
    """

    object_: str
    data: list["PromptListResponseDataItem"]
    first_id: Union[None, UUID]
    last_id: Union[None, UUID]
    has_more: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        first_id: Union[None, str]
        if isinstance(self.first_id, UUID):
            first_id = str(self.first_id)
        else:
            first_id = self.first_id

        last_id: Union[None, str]
        if isinstance(self.last_id, UUID):
            last_id = str(self.last_id)
        else:
            last_id = self.last_id

        has_more = self.has_more

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "data": data,
                "first_id": first_id,
                "last_id": last_id,
                "has_more": has_more,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.prompt_list_response_data_item import PromptListResponseDataItem

        d = dict(src_dict)
        object_ = d.pop("object")

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = PromptListResponseDataItem.from_dict(data_item_data)

            data.append(data_item)

        def _parse_first_id(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_id_type_0 = UUID(data)

                return first_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        first_id = _parse_first_id(d.pop("first_id"))

        def _parse_last_id(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_id_type_0 = UUID(data)

                return last_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        last_id = _parse_last_id(d.pop("last_id"))

        has_more = d.pop("has_more")

        prompt_list_response = cls(
            object_=object_,
            data=data,
            first_id=first_id,
            last_id=last_id,
            has_more=has_more,
        )

        prompt_list_response.additional_properties = d
        return prompt_list_response

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

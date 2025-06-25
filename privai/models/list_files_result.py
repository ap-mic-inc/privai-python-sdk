from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file import File
    from ..models.file_resp import FileResp


T = TypeVar("T", bound="ListFilesResult")


@_attrs_define
class ListFilesResult:
    """
    Attributes:
        data (Union[list['File'], list['FileResp']]):
        has_more (bool):
        object_ (Union[Unset, str]):  Default: 'list'.
    """

    data: Union[list["File"], list["FileResp"]]
    has_more: bool
    object_: Union[Unset, str] = "list"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]]
        if isinstance(self.data, list):
            data = []
            for data_type_0_item_data in self.data:
                data_type_0_item = data_type_0_item_data.to_dict()
                data.append(data_type_0_item)

        else:
            data = []
            for data_type_1_item_data in self.data:
                data_type_1_item = data_type_1_item_data.to_dict()
                data.append(data_type_1_item)

        has_more = self.has_more

        object_ = self.object_

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file import File
        from ..models.file_resp import FileResp

        d = dict(src_dict)

        def _parse_data(data: object) -> Union[list["File"], list["FileResp"]]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                data_type_0 = []
                _data_type_0 = data
                for data_type_0_item_data in _data_type_0:
                    data_type_0_item = FileResp.from_dict(data_type_0_item_data)

                    data_type_0.append(data_type_0_item)

                return data_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, list):
                raise TypeError()
            data_type_1 = []
            _data_type_1 = data
            for data_type_1_item_data in _data_type_1:
                data_type_1_item = File.from_dict(data_type_1_item_data)

                data_type_1.append(data_type_1_item)

            return data_type_1

        data = _parse_data(d.pop("data"))

        has_more = d.pop("has_more")

        object_ = d.pop("object", UNSET)

        list_files_result = cls(
            data=data,
            has_more=has_more,
            object_=object_,
        )

        list_files_result.additional_properties = d
        return list_files_result

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

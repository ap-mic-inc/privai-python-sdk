from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileCounts")


@_attrs_define
class FileCounts:
    """
    Attributes:
        draft (Union[Unset, int]):  Default: 0.
        processing (Union[Unset, int]):  Default: 0.
        completed (Union[Unset, int]):  Default: 0.
        failed (Union[Unset, int]):  Default: 0.
        total (Union[Unset, int]):  Default: 0.
    """

    draft: Union[Unset, int] = 0
    processing: Union[Unset, int] = 0
    completed: Union[Unset, int] = 0
    failed: Union[Unset, int] = 0
    total: Union[Unset, int] = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        draft = self.draft

        processing = self.processing

        completed = self.completed

        failed = self.failed

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if draft is not UNSET:
            field_dict["draft"] = draft
        if processing is not UNSET:
            field_dict["processing"] = processing
        if completed is not UNSET:
            field_dict["completed"] = completed
        if failed is not UNSET:
            field_dict["failed"] = failed
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        draft = d.pop("draft", UNSET)

        processing = d.pop("processing", UNSET)

        completed = d.pop("completed", UNSET)

        failed = d.pop("failed", UNSET)

        total = d.pop("total", UNSET)

        file_counts = cls(
            draft=draft,
            processing=processing,
            completed=completed,
            failed=failed,
            total=total,
        )

        file_counts.additional_properties = d
        return file_counts

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

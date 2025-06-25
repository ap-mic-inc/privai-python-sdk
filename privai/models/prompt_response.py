import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.prompt_response_metadata import PromptResponseMetadata


T = TypeVar("T", bound="PromptResponse")


@_attrs_define
class PromptResponse:
    """
    Attributes:
        id (UUID):
        value (str):
        metadata (PromptResponseMetadata):
        created_at (datetime.datetime):
    """

    id: UUID
    value: str
    metadata: "PromptResponseMetadata"
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        value = self.value

        metadata = self.metadata.to_dict()

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "value": value,
                "metadata": metadata,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.prompt_response_metadata import PromptResponseMetadata

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        value = d.pop("value")

        metadata = PromptResponseMetadata.from_dict(d.pop("metadata"))

        created_at = isoparse(d.pop("created_at"))

        prompt_response = cls(
            id=id,
            value=value,
            metadata=metadata,
            created_at=created_at,
        )

        prompt_response.additional_properties = d
        return prompt_response

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

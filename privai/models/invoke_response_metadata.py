from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.feedback_token import FeedbackToken


T = TypeVar("T", bound="InvokeResponseMetadata")


@_attrs_define
class InvokeResponseMetadata:
    """Represents response metadata used for just single input/output LangServe
    responses.

        Attributes:
            run_id (UUID):
            feedback_tokens (list['FeedbackToken']): Feedback tokens from the given run.These tokens allow a user to provide
                feedback on the run.Only available if server was configured to provide feedback tokens.
    """

    run_id: UUID
    feedback_tokens: list["FeedbackToken"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run_id = str(self.run_id)

        feedback_tokens = []
        for feedback_tokens_item_data in self.feedback_tokens:
            feedback_tokens_item = feedback_tokens_item_data.to_dict()
            feedback_tokens.append(feedback_tokens_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "run_id": run_id,
                "feedback_tokens": feedback_tokens,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.feedback_token import FeedbackToken

        d = dict(src_dict)
        run_id = UUID(d.pop("run_id"))

        feedback_tokens = []
        _feedback_tokens = d.pop("feedback_tokens")
        for feedback_tokens_item_data in _feedback_tokens:
            feedback_tokens_item = FeedbackToken.from_dict(feedback_tokens_item_data)

            feedback_tokens.append(feedback_tokens_item)

        invoke_response_metadata = cls(
            run_id=run_id,
            feedback_tokens=feedback_tokens,
        )

        invoke_response_metadata.additional_properties = d
        return invoke_response_metadata

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

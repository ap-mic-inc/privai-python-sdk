from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GenerateQaReq")


@_attrs_define
class GenerateQaReq:
    """
    Attributes:
        model_name (Union[Unset, str]): Model name for generating QA pairs Default: 'azure-gpt-4o'.
        extract_model_name (Union[Unset, str]): Model name for extracting QA pairs. Only support non thinking models.
            Default: 'azure-gpt-4o'.
        temperature (Union[Unset, float]): Temperature for the model, between 0 and 1 Default: 0.7.
        target_amount (Union[Unset, int]): Target amount of QA questions to generate per 500 words Default: 1.
    """

    model_name: Union[Unset, str] = "azure-gpt-4o"
    extract_model_name: Union[Unset, str] = "azure-gpt-4o"
    temperature: Union[Unset, float] = 0.7
    target_amount: Union[Unset, int] = 1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_name = self.model_name

        extract_model_name = self.extract_model_name

        temperature = self.temperature

        target_amount = self.target_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if model_name is not UNSET:
            field_dict["model_name"] = model_name
        if extract_model_name is not UNSET:
            field_dict["extract_model_name"] = extract_model_name
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if target_amount is not UNSET:
            field_dict["target_amount"] = target_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model_name = d.pop("model_name", UNSET)

        extract_model_name = d.pop("extract_model_name", UNSET)

        temperature = d.pop("temperature", UNSET)

        target_amount = d.pop("target_amount", UNSET)

        generate_qa_req = cls(
            model_name=model_name,
            extract_model_name=extract_model_name,
            temperature=temperature,
            target_amount=target_amount,
        )

        generate_qa_req.additional_properties = d
        return generate_qa_req

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

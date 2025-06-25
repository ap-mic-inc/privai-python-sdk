from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IntelichatReq")


@_attrs_define
class IntelichatReq:
    """
    Attributes:
        fileset_id (str):
        prompt_id (str):
        question (str):
        llm_name (Union[Unset, str]):  Default: 'azure-gpt-4o'.
        embedding_model_name (Union[Unset, str]):  Default: 'llama-3.2-nv-embedqa-1b-v2'.
        rerank_model_name (Union[None, Unset, str]):  Default: 'llama-3.2-nv-rerankqa-1b-v2'.
    """

    fileset_id: str
    prompt_id: str
    question: str
    llm_name: Union[Unset, str] = "azure-gpt-4o"
    embedding_model_name: Union[Unset, str] = "llama-3.2-nv-embedqa-1b-v2"
    rerank_model_name: Union[None, Unset, str] = "llama-3.2-nv-rerankqa-1b-v2"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fileset_id = self.fileset_id

        prompt_id = self.prompt_id

        question = self.question

        llm_name = self.llm_name

        embedding_model_name = self.embedding_model_name

        rerank_model_name: Union[None, Unset, str]
        if isinstance(self.rerank_model_name, Unset):
            rerank_model_name = UNSET
        else:
            rerank_model_name = self.rerank_model_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fileset_id": fileset_id,
                "prompt_id": prompt_id,
                "question": question,
            }
        )
        if llm_name is not UNSET:
            field_dict["llm_name"] = llm_name
        if embedding_model_name is not UNSET:
            field_dict["embedding_model_name"] = embedding_model_name
        if rerank_model_name is not UNSET:
            field_dict["rerank_model_name"] = rerank_model_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fileset_id = d.pop("fileset_id")

        prompt_id = d.pop("prompt_id")

        question = d.pop("question")

        llm_name = d.pop("llm_name", UNSET)

        embedding_model_name = d.pop("embedding_model_name", UNSET)

        def _parse_rerank_model_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        rerank_model_name = _parse_rerank_model_name(d.pop("rerank_model_name", UNSET))

        intelichat_req = cls(
            fileset_id=fileset_id,
            prompt_id=prompt_id,
            question=question,
            llm_name=llm_name,
            embedding_model_name=embedding_model_name,
            rerank_model_name=rerank_model_name,
        )

        intelichat_req.additional_properties = d
        return intelichat_req

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

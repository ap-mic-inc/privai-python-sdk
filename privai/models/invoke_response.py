from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.intelichat_resp import IntelichatResp
    from ..models.invoke_response_metadata import InvokeResponseMetadata


T = TypeVar("T", bound="InvokeResponse")


@_attrs_define
class InvokeResponse:
    """
    Attributes:
        output (IntelichatResp):
        metadata (InvokeResponseMetadata): Represents response metadata used for just single input/output LangServe
            responses.
    """

    output: "IntelichatResp"
    metadata: "InvokeResponseMetadata"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        output = self.output.to_dict()

        metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "output": output,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.intelichat_resp import IntelichatResp
        from ..models.invoke_response_metadata import InvokeResponseMetadata

        d = dict(src_dict)
        output = IntelichatResp.from_dict(d.pop("output"))

        metadata = InvokeResponseMetadata.from_dict(d.pop("metadata"))

        invoke_response = cls(
            output=output,
            metadata=metadata,
        )

        invoke_response.additional_properties = d
        return invoke_response

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

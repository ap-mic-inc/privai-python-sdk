from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inteli_chain_config import InteliChainConfig
    from ..models.intelichat_req import IntelichatReq
    from ..models.stream_request_kwargs import StreamRequestKwargs


T = TypeVar("T", bound="StreamRequest")


@_attrs_define
class StreamRequest:
    """
    Attributes:
        input_ (IntelichatReq):
        config (Union[Unset, InteliChainConfig]):
        kwargs (Union[Unset, StreamRequestKwargs]): Keyword arguments to the runnable. Currently ignored.
    """

    input_: "IntelichatReq"
    config: Union[Unset, "InteliChainConfig"] = UNSET
    kwargs: Union[Unset, "StreamRequestKwargs"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_ = self.input_.to_dict()

        config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        kwargs: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.kwargs, Unset):
            kwargs = self.kwargs.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "input": input_,
            }
        )
        if config is not UNSET:
            field_dict["config"] = config
        if kwargs is not UNSET:
            field_dict["kwargs"] = kwargs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inteli_chain_config import InteliChainConfig
        from ..models.intelichat_req import IntelichatReq
        from ..models.stream_request_kwargs import StreamRequestKwargs

        d = dict(src_dict)
        input_ = IntelichatReq.from_dict(d.pop("input"))

        _config = d.pop("config", UNSET)
        config: Union[Unset, InteliChainConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = InteliChainConfig.from_dict(_config)

        _kwargs = d.pop("kwargs", UNSET)
        kwargs: Union[Unset, StreamRequestKwargs]
        if isinstance(_kwargs, Unset):
            kwargs = UNSET
        else:
            kwargs = StreamRequestKwargs.from_dict(_kwargs)

        stream_request = cls(
            input_=input_,
            config=config,
            kwargs=kwargs,
        )

        stream_request.additional_properties = d
        return stream_request

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

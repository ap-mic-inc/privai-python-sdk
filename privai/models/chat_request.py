from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_request_search_kwargs_type_0 import ChatRequestSearchKwargsType0
    from ..models.message import Message


T = TypeVar("T", bound="ChatRequest")


@_attrs_define
class ChatRequest:
    """
    Attributes:
        model (str):
        messages (list['Message']):
        stream (Union[Unset, bool]):  Default: False.
        search_kwargs (Union['ChatRequestSearchKwargsType0', None, Unset]):
        prompt (Union[None, Unset, str]):
        prompt_id (Union[None, Unset, str]):
        fileset_id (Union[None, Unset, str]):
        temperature (Union[None, Unset, float]):
    """

    model: str
    messages: list["Message"]
    stream: Union[Unset, bool] = False
    search_kwargs: Union["ChatRequestSearchKwargsType0", None, Unset] = UNSET
    prompt: Union[None, Unset, str] = UNSET
    prompt_id: Union[None, Unset, str] = UNSET
    fileset_id: Union[None, Unset, str] = UNSET
    temperature: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.chat_request_search_kwargs_type_0 import ChatRequestSearchKwargsType0

        model = self.model

        messages = []
        for messages_item_data in self.messages:
            messages_item = messages_item_data.to_dict()
            messages.append(messages_item)

        stream = self.stream

        search_kwargs: Union[None, Unset, dict[str, Any]]
        if isinstance(self.search_kwargs, Unset):
            search_kwargs = UNSET
        elif isinstance(self.search_kwargs, ChatRequestSearchKwargsType0):
            search_kwargs = self.search_kwargs.to_dict()
        else:
            search_kwargs = self.search_kwargs

        prompt: Union[None, Unset, str]
        if isinstance(self.prompt, Unset):
            prompt = UNSET
        else:
            prompt = self.prompt

        prompt_id: Union[None, Unset, str]
        if isinstance(self.prompt_id, Unset):
            prompt_id = UNSET
        else:
            prompt_id = self.prompt_id

        fileset_id: Union[None, Unset, str]
        if isinstance(self.fileset_id, Unset):
            fileset_id = UNSET
        else:
            fileset_id = self.fileset_id

        temperature: Union[None, Unset, float]
        if isinstance(self.temperature, Unset):
            temperature = UNSET
        else:
            temperature = self.temperature

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model": model,
                "messages": messages,
            }
        )
        if stream is not UNSET:
            field_dict["stream"] = stream
        if search_kwargs is not UNSET:
            field_dict["search_kwargs"] = search_kwargs
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if prompt_id is not UNSET:
            field_dict["prompt_id"] = prompt_id
        if fileset_id is not UNSET:
            field_dict["fileset_id"] = fileset_id
        if temperature is not UNSET:
            field_dict["temperature"] = temperature

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_request_search_kwargs_type_0 import ChatRequestSearchKwargsType0
        from ..models.message import Message

        d = dict(src_dict)
        model = d.pop("model")

        messages = []
        _messages = d.pop("messages")
        for messages_item_data in _messages:
            messages_item = Message.from_dict(messages_item_data)

            messages.append(messages_item)

        stream = d.pop("stream", UNSET)

        def _parse_search_kwargs(data: object) -> Union["ChatRequestSearchKwargsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                search_kwargs_type_0 = ChatRequestSearchKwargsType0.from_dict(data)

                return search_kwargs_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ChatRequestSearchKwargsType0", None, Unset], data)

        search_kwargs = _parse_search_kwargs(d.pop("search_kwargs", UNSET))

        def _parse_prompt(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        prompt = _parse_prompt(d.pop("prompt", UNSET))

        def _parse_prompt_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        prompt_id = _parse_prompt_id(d.pop("prompt_id", UNSET))

        def _parse_fileset_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        fileset_id = _parse_fileset_id(d.pop("fileset_id", UNSET))

        def _parse_temperature(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        temperature = _parse_temperature(d.pop("temperature", UNSET))

        chat_request = cls(
            model=model,
            messages=messages,
            stream=stream,
            search_kwargs=search_kwargs,
            prompt=prompt,
            prompt_id=prompt_id,
            fileset_id=fileset_id,
            temperature=temperature,
        )

        chat_request.additional_properties = d
        return chat_request

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

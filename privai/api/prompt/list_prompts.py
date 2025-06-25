from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.order import Order
from ...models.prompt_list_response import PromptListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, int] = 20,
    order: Union[Unset, Order] = UNSET,
    after: Union[None, UUID, Unset] = UNSET,
    before: Union[None, UUID, Unset] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    json_after: Union[None, Unset, str]
    if isinstance(after, Unset):
        json_after = UNSET
    elif isinstance(after, UUID):
        json_after = str(after)
    else:
        json_after = after
    params["after"] = json_after

    json_before: Union[None, Unset, str]
    if isinstance(before, Unset):
        json_before = UNSET
    elif isinstance(before, UUID):
        json_before = str(before)
    else:
        json_before = before
    params["before"] = json_before

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/prompt",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, PromptListResponse]]:
    if response.status_code == 200:
        response_200 = PromptListResponse.from_dict(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPValidationError, PromptListResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = 20,
    order: Union[Unset, Order] = UNSET,
    after: Union[None, UUID, Unset] = UNSET,
    before: Union[None, UUID, Unset] = UNSET,
) -> Response[Union[HTTPValidationError, PromptListResponse]]:
    """List Prompts

     列出 prompts，支援 cursor-based 分頁

    Args:
        limit (Union[Unset, int]):  Default: 20.
        order (Union[Unset, Order]): Order Enum for sorting.
        after (Union[None, UUID, Unset]):
        before (Union[None, UUID, Unset]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, PromptListResponse]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        order=order,
        after=after,
        before=before,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = 20,
    order: Union[Unset, Order] = UNSET,
    after: Union[None, UUID, Unset] = UNSET,
    before: Union[None, UUID, Unset] = UNSET,
) -> Optional[Union[HTTPValidationError, PromptListResponse]]:
    """List Prompts

     列出 prompts，支援 cursor-based 分頁

    Args:
        limit (Union[Unset, int]):  Default: 20.
        order (Union[Unset, Order]): Order Enum for sorting.
        after (Union[None, UUID, Unset]):
        before (Union[None, UUID, Unset]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, PromptListResponse]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        order=order,
        after=after,
        before=before,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = 20,
    order: Union[Unset, Order] = UNSET,
    after: Union[None, UUID, Unset] = UNSET,
    before: Union[None, UUID, Unset] = UNSET,
) -> Response[Union[HTTPValidationError, PromptListResponse]]:
    """List Prompts

     列出 prompts，支援 cursor-based 分頁

    Args:
        limit (Union[Unset, int]):  Default: 20.
        order (Union[Unset, Order]): Order Enum for sorting.
        after (Union[None, UUID, Unset]):
        before (Union[None, UUID, Unset]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, PromptListResponse]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        order=order,
        after=after,
        before=before,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = 20,
    order: Union[Unset, Order] = UNSET,
    after: Union[None, UUID, Unset] = UNSET,
    before: Union[None, UUID, Unset] = UNSET,
) -> Optional[Union[HTTPValidationError, PromptListResponse]]:
    """List Prompts

     列出 prompts，支援 cursor-based 分頁

    Args:
        limit (Union[Unset, int]):  Default: 20.
        order (Union[Unset, Order]): Order Enum for sorting.
        after (Union[None, UUID, Unset]):
        before (Union[None, UUID, Unset]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, PromptListResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            order=order,
            after=after,
            before=before,
        )
    ).parsed

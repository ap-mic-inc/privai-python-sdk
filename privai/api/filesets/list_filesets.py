from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fileset_list_response import FilesetListResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.order import Order
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, int] = 10000,
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
        "url": "/v1/filesets",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[FilesetListResponse, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = FilesetListResponse.from_dict(response.json())

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
) -> Response[Union[FilesetListResponse, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = 10000,
    order: Union[Unset, Order] = UNSET,
    after: Union[None, UUID, Unset] = UNSET,
    before: Union[None, UUID, Unset] = UNSET,
) -> Response[Union[FilesetListResponse, HTTPValidationError]]:
    """List Filesets

     獲取所有 fileset，支援分頁和排序

    Args:
        limit: 返回的物件數量限制，範圍 1-10000，預設 10000
        order: 排序方式，asc 為升序，desc 為降序，預設 desc
        after: 分頁游標，用於獲取指定 ID 之後的資料
        before: 分頁游標，用於獲取指定 ID 之前的資料，與 after 互斥

    Args:
        limit (Union[Unset, int]):  Default: 10000.
        order (Union[Unset, Order]): Order Enum for sorting.
        after (Union[None, UUID, Unset]):
        before (Union[None, UUID, Unset]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[FilesetListResponse, HTTPValidationError]]
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
    limit: Union[Unset, int] = 10000,
    order: Union[Unset, Order] = UNSET,
    after: Union[None, UUID, Unset] = UNSET,
    before: Union[None, UUID, Unset] = UNSET,
) -> Optional[Union[FilesetListResponse, HTTPValidationError]]:
    """List Filesets

     獲取所有 fileset，支援分頁和排序

    Args:
        limit: 返回的物件數量限制，範圍 1-10000，預設 10000
        order: 排序方式，asc 為升序，desc 為降序，預設 desc
        after: 分頁游標，用於獲取指定 ID 之後的資料
        before: 分頁游標，用於獲取指定 ID 之前的資料，與 after 互斥

    Args:
        limit (Union[Unset, int]):  Default: 10000.
        order (Union[Unset, Order]): Order Enum for sorting.
        after (Union[None, UUID, Unset]):
        before (Union[None, UUID, Unset]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[FilesetListResponse, HTTPValidationError]
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
    limit: Union[Unset, int] = 10000,
    order: Union[Unset, Order] = UNSET,
    after: Union[None, UUID, Unset] = UNSET,
    before: Union[None, UUID, Unset] = UNSET,
) -> Response[Union[FilesetListResponse, HTTPValidationError]]:
    """List Filesets

     獲取所有 fileset，支援分頁和排序

    Args:
        limit: 返回的物件數量限制，範圍 1-10000，預設 10000
        order: 排序方式，asc 為升序，desc 為降序，預設 desc
        after: 分頁游標，用於獲取指定 ID 之後的資料
        before: 分頁游標，用於獲取指定 ID 之前的資料，與 after 互斥

    Args:
        limit (Union[Unset, int]):  Default: 10000.
        order (Union[Unset, Order]): Order Enum for sorting.
        after (Union[None, UUID, Unset]):
        before (Union[None, UUID, Unset]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[FilesetListResponse, HTTPValidationError]]
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
    limit: Union[Unset, int] = 10000,
    order: Union[Unset, Order] = UNSET,
    after: Union[None, UUID, Unset] = UNSET,
    before: Union[None, UUID, Unset] = UNSET,
) -> Optional[Union[FilesetListResponse, HTTPValidationError]]:
    """List Filesets

     獲取所有 fileset，支援分頁和排序

    Args:
        limit: 返回的物件數量限制，範圍 1-10000，預設 10000
        order: 排序方式，asc 為升序，desc 為降序，預設 desc
        after: 分頁游標，用於獲取指定 ID 之後的資料
        before: 分頁游標，用於獲取指定 ID 之前的資料，與 after 互斥

    Args:
        limit (Union[Unset, int]):  Default: 10000.
        order (Union[Unset, Order]): Order Enum for sorting.
        after (Union[None, UUID, Unset]):
        before (Union[None, UUID, Unset]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[FilesetListResponse, HTTPValidationError]
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

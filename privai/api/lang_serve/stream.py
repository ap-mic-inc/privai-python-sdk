from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.stream_request import StreamRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: StreamRequest,
    config_hash: Union[Unset, str] = "",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["config_hash"] = config_hash

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/stream",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Union[Any, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: StreamRequest,
    config_hash: Union[Unset, str] = "",
) -> Response[Union[Any, HTTPValidationError]]:
    """Stream

     This endpoint allows to stream the output of the runnable. The endpoint uses a server sent event
    stream to stream the output. https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events

    Args:
        config_hash (Union[Unset, str]):  Default: ''.
        body (StreamRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        body=body,
        config_hash=config_hash,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: StreamRequest,
    config_hash: Union[Unset, str] = "",
) -> Optional[Union[Any, HTTPValidationError]]:
    """Stream

     This endpoint allows to stream the output of the runnable. The endpoint uses a server sent event
    stream to stream the output. https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events

    Args:
        config_hash (Union[Unset, str]):  Default: ''.
        body (StreamRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        body=body,
        config_hash=config_hash,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: StreamRequest,
    config_hash: Union[Unset, str] = "",
) -> Response[Union[Any, HTTPValidationError]]:
    """Stream

     This endpoint allows to stream the output of the runnable. The endpoint uses a server sent event
    stream to stream the output. https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events

    Args:
        config_hash (Union[Unset, str]):  Default: ''.
        body (StreamRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        body=body,
        config_hash=config_hash,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: StreamRequest,
    config_hash: Union[Unset, str] = "",
) -> Optional[Union[Any, HTTPValidationError]]:
    """Stream

     This endpoint allows to stream the output of the runnable. The endpoint uses a server sent event
    stream to stream the output. https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events

    Args:
        config_hash (Union[Unset, str]):  Default: ''.
        body (StreamRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            config_hash=config_hash,
        )
    ).parsed

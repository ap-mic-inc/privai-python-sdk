from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.invoke_request import InvokeRequest
from ...models.invoke_response import InvokeResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: InvokeRequest,
    config_hash: Union[Unset, str] = "",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["config_hash"] = config_hash

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/invoke",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, InvokeResponse]]:
    if response.status_code == 200:
        response_200 = InvokeResponse.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, InvokeResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: InvokeRequest,
    config_hash: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, InvokeResponse]]:
    """Invoke

     Invoke the runnable with the given input and config.

    Args:
        config_hash (Union[Unset, str]):  Default: ''.
        body (InvokeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, InvokeResponse]]
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
    body: InvokeRequest,
    config_hash: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, InvokeResponse]]:
    """Invoke

     Invoke the runnable with the given input and config.

    Args:
        config_hash (Union[Unset, str]):  Default: ''.
        body (InvokeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, InvokeResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
        config_hash=config_hash,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: InvokeRequest,
    config_hash: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, InvokeResponse]]:
    """Invoke

     Invoke the runnable with the given input and config.

    Args:
        config_hash (Union[Unset, str]):  Default: ''.
        body (InvokeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, InvokeResponse]]
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
    body: InvokeRequest,
    config_hash: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, InvokeResponse]]:
    """Invoke

     Invoke the runnable with the given input and config.

    Args:
        config_hash (Union[Unset, str]):  Default: ''.
        body (InvokeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, InvokeResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            config_hash=config_hash,
        )
    ).parsed

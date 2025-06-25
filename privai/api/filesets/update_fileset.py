from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fileset_response import FilesetResponse
from ...models.fileset_update import FilesetUpdate
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    filesets_id: UUID,
    *,
    body: FilesetUpdate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/v1/filesets/{filesets_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[FilesetResponse, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = FilesetResponse.from_dict(response.json())

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
) -> Response[Union[FilesetResponse, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    filesets_id: UUID,
    *,
    client: AuthenticatedClient,
    body: FilesetUpdate,
) -> Response[Union[FilesetResponse, HTTPValidationError]]:
    """Update Fileset

     更新特定 fileset

    Args:
        filesets_id: fileset ID
        fileset: 要更新的 fileset 資料

    Args:
        filesets_id (UUID):
        body (FilesetUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[FilesetResponse, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        filesets_id=filesets_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    filesets_id: UUID,
    *,
    client: AuthenticatedClient,
    body: FilesetUpdate,
) -> Optional[Union[FilesetResponse, HTTPValidationError]]:
    """Update Fileset

     更新特定 fileset

    Args:
        filesets_id: fileset ID
        fileset: 要更新的 fileset 資料

    Args:
        filesets_id (UUID):
        body (FilesetUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[FilesetResponse, HTTPValidationError]
    """

    return sync_detailed(
        filesets_id=filesets_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    filesets_id: UUID,
    *,
    client: AuthenticatedClient,
    body: FilesetUpdate,
) -> Response[Union[FilesetResponse, HTTPValidationError]]:
    """Update Fileset

     更新特定 fileset

    Args:
        filesets_id: fileset ID
        fileset: 要更新的 fileset 資料

    Args:
        filesets_id (UUID):
        body (FilesetUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[FilesetResponse, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        filesets_id=filesets_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    filesets_id: UUID,
    *,
    client: AuthenticatedClient,
    body: FilesetUpdate,
) -> Optional[Union[FilesetResponse, HTTPValidationError]]:
    """Update Fileset

     更新特定 fileset

    Args:
        filesets_id: fileset ID
        fileset: 要更新的 fileset 資料

    Args:
        filesets_id (UUID):
        body (FilesetUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[FilesetResponse, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            filesets_id=filesets_id,
            client=client,
            body=body,
        )
    ).parsed

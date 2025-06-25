from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file_type import FileType
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    file_id: UUID,
    *,
    file_type: Union[Unset, FileType] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_file_type: Union[Unset, str] = UNSET
    if not isinstance(file_type, Unset):
        json_file_type = file_type.value

    params["file_type"] = json_file_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/files/{file_id}/content",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
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
    file_id: UUID,
    *,
    client: AuthenticatedClient,
    file_type: Union[Unset, FileType] = UNSET,
) -> Response[Union[Any, HTTPValidationError]]:
    """Download File

     Returns the contents of the specified file.

    Args:
        file_id (str): The ID of the file to download.

    Returns:
        str: The file content.

    Args:
        file_id (UUID):
        file_type (Union[Unset, FileType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        file_id=file_id,
        file_type=file_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    file_id: UUID,
    *,
    client: AuthenticatedClient,
    file_type: Union[Unset, FileType] = UNSET,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Download File

     Returns the contents of the specified file.

    Args:
        file_id (str): The ID of the file to download.

    Returns:
        str: The file content.

    Args:
        file_id (UUID):
        file_type (Union[Unset, FileType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        file_id=file_id,
        client=client,
        file_type=file_type,
    ).parsed


async def asyncio_detailed(
    file_id: UUID,
    *,
    client: AuthenticatedClient,
    file_type: Union[Unset, FileType] = UNSET,
) -> Response[Union[Any, HTTPValidationError]]:
    """Download File

     Returns the contents of the specified file.

    Args:
        file_id (str): The ID of the file to download.

    Returns:
        str: The file content.

    Args:
        file_id (UUID):
        file_type (Union[Unset, FileType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        file_id=file_id,
        file_type=file_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    file_id: UUID,
    *,
    client: AuthenticatedClient,
    file_type: Union[Unset, FileType] = UNSET,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Download File

     Returns the contents of the specified file.

    Args:
        file_id (str): The ID of the file to download.

    Returns:
        str: The file content.

    Args:
        file_id (UUID):
        file_type (Union[Unset, FileType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            file_id=file_id,
            client=client,
            file_type=file_type,
        )
    ).parsed

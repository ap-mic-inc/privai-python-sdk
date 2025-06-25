from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file_resp import FileResp
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    file_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/files/{file_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[FileResp, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = FileResp.from_dict(response.json())

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
) -> Response[Union[FileResp, HTTPValidationError]]:
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
) -> Response[Union[FileResp, HTTPValidationError]]:
    """Get File

     Returns information about a specific file.

    Args:
        file_id (str): The ID of the file to retrieve.

    Returns:
        File: The [File] object matching the specified ID.
        The File object has the following attributes:
        - id: UUID
        - created_at: datetime
        - metadata: Dict[str, Any]
        - filetype: str

    Args:
        file_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[FileResp, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        file_id=file_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    file_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[FileResp, HTTPValidationError]]:
    """Get File

     Returns information about a specific file.

    Args:
        file_id (str): The ID of the file to retrieve.

    Returns:
        File: The [File] object matching the specified ID.
        The File object has the following attributes:
        - id: UUID
        - created_at: datetime
        - metadata: Dict[str, Any]
        - filetype: str

    Args:
        file_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[FileResp, HTTPValidationError]
    """

    return sync_detailed(
        file_id=file_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    file_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Union[FileResp, HTTPValidationError]]:
    """Get File

     Returns information about a specific file.

    Args:
        file_id (str): The ID of the file to retrieve.

    Returns:
        File: The [File] object matching the specified ID.
        The File object has the following attributes:
        - id: UUID
        - created_at: datetime
        - metadata: Dict[str, Any]
        - filetype: str

    Args:
        file_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[FileResp, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        file_id=file_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    file_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[FileResp, HTTPValidationError]]:
    """Get File

     Returns information about a specific file.

    Args:
        file_id (str): The ID of the file to retrieve.

    Returns:
        File: The [File] object matching the specified ID.
        The File object has the following attributes:
        - id: UUID
        - created_at: datetime
        - metadata: Dict[str, Any]
        - filetype: str

    Args:
        file_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[FileResp, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            file_id=file_id,
            client=client,
        )
    ).parsed

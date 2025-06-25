from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_create_file_v1_files_post import BodyCreateFileV1FilesPost
from ...models.file_resp import FileResp
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BodyCreateFileV1FilesPost,
    purpose: Union[Unset, str] = "user_data",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["purpose"] = purpose

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/files",
        "params": params,
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
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
    *,
    client: AuthenticatedClient,
    body: BodyCreateFileV1FilesPost,
    purpose: Union[Unset, str] = "user_data",
) -> Response[Union[FileResp, HTTPValidationError]]:
    """Create File

     Uploads a file.

    Args:
        file (UploadFile): The file to upload.
        purpose (str): The purpose of the file.
        extra_metadata (dict, optional): Additional metadata to store with the file. Defaults to None.

    Returns:
        dict: The uploaded [File]

    Args:
        purpose (Union[Unset, str]):  Default: 'user_data'.
        body (BodyCreateFileV1FilesPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[FileResp, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        body=body,
        purpose=purpose,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: BodyCreateFileV1FilesPost,
    purpose: Union[Unset, str] = "user_data",
) -> Optional[Union[FileResp, HTTPValidationError]]:
    """Create File

     Uploads a file.

    Args:
        file (UploadFile): The file to upload.
        purpose (str): The purpose of the file.
        extra_metadata (dict, optional): Additional metadata to store with the file. Defaults to None.

    Returns:
        dict: The uploaded [File]

    Args:
        purpose (Union[Unset, str]):  Default: 'user_data'.
        body (BodyCreateFileV1FilesPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[FileResp, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        body=body,
        purpose=purpose,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyCreateFileV1FilesPost,
    purpose: Union[Unset, str] = "user_data",
) -> Response[Union[FileResp, HTTPValidationError]]:
    """Create File

     Uploads a file.

    Args:
        file (UploadFile): The file to upload.
        purpose (str): The purpose of the file.
        extra_metadata (dict, optional): Additional metadata to store with the file. Defaults to None.

    Returns:
        dict: The uploaded [File]

    Args:
        purpose (Union[Unset, str]):  Default: 'user_data'.
        body (BodyCreateFileV1FilesPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[FileResp, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        body=body,
        purpose=purpose,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BodyCreateFileV1FilesPost,
    purpose: Union[Unset, str] = "user_data",
) -> Optional[Union[FileResp, HTTPValidationError]]:
    """Create File

     Uploads a file.

    Args:
        file (UploadFile): The file to upload.
        purpose (str): The purpose of the file.
        extra_metadata (dict, optional): Additional metadata to store with the file. Defaults to None.

    Returns:
        dict: The uploaded [File]

    Args:
        purpose (Union[Unset, str]):  Default: 'user_data'.
        body (BodyCreateFileV1FilesPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[FileResp, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            purpose=purpose,
        )
    ).parsed

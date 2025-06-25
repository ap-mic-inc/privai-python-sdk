from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file_resp import FileResp
from ...models.generate_qa_req import GenerateQaReq
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: GenerateQaReq,
    fileset_id: UUID,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_fileset_id = str(fileset_id)
    params["fileset_id"] = json_fileset_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/qa/generate",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[FileResp, HTTPValidationError]]:
    if response.status_code == 201:
        response_201 = FileResp.from_dict(response.json())

        return response_201
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
    body: GenerateQaReq,
    fileset_id: UUID,
) -> Response[Union[FileResp, HTTPValidationError]]:
    """Generate Qa

     Generate QA pairs from fileset

    Args:
        fileset_id (UUID):
        body (GenerateQaReq):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[FileResp, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        body=body,
        fileset_id=fileset_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: GenerateQaReq,
    fileset_id: UUID,
) -> Optional[Union[FileResp, HTTPValidationError]]:
    """Generate Qa

     Generate QA pairs from fileset

    Args:
        fileset_id (UUID):
        body (GenerateQaReq):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[FileResp, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        body=body,
        fileset_id=fileset_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: GenerateQaReq,
    fileset_id: UUID,
) -> Response[Union[FileResp, HTTPValidationError]]:
    """Generate Qa

     Generate QA pairs from fileset

    Args:
        fileset_id (UUID):
        body (GenerateQaReq):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[FileResp, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        body=body,
        fileset_id=fileset_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: GenerateQaReq,
    fileset_id: UUID,
) -> Optional[Union[FileResp, HTTPValidationError]]:
    """Generate Qa

     Generate QA pairs from fileset

    Args:
        fileset_id (UUID):
        body (GenerateQaReq):

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
            fileset_id=fileset_id,
        )
    ).parsed

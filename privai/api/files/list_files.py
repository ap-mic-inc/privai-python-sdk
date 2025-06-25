from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.list_files_result import ListFilesResult
from ...models.order import Order
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    fileset_id: Union[None, UUID, Unset] = UNSET,
    limit: Union[Unset, int] = 10000,
    order: Union[Unset, Order] = UNSET,
    after: Union[None, UUID, Unset] = UNSET,
    before: Union[None, UUID, Unset] = UNSET,
    purpose: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_fileset_id: Union[None, Unset, str]
    if isinstance(fileset_id, Unset):
        json_fileset_id = UNSET
    elif isinstance(fileset_id, UUID):
        json_fileset_id = str(fileset_id)
    else:
        json_fileset_id = fileset_id
    params["fileset_id"] = json_fileset_id

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

    json_purpose: Union[None, Unset, str]
    if isinstance(purpose, Unset):
        json_purpose = UNSET
    else:
        json_purpose = purpose
    params["purpose"] = json_purpose

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/files",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, ListFilesResult]]:
    if response.status_code == 200:
        response_200 = ListFilesResult.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, ListFilesResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    fileset_id: Union[None, UUID, Unset] = UNSET,
    limit: Union[Unset, int] = 10000,
    order: Union[Unset, Order] = UNSET,
    after: Union[None, UUID, Unset] = UNSET,
    before: Union[None, UUID, Unset] = UNSET,
    purpose: Union[None, Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ListFilesResult]]:
    r"""List Files

     Returns a list of files.

    Args:
        fileset_id (str, optional): Only return files which is used by the fileset_id. Defaults to None.
        limit (int, optional): A limit on the number of objects to be returned.
                                 Limit can range between 1 and 10,000, and the default is 10,000.
                                 Defaults to 10000.
        order (str, optional): Sort order by the `created_at` timestamp of the objects.
                                 `asc` for ascending order and `desc` for descending order.
                                 Defaults to \"desc\".
        after (str, optional): A cursor for use in pagination. `after` is an object ID that
                                defines your place in the list. For instance, if you make a list
                                request and receive 100 objects, ending with obj_foo, your
                                subsequent call can include after=obj_foo in order to fetch the
                                next page of the list. Defaults to None.
        before (str, optional): A cursor for use in pagination. `before` is an object ID that
                                 defines your place in the list. For instance, if you make a list
                                 request and receive 100 objects, start with obj_foo, your
                                 subsequent call can include before=obj_foo in order to fetch the
                                 next page of the list. Defaults to None.
        purpose (str, optional): The intended purpose of the uploaded file.

    Returns:
         ListFilesResult : A list of [File] objects containing the data and a boolean indicating if
    there are more files.
                           The result includes a `data` field containing a list of File objects,
                           and a `has_more` field indicating whether there are more files available to
    be fetched.

    Args:
        fileset_id (Union[None, UUID, Unset]):
        limit (Union[Unset, int]):  Default: 10000.
        order (Union[Unset, Order]): Order Enum for sorting.
        after (Union[None, UUID, Unset]):
        before (Union[None, UUID, Unset]):
        purpose (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ListFilesResult]]
    """

    kwargs = _get_kwargs(
        fileset_id=fileset_id,
        limit=limit,
        order=order,
        after=after,
        before=before,
        purpose=purpose,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    fileset_id: Union[None, UUID, Unset] = UNSET,
    limit: Union[Unset, int] = 10000,
    order: Union[Unset, Order] = UNSET,
    after: Union[None, UUID, Unset] = UNSET,
    before: Union[None, UUID, Unset] = UNSET,
    purpose: Union[None, Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ListFilesResult]]:
    r"""List Files

     Returns a list of files.

    Args:
        fileset_id (str, optional): Only return files which is used by the fileset_id. Defaults to None.
        limit (int, optional): A limit on the number of objects to be returned.
                                 Limit can range between 1 and 10,000, and the default is 10,000.
                                 Defaults to 10000.
        order (str, optional): Sort order by the `created_at` timestamp of the objects.
                                 `asc` for ascending order and `desc` for descending order.
                                 Defaults to \"desc\".
        after (str, optional): A cursor for use in pagination. `after` is an object ID that
                                defines your place in the list. For instance, if you make a list
                                request and receive 100 objects, ending with obj_foo, your
                                subsequent call can include after=obj_foo in order to fetch the
                                next page of the list. Defaults to None.
        before (str, optional): A cursor for use in pagination. `before` is an object ID that
                                 defines your place in the list. For instance, if you make a list
                                 request and receive 100 objects, start with obj_foo, your
                                 subsequent call can include before=obj_foo in order to fetch the
                                 next page of the list. Defaults to None.
        purpose (str, optional): The intended purpose of the uploaded file.

    Returns:
         ListFilesResult : A list of [File] objects containing the data and a boolean indicating if
    there are more files.
                           The result includes a `data` field containing a list of File objects,
                           and a `has_more` field indicating whether there are more files available to
    be fetched.

    Args:
        fileset_id (Union[None, UUID, Unset]):
        limit (Union[Unset, int]):  Default: 10000.
        order (Union[Unset, Order]): Order Enum for sorting.
        after (Union[None, UUID, Unset]):
        before (Union[None, UUID, Unset]):
        purpose (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ListFilesResult]
    """

    return sync_detailed(
        client=client,
        fileset_id=fileset_id,
        limit=limit,
        order=order,
        after=after,
        before=before,
        purpose=purpose,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    fileset_id: Union[None, UUID, Unset] = UNSET,
    limit: Union[Unset, int] = 10000,
    order: Union[Unset, Order] = UNSET,
    after: Union[None, UUID, Unset] = UNSET,
    before: Union[None, UUID, Unset] = UNSET,
    purpose: Union[None, Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ListFilesResult]]:
    r"""List Files

     Returns a list of files.

    Args:
        fileset_id (str, optional): Only return files which is used by the fileset_id. Defaults to None.
        limit (int, optional): A limit on the number of objects to be returned.
                                 Limit can range between 1 and 10,000, and the default is 10,000.
                                 Defaults to 10000.
        order (str, optional): Sort order by the `created_at` timestamp of the objects.
                                 `asc` for ascending order and `desc` for descending order.
                                 Defaults to \"desc\".
        after (str, optional): A cursor for use in pagination. `after` is an object ID that
                                defines your place in the list. For instance, if you make a list
                                request and receive 100 objects, ending with obj_foo, your
                                subsequent call can include after=obj_foo in order to fetch the
                                next page of the list. Defaults to None.
        before (str, optional): A cursor for use in pagination. `before` is an object ID that
                                 defines your place in the list. For instance, if you make a list
                                 request and receive 100 objects, start with obj_foo, your
                                 subsequent call can include before=obj_foo in order to fetch the
                                 next page of the list. Defaults to None.
        purpose (str, optional): The intended purpose of the uploaded file.

    Returns:
         ListFilesResult : A list of [File] objects containing the data and a boolean indicating if
    there are more files.
                           The result includes a `data` field containing a list of File objects,
                           and a `has_more` field indicating whether there are more files available to
    be fetched.

    Args:
        fileset_id (Union[None, UUID, Unset]):
        limit (Union[Unset, int]):  Default: 10000.
        order (Union[Unset, Order]): Order Enum for sorting.
        after (Union[None, UUID, Unset]):
        before (Union[None, UUID, Unset]):
        purpose (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ListFilesResult]]
    """

    kwargs = _get_kwargs(
        fileset_id=fileset_id,
        limit=limit,
        order=order,
        after=after,
        before=before,
        purpose=purpose,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    fileset_id: Union[None, UUID, Unset] = UNSET,
    limit: Union[Unset, int] = 10000,
    order: Union[Unset, Order] = UNSET,
    after: Union[None, UUID, Unset] = UNSET,
    before: Union[None, UUID, Unset] = UNSET,
    purpose: Union[None, Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ListFilesResult]]:
    r"""List Files

     Returns a list of files.

    Args:
        fileset_id (str, optional): Only return files which is used by the fileset_id. Defaults to None.
        limit (int, optional): A limit on the number of objects to be returned.
                                 Limit can range between 1 and 10,000, and the default is 10,000.
                                 Defaults to 10000.
        order (str, optional): Sort order by the `created_at` timestamp of the objects.
                                 `asc` for ascending order and `desc` for descending order.
                                 Defaults to \"desc\".
        after (str, optional): A cursor for use in pagination. `after` is an object ID that
                                defines your place in the list. For instance, if you make a list
                                request and receive 100 objects, ending with obj_foo, your
                                subsequent call can include after=obj_foo in order to fetch the
                                next page of the list. Defaults to None.
        before (str, optional): A cursor for use in pagination. `before` is an object ID that
                                 defines your place in the list. For instance, if you make a list
                                 request and receive 100 objects, start with obj_foo, your
                                 subsequent call can include before=obj_foo in order to fetch the
                                 next page of the list. Defaults to None.
        purpose (str, optional): The intended purpose of the uploaded file.

    Returns:
         ListFilesResult : A list of [File] objects containing the data and a boolean indicating if
    there are more files.
                           The result includes a `data` field containing a list of File objects,
                           and a `has_more` field indicating whether there are more files available to
    be fetched.

    Args:
        fileset_id (Union[None, UUID, Unset]):
        limit (Union[Unset, int]):  Default: 10000.
        order (Union[Unset, Order]): Order Enum for sorting.
        after (Union[None, UUID, Unset]):
        before (Union[None, UUID, Unset]):
        purpose (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ListFilesResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            fileset_id=fileset_id,
            limit=limit,
            order=order,
            after=after,
            before=before,
            purpose=purpose,
        )
    ).parsed

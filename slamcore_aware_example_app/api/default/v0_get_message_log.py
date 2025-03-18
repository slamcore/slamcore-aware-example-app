from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_exception_model import HTTPExceptionModel
from ...models.http_validation_error import HTTPValidationError
from ...models.log_buffer import LogBuffer
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    since_timestamp: Unset | float = 0.0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["since_timestamp"] = since_timestamp

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/message_log",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPExceptionModel | HTTPValidationError | LogBuffer | None:
    if response.status_code == 200:
        response_200 = LogBuffer.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = HTTPExceptionModel.from_dict(response.json())

        return response_401
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPExceptionModel | HTTPValidationError | LogBuffer]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    since_timestamp: Unset | float = 0.0,
) -> Response[HTTPExceptionModel | HTTPValidationError | LogBuffer]:
    """Get Message Log

     Get Slamcore WebUI log messages.

    Args:
        since_timestamp: The timestamp to filter log messages - in UNIX time.

    Returns:
        LogBuffer: The log messages since the specified timestamp.

    Args:
        since_timestamp (Union[Unset, float]):  Default: 0.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPExceptionModel, HTTPValidationError, LogBuffer]]
    """

    kwargs = _get_kwargs(
        since_timestamp=since_timestamp,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    since_timestamp: Unset | float = 0.0,
) -> HTTPExceptionModel | HTTPValidationError | LogBuffer | None:
    """Get Message Log

     Get Slamcore WebUI log messages.

    Args:
        since_timestamp: The timestamp to filter log messages - in UNIX time.

    Returns:
        LogBuffer: The log messages since the specified timestamp.

    Args:
        since_timestamp (Union[Unset, float]):  Default: 0.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPExceptionModel, HTTPValidationError, LogBuffer]
    """

    return sync_detailed(
        client=client,
        since_timestamp=since_timestamp,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    since_timestamp: Unset | float = 0.0,
) -> Response[HTTPExceptionModel | HTTPValidationError | LogBuffer]:
    """Get Message Log

     Get Slamcore WebUI log messages.

    Args:
        since_timestamp: The timestamp to filter log messages - in UNIX time.

    Returns:
        LogBuffer: The log messages since the specified timestamp.

    Args:
        since_timestamp (Union[Unset, float]):  Default: 0.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPExceptionModel, HTTPValidationError, LogBuffer]]
    """

    kwargs = _get_kwargs(
        since_timestamp=since_timestamp,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    since_timestamp: Unset | float = 0.0,
) -> HTTPExceptionModel | HTTPValidationError | LogBuffer | None:
    """Get Message Log

     Get Slamcore WebUI log messages.

    Args:
        since_timestamp: The timestamp to filter log messages - in UNIX time.

    Returns:
        LogBuffer: The log messages since the specified timestamp.

    Args:
        since_timestamp (Union[Unset, float]):  Default: 0.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPExceptionModel, HTTPValidationError, LogBuffer]
    """

    return (
        await asyncio_detailed(
            client=client,
            since_timestamp=since_timestamp,
        )
    ).parsed

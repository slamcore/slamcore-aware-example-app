from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_exception_model import HTTPExceptionModel
from ...models.system_info_wrapper import SystemInfoWrapper
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v0/system/info",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPExceptionModel | SystemInfoWrapper | None:
    if response.status_code == 200:
        response_200 = SystemInfoWrapper.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = HTTPExceptionModel.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPExceptionModel | SystemInfoWrapper]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[HTTPExceptionModel | SystemInfoWrapper]:
    """Get System Info

     Get system information about the Slamcore WebUI and underlying SLAM process.

    Returns:
        The system information model.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPExceptionModel | SystemInfoWrapper]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> HTTPExceptionModel | SystemInfoWrapper | None:
    """Get System Info

     Get system information about the Slamcore WebUI and underlying SLAM process.

    Returns:
        The system information model.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPExceptionModel | SystemInfoWrapper
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[HTTPExceptionModel | SystemInfoWrapper]:
    """Get System Info

     Get system information about the Slamcore WebUI and underlying SLAM process.

    Returns:
        The system information model.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPExceptionModel | SystemInfoWrapper]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> HTTPExceptionModel | SystemInfoWrapper | None:
    """Get System Info

     Get system information about the Slamcore WebUI and underlying SLAM process.

    Returns:
        The system information model.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPExceptionModel | SystemInfoWrapper
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed

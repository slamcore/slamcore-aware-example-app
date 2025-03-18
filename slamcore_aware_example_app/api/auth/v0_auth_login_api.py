from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_exception_model import HTTPExceptionModel
from ...models.token import Token
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/login/api_key",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPExceptionModel | Token | None:
    if response.status_code == 200:
        response_200 = Token.from_dict(response.json())

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
) -> Response[HTTPExceptionModel | Token]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[HTTPExceptionModel | Token]:
    """Login Api

     Authenticate using an API key.

    Returns:
        The access token to use for subsequent requests.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPExceptionModel, Token]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> HTTPExceptionModel | Token | None:
    """Login Api

     Authenticate using an API key.

    Returns:
        The access token to use for subsequent requests.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPExceptionModel, Token]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[HTTPExceptionModel | Token]:
    """Login Api

     Authenticate using an API key.

    Returns:
        The access token to use for subsequent requests.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPExceptionModel, Token]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> HTTPExceptionModel | Token | None:
    """Login Api

     Authenticate using an API key.

    Returns:
        The access token to use for subsequent requests.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPExceptionModel, Token]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed

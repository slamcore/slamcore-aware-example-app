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
        "method": "get",
        "url": "/v0/ws_token",
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
    """Get Ws Token

     Request a websocket token.

    Use this endpoint to request a token to authenticate specifically with the websocket.

    To do so, first get an access token by logging in, e.g., via the API and the
    `/login/api_key` endpoint. Then use the said access token to request a websocket token from
    this endpoint.

    Finally, when opening a new websocket connection, append the websocket token
    to the URL as follows:

    ```
    websocat ws://$AWARE_DEVICE_HOST/v0/slam/ws/$WS_TOKEN
    ```

    Returns:
        The websocket token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPExceptionModel | Token]
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
    """Get Ws Token

     Request a websocket token.

    Use this endpoint to request a token to authenticate specifically with the websocket.

    To do so, first get an access token by logging in, e.g., via the API and the
    `/login/api_key` endpoint. Then use the said access token to request a websocket token from
    this endpoint.

    Finally, when opening a new websocket connection, append the websocket token
    to the URL as follows:

    ```
    websocat ws://$AWARE_DEVICE_HOST/v0/slam/ws/$WS_TOKEN
    ```

    Returns:
        The websocket token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPExceptionModel | Token
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[HTTPExceptionModel | Token]:
    """Get Ws Token

     Request a websocket token.

    Use this endpoint to request a token to authenticate specifically with the websocket.

    To do so, first get an access token by logging in, e.g., via the API and the
    `/login/api_key` endpoint. Then use the said access token to request a websocket token from
    this endpoint.

    Finally, when opening a new websocket connection, append the websocket token
    to the URL as follows:

    ```
    websocat ws://$AWARE_DEVICE_HOST/v0/slam/ws/$WS_TOKEN
    ```

    Returns:
        The websocket token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPExceptionModel | Token]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> HTTPExceptionModel | Token | None:
    """Get Ws Token

     Request a websocket token.

    Use this endpoint to request a token to authenticate specifically with the websocket.

    To do so, first get an access token by logging in, e.g., via the API and the
    `/login/api_key` endpoint. Then use the said access token to request a websocket token from
    this endpoint.

    Finally, when opening a new websocket connection, append the websocket token
    to the URL as follows:

    ```
    websocat ws://$AWARE_DEVICE_HOST/v0/slam/ws/$WS_TOKEN
    ```

    Returns:
        The websocket token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPExceptionModel | Token
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed

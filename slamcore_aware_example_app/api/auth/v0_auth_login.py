from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_v0_auth_login import BodyV0AuthLogin
from ...models.http_exception_model import HTTPExceptionModel
from ...models.http_validation_error import HTTPValidationError
from ...models.token import Token
from ...types import Response


def _get_kwargs(
    *,
    body: BodyV0AuthLogin,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/login",
    }

    _body = body.to_dict()

    _kwargs["data"] = _body
    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPExceptionModel | HTTPValidationError | Token | None:
    if response.status_code == 200:
        response_200 = Token.from_dict(response.json())

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
) -> Response[HTTPExceptionModel | HTTPValidationError | Token]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BodyV0AuthLogin,
) -> Response[HTTPExceptionModel | HTTPValidationError | Token]:
    """Login

     Authenticate using username and password.

    Returns:
        The access token to use for subsequent requests.

    Args:
        body (BodyV0AuthLogin):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPExceptionModel, HTTPValidationError, Token]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: BodyV0AuthLogin,
) -> HTTPExceptionModel | HTTPValidationError | Token | None:
    """Login

     Authenticate using username and password.

    Returns:
        The access token to use for subsequent requests.

    Args:
        body (BodyV0AuthLogin):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPExceptionModel, HTTPValidationError, Token]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BodyV0AuthLogin,
) -> Response[HTTPExceptionModel | HTTPValidationError | Token]:
    """Login

     Authenticate using username and password.

    Returns:
        The access token to use for subsequent requests.

    Args:
        body (BodyV0AuthLogin):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPExceptionModel, HTTPValidationError, Token]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BodyV0AuthLogin,
) -> HTTPExceptionModel | HTTPValidationError | Token | None:
    """Login

     Authenticate using username and password.

    Returns:
        The access token to use for subsequent requests.

    Args:
        body (BodyV0AuthLogin):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPExceptionModel, HTTPValidationError, Token]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_key_creation_response import APIKeyCreationResponse
from ...models.http_exception_model import HTTPExceptionModel
from ...models.http_validation_error import HTTPValidationError
from ...models.new_api_key_props import NewAPIKeyProps
from ...types import Response


def _get_kwargs(
    *,
    body: NewAPIKeyProps,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v0/api_key",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIKeyCreationResponse | HTTPExceptionModel | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = APIKeyCreationResponse.from_dict(response.json())

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
) -> Response[APIKeyCreationResponse | HTTPExceptionModel | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: NewAPIKeyProps,
) -> Response[APIKeyCreationResponse | HTTPExceptionModel | HTTPValidationError]:
    """Create Api Key

     Create a new API key for the current user.

    Returns:
        The created API key in plaintext.

    Args:
        body (NewAPIKeyProps):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[APIKeyCreationResponse, HTTPExceptionModel, HTTPValidationError]]
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
    client: AuthenticatedClient,
    body: NewAPIKeyProps,
) -> APIKeyCreationResponse | HTTPExceptionModel | HTTPValidationError | None:
    """Create Api Key

     Create a new API key for the current user.

    Returns:
        The created API key in plaintext.

    Args:
        body (NewAPIKeyProps):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[APIKeyCreationResponse, HTTPExceptionModel, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: NewAPIKeyProps,
) -> Response[APIKeyCreationResponse | HTTPExceptionModel | HTTPValidationError]:
    """Create Api Key

     Create a new API key for the current user.

    Returns:
        The created API key in plaintext.

    Args:
        body (NewAPIKeyProps):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[APIKeyCreationResponse, HTTPExceptionModel, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: NewAPIKeyProps,
) -> APIKeyCreationResponse | HTTPExceptionModel | HTTPValidationError | None:
    """Create Api Key

     Create a new API key for the current user.

    Returns:
        The created API key in plaintext.

    Args:
        body (NewAPIKeyProps):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[APIKeyCreationResponse, HTTPExceptionModel, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

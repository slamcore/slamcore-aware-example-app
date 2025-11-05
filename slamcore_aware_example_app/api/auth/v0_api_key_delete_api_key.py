from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_exception_model import HTTPExceptionModel
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response


def _get_kwargs(
    *,
    api_key_last_3_chars: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["api_key_last_3_chars"] = api_key_last_3_chars

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v0/api_key",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPExceptionModel | HTTPValidationError | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
) -> Response[Any | HTTPExceptionModel | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    api_key_last_3_chars: str,
) -> Response[Any | HTTPExceptionModel | HTTPValidationError]:
    """Delete Api Key

     Delete matching API key(s) for the current user.

    Raises:
        HTTPException: If the API key is not found.

    Args:
        api_key_last_3_chars (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPExceptionModel | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        api_key_last_3_chars=api_key_last_3_chars,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    api_key_last_3_chars: str,
) -> Any | HTTPExceptionModel | HTTPValidationError | None:
    """Delete Api Key

     Delete matching API key(s) for the current user.

    Raises:
        HTTPException: If the API key is not found.

    Args:
        api_key_last_3_chars (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPExceptionModel | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        api_key_last_3_chars=api_key_last_3_chars,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    api_key_last_3_chars: str,
) -> Response[Any | HTTPExceptionModel | HTTPValidationError]:
    """Delete Api Key

     Delete matching API key(s) for the current user.

    Raises:
        HTTPException: If the API key is not found.

    Args:
        api_key_last_3_chars (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPExceptionModel | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        api_key_last_3_chars=api_key_last_3_chars,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    api_key_last_3_chars: str,
) -> Any | HTTPExceptionModel | HTTPValidationError | None:
    """Delete Api Key

     Delete matching API key(s) for the current user.

    Raises:
        HTTPException: If the API key is not found.

    Args:
        api_key_last_3_chars (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPExceptionModel | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            api_key_last_3_chars=api_key_last_3_chars,
        )
    ).parsed

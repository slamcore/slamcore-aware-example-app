# ruff: noqa: T201, INP001
"""Slamcore Aware Demo application.

This script constitutes a demo for how to interact with the Slamcore Aware server, its REST API
and its Websocket endpoint for receiving real-time Positioning events.

The demo uses a sample python client library, created using `openapi-python-client`, to
interact with the Slamcore Aware server from python.

Prerequisites:
--------------

This demo assumes that:

1. You have access to a Slamcore Aware device and you know its IP address and/or hostname.
2. The Slamcore Aware device is already running Positioning (default behavior) and that the
   pedestrian detection feature is enabled.
3. You have generated an API key for the Slamcore Aware device using the Slamcore Aware UI
   (although the REST API does allow for creating API keys programmatically, using username and
   password of the user).
"""

__copyright__ = """Slamcore Confidential.

Slamcore Limited
All Rights Reserved.
(C) Copyright 2025

NOTICE:

All information contained herein is, and remains the property of Slamcore
Limited and its suppliers, if any. The intellectual and technical concepts
contained herein are proprietary to Slamcore Limited and its suppliers and
may be covered by patents in process, and are protected by trade secret or
copyright law. Dissemination of this information or reproduction of this
material is strictly forbidden unless prior written permission is obtained
from Slamcore Limited.
"""


import argparse
import json
import pprint
import sys
import time
import traceback
from collections.abc import Callable
from functools import partial
from itertools import islice
from urllib.parse import ParseResult, urlparse

import httpx
from slamcore_aware_example_app.api.auth import v0_auth_get_ws_token, v0_auth_login_api
from slamcore_aware_example_app.api.default import v0_get_message_log
from slamcore_aware_example_app.api.slam import v0_slam_get
from slamcore_aware_example_app.api.system import v0_system_get_system_info
from slamcore_aware_example_app.client import AuthenticatedClient
from slamcore_aware_example_app.models.http_exception_model import HTTPExceptionModel
from slamcore_aware_example_app.models.token import Token
from websockets.sync.client import connect


# general-purpose helper  functions -----------------------------------------------------------
def parse_and_delegate_to_main() -> int:
    """Parse command-line arguments and run the main function.

    Returns:
        The exit code of the process.

    """
    args = parse_args()
    return catch_exceptions(verbose=args.verbose > 0, fn=lambda: main(args=args))()


def catch_exceptions(*, verbose: bool, fn: Callable[[], int]) -> Callable[[], int]:
    """Catch exceptions and print them to the console.

    Args:
        verbose: Whether to print the full traceback or just a summary in case of an exception.
        fn: The function to execute.

    Returns:
        The function wrapped in an exception handler.

    """

    def wrapper() -> int:
        try:
            return fn()
        except Exception:  # noqa: BLE001
            if verbose:
                announce(
                    header="Error during execution",
                    msg=traceback.format_exc(),
                )
            else:
                traceback_lines = traceback.format_exc().split("\n")
                num_traceback_lines = 5
                if len(traceback.format_exc().split("\n")) < num_traceback_lines:
                    announce(
                        header="Error during execution",
                        msg=traceback.format_exc(),
                    )
                else:
                    msg = (
                        "\n".join(traceback_lines[-num_traceback_lines:])
                        + "\n\n"
                        + "Run with -v/--verbose for more details."
                    )
                    announce(
                        header="Error during execution",
                        msg=msg,
                    )

            return 1

    return wrapper


def announce(msg: str, header: str | None = None) -> None:
    """Print a message to the console.

    Args:
        header: The header to print.
        msg: The message

    """
    if header is not None:
        sep = "=" * len(header)
        fullmsg = f"\n{header}\n{sep}\n\n{msg}\n"
    else:
        sep_len = min(max(len(li) for li in msg.split("\n")), 120)
        sep = "=" * sep_len
        fullmsg = f"\n{sep}\n{msg}\n{sep}\n"
    print(fullmsg)


def confirm_prerequisites_or_exit() -> None:
    """Confirm with the user the prerequisites for running the demo."""
    assert __doc__
    header = __doc__.split("\n")[0]
    prerequisites = __doc__[__doc__.find("Prerequisites:") :]
    announce(header=header, msg=prerequisites)
    while True:
        response = input("Confirm [Y/n]:")
        # while the response is not y/n/ENTER keep asking
        if response.lower() in {"y", ""}:
            break
        if response.lower() == "n":
            sys.exit(0)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments.

    Returns:
        The namespace with the parsed arguments.

    """
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--aware-url",
        help="The base URL of the Slamcore Aware server.",
        required=True,
    )
    parser.add_argument(
        "--no-confirm",
        help="Skip the confirmation of the demo prerequisites",
        action="store_true",
    )
    parser.add_argument(
        "--api-key",
        help="The API key to use for authenticating with the Slamcore Aware server",
        required=True,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        help="Increase output verbosity",
        action="count",
        default=0,
    )

    return parser.parse_args()


# demo-specific functions ---------------------------------------------------------------------
def login_via_api_key(
    aware_url: str,
    api_key: str,
) -> AuthenticatedClient:
    """Authenticate with the Slamcore Aware server using the provided user API key.

    Raises:
        TypeError: If the authentication fails.
        RuntimeError: If the connection to the server fails.

    Returns:
        The authenticated client object to use for making further, this time authenticated, API
        requests.

    """
    print(f"Authenticating with the Slamcore Aware server -> {aware_url!r}...")
    aware_url_parsed: ParseResult = urlparse(aware_url)

    # Passing a token is not necessary in the API. In this case we're doing it since
    # openapi-python-client requires interacting with `v0/auth/login_api` via an
    # `AuthenticatedClient` and not a `Client`.
    APIKeyLoginClient = partial(AuthenticatedClient, token="dummy")  # noqa: S106, N806

    client = APIKeyLoginClient(
        base_url=aware_url_parsed.geturl(),
        raise_on_unexpected_status=False,
        headers={"x-api-key": api_key},
    )
    with client as client:
        try:
            token = v0_auth_login_api.sync(
                client=client,
            )
        except httpx.ConnectError as e:
            s = (
                "Failed to connect to the Slamcore Aware server. "
                f"Please verify the IP / name to connect to: {aware_url!r}."
            )
            raise RuntimeError(s) from e

        if not isinstance(token, Token):
            s = f"Failed to authenticate with the Slamcore Aware server -> {aware_url!r}"
            raise TypeError(s)

        print("Successfully authenticated with the Slamcore Aware server.")
        return AuthenticatedClient(
            base_url=aware_url_parsed.geturl(),
            raise_on_unexpected_status=True,
            token=token.access_token,
        )


def interact_w_websocket(client: AuthenticatedClient) -> None:
    """Interact with the Slamcore Aware server via a Websocket connection.

    - Send requests to start/stop Positioning-related streams
    - Receive real-time Positioning events.

    Raises:
        TypeError: If the websocket token cannot be retrieved

    """
    # get WS token ----------------------------------------------------------------------------
    # a new token, separate to the REST API, is required to establish a connection to the
    # Websocket endpoint.
    token_data = v0_auth_get_ws_token.sync(client=client)

    if isinstance(token_data, HTTPExceptionModel) or token_data is None:
        token_data_str = token_data if token_data is not None else ""
        s = f"Failed to get the Websocket token{token_data_str}"
        raise TypeError(s)
    ws_token = token_data.access_token

    # connect to the websocket ----------------------------------------------------------------
    aware_url = client.get_httpx_client().base_url.copy_with(scheme="ws")
    with connect(str(aware_url.join(f"v0/slam/ws/{ws_token}"))) as websocket:
        # request streaming of messages
        print("Requesting streaming of messages: FullPose, SLAMStatus, Panoptic...")
        websocket.send(
            json.dumps(
                {
                    "start": [
                        "FullPose",
                        "SLAMStatus",
                        "Panoptic",
                    ],
                },
            ),
        )

        print("Receiving real-time Positioning messages via websocket...")

        announce("Receiving a single message via websocket...")
        msg = websocket.recv()
        print(pprint.pformat(json.loads(msg)))

        num_msgs = 10
        announce(f"Receiving: first {num_msgs} messages...")
        for msg in islice(websocket, num_msgs):
            print(pprint.pformat(msg))

        # stop the FullPose stream
        announce("Stopping the FullPose stream...")
        websocket.send(json.dumps({"stop": ["FullPose"]}))

        num_msgs = 50
        announce(f"Receiving: next {num_msgs} messages...")
        for msg in islice(websocket, num_msgs):
            print(pprint.pformat(msg))
        announce("Disconnecting from the websocket...")
        time.sleep(1)


# main ----------------------------------------------------------------------------------------
def main(args: argparse.Namespace) -> int:
    """Run demo.

    Returns:
        The exit code of the process.

    """
    args = parse_args()
    aware_url = args.aware_url

    # confirm ---------------------------------------------------------------------------------
    if not args.no_confirm:
        confirm_prerequisites_or_exit()
        print("Proceeding with the demo...")

    # login -----------------------------------------------------------------------------------
    client = login_via_api_key(aware_url, args.api_key)

    # get system information ------------------------------------------------------------------
    print("Getting system information...")
    system_info_ret = v0_system_get_system_info.sync(client=client)
    if isinstance(system_info_ret, HTTPExceptionModel) or system_info_ret is None:
        s = system_info_ret if system_info_ret is not None else ""
        print(f"Failed to get system information{s}")
    else:
        announce(
            header="System Information",
            msg=str(
                pprint.pformat(system_info_ret.to_dict()),
            ),
        )

    # get device status -----------------------------------------------------------------------
    print("Getting the device status...")
    device_status_ret = v0_slam_get.sync(client=client)
    if isinstance(device_status_ret, HTTPExceptionModel) or device_status_ret is None:
        s = device_status_ret if device_status_ret is not None else ""
        print(f"Failed to get the device status{s}")

    else:
        announce(
            header="Device Status",
            msg=str(
                pprint.pformat(device_status_ret.to_dict()),
            ),
        )

    # websocket interaction -------------------------------------------------------------------
    interact_w_websocket(client=client)

    # print message log -----------------------------------------------------------------------
    print("Getting the full message log...")
    message_log_ret = v0_get_message_log.sync(client=client)
    if isinstance(message_log_ret, HTTPExceptionModel) or message_log_ret is None:
        s = message_log_ret if message_log_ret is not None else ""
        print(f"Failed to get the full message log{s}")
    else:
        msgs = message_log_ret.to_dict()["log"]
        announce(
            header="Message Log",
            msg=str(
                # last 10 messages to avoid crowding the console
                pprint.pformat(msgs[:10]),
            ),
        )

    return 0


if __name__ == "__main__":
    sys.exit(parse_and_delegate_to_main())

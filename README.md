# Slamcore Aware - REST API Example App

> A client library for accessing Slamcore Aware - v0

The current repository contains an example application that demonstrates how to
use the Slamcore Aware REST API to interact with the Slamcore Aware platform.
Said interaction is done via python bindings, generated using
[openapi-python-client](https://github.com/openapi-generators/openapi-python-client)
and the OpenAPI specification that the Slamcore Aware server advertises (see the
`v0/openapi.json` server endpoint).

## Installation

To install the `slamcore-aware-example-app`, you can either clone this repo and
point `pip install` to your local clone, or you can install it directly from
github:

```bash
# either clone and install:
git clone git@github.com:slamcore/slamcore-aware-example-app.git

# or install directly from github:
pip install git+https://github.com/slamcore/slamcore-aware-example-app.git
```

A third installation method would be to use `pipx` to avoid installing the
example app in your global/local python environment:

```bash
pipx run \
    --spec git+ssh://git@github.com/slamcore/slamcore-aware-example-app \
    slamcore-aware-demo --help
```

## Usage

The example app is a command-line interface that allows you to interact with a
live instance of the Slamcore Aware server. Following are the example outputs
when using the `--help` flag and when using the `--aware-url` and `--api-key`
flags to interact with a live instance of the Slamcore Aware server.

You can find more information about the Slamcore Aware REST API and how to
interact with it in the [Slamcore Aware
documentation](https://aware.docs.slamcore.com).

<details>
<summary>Using --help</summary>

```txt
$ pipx run --no-cache \
    --spec git+ssh://git@github.com/slamcore/slamcore-aware-example-app \
    slamcore-aware-demo --help

usage: slamcore-aware-demo [-h] --aware-url AWARE_URL [--no-confirm]
                           --api-key API_KEY [-v]

Slamcore Aware Demo application.

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
   (although the REST API does allow for creating API keys programmatically,
   using the username and password of the user).

options:
  -h, --help            show this help message and exit
  --aware-url AWARE_URL
                        The base URL of the Slamcore Aware server.
  --no-confirm          Skip the confirmation of the demo prerequisites
  --api-key API_KEY     The API key to use for authenticating with the
                        Slamcore Aware server.
  -v, --verbose         Increase output verbosity
```

</details>

<details>
<summary>Using --aware-url and --api-key</summary>

```bash
$ pipx run  \
    --spec git+ssh://git@github.com/slamcore/slamcore-aware-example-app \
    slamcore-aware-demo \
    --aware-url http://slamcore-aware-host --api-key <API_KEY>
```

```txt
Slamcore Aware Demo application.
================================

Prerequisites:
--------------

This demo assumes that:

1. You have access to a Slamcore Aware device and you know its IP address and/or hostname.
2. The Slamcore Aware device is already running Positioning (default behavior) and that the
   pedestrian detection feature is enabled.
3. You have generated an API key for the Slamcore Aware device using the Slamcore Aware UI
   (although the REST API does allow for creating API keys programmatically, using the user's
   username and password).


Confirm [Y/n]:
Proceeding with the demo...
Authenticating with the Slamcore Aware server -> 'http://localhost:8000'...
Successfully authenticated with the Slamcore Aware server.
Getting system information...

System Information
==================

{'system': {'hostname': 'v173',
            'info': {'cameras': [{'firmware_version': '5.12.15.50',
                                  'manufacturer': '...',
                                  'model': '...',
                                  'serial_number': '...'}],
                     'software_version': '25.2.18.dev45+gfd4ceddb.d20250319'}}}

Getting the device status...

Device Status
``{'health': {'camera': True, 'license': True},
 'sessions': [],
 'slam_state': None,
 'state': 'ready'}

Requesting streaming of messages: FullPose, SLAMStatus, BodyPanoptic...
Receiving real-time Positioning messages via websocket...

===========================================
Receiving a single message via websocket...
===========================================

'{"slam_status":{"tracking_status":"Ok","tracking_confidence":0.0,"events":[]}}'
```

</details>

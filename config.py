#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = "" or os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = "" or os.environ.get("MicrosoftAppPassword", "")

# Copyright 2023 Deepgram SDK contributors. All Rights Reserved.
# Use of this source code is governed by a MIT license that can be found in the LICENSE file.
# SPDX-License-Identifier: MIT

from .client import OnPremClient
from .async_client import AsyncOnPremClient
from ....options import DeepgramClientOptions


def onprem(config: DeepgramClientOptions):
    return OnPremClient(config)


def asynconprem(config: DeepgramClientOptions):
    return AsyncOnPremClient(config)
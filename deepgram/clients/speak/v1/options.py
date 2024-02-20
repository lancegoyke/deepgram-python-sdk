# Copyright 2024 Deepgram SDK contributors. All Rights Reserved.
# Use of this source code is governed by a MIT license that can be found in the LICENSE file.
# SPDX-License-Identifier: MIT

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Union, List, TypedDict, Optional
import logging, verboselogs


@dataclass_json
@dataclass
class SpeakOptions:
    """
    Contains all the options for the SpeakOptions.

    Reference:
    https://developers.deepgram.com/reference/text-to-speech-preview-api
    """

    model: Optional[str] = None
    encoding: Optional[str] = None
    container: Optional[str] = None
    sample_rate: Optional[int] = None
    bit_rate: Optional[int] = None

    def __getitem__(self, key):
        _dict = self.to_dict()
        return _dict[key]

    def check(self):
        verboselogs.install()
        logger = logging.getLogger(__name__)
        logger.addHandler(logging.StreamHandler())
        prev = logger.level
        logger.setLevel(logging.ERROR)

        # no op at the moment

        logger.setLevel(prev)

        return True

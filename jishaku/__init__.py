# -*- coding: utf-8 -*-

"""
jishaku
~~~~~~~

A discord.py extension including useful tools for bot development and debugging.

:copyright: (c) 2024 Devon (scarletcafe) R
:license: MIT, see LICENSE for more details.

"""

from jishaku.cog import Jishaku, STANDARD_FEATURES, OPTIONAL_FEATURES, setup
from jishaku.features.baseclass import Feature
from jishaku.flags import Flags
from jishaku.meta import *  # noqa: F403

__all__ = (
    'Jishaku',
    'Feature',
    'Flags',
    'STANDARD_FEATURES',
    'OPTIONAL_FEATURES',
    'setup',
)

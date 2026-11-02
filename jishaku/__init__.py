"""
jishaku
~~~~~~~

A discord.py extension including useful tools for bot development and debugging.

:copyright: (c) 2024 Devon (scarletcafe) R
:license: MIT, see LICENSE for more details.

"""

from jishaku.cog import OPTIONAL_FEATURES, STANDARD_FEATURES, Jishaku, setup
from jishaku.features.baseclass import Feature
from jishaku.flags import Flags
from jishaku.meta import *

__all__ = (
    'OPTIONAL_FEATURES',
    'STANDARD_FEATURES',
    'Feature',
    'Flags',
    'Jishaku',
    'setup',
)

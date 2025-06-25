# -*- coding: utf-8 -*-

"""
jishaku
~~~~~~~

A discord.py extension including useful tools for bot development and debugging.

:copyright: (c) 2024 Devon (scarletcafe) R
:license: MIT, see LICENSE for more details.

"""

# pylint: disable=wildcard-import
from jishaku_mod.cog import *  # noqa: F401
from jishaku_mod.features.baseclass import Feature  # noqa: F401
from jishaku_mod.flags import Flags  # noqa: F401
from jishaku_mod.meta import *  # noqa: F401

__all__ = (
    'Jishaku',
    'Feature',
    'Flags',
    'setup'
)

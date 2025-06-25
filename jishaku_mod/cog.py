# -*- coding: utf-8 -*-

"""
jishaku.cog
~~~~~~~~~~~~

The Jishaku debugging and diagnostics cog implementation.

:copyright: (c) 2021 Devon (scarletcafe) R
:license: MIT, see LICENSE for more details.

"""

import inspect
import typing

from discord.ext import commands

from jishaku_mod.features.baseclass import Feature
from jishaku_mod.features.filesystem import FilesystemFeature
from jishaku_mod.features.guild import GuildFeature
from jishaku_mod.features.invocation import InvocationFeature
from jishaku_mod.features.management import ManagementFeature
from jishaku_mod.features.python import PythonFeature
from jishaku_mod.features.root_command import RootCommand
from jishaku_mod.features.shell import ShellFeature
from jishaku_mod.features.sql import SQLFeature
from jishaku_mod.features.voice import VoiceFeature

__all__ = (
    "Jishaku",
    "STANDARD_FEATURES",
    "OPTIONAL_FEATURES",
    "setup",
)

STANDARD_FEATURES = (VoiceFeature, GuildFeature, FilesystemFeature, InvocationFeature, ShellFeature, SQLFeature, PythonFeature, ManagementFeature, RootCommand)

OPTIONAL_FEATURES: typing.List[typing.Type[Feature]] = []

try:
    from jishaku_mod.features.youtube import YouTubeFeature
except ImportError:
    pass
else:
    OPTIONAL_FEATURES.insert(0, YouTubeFeature)


class Jishaku(*OPTIONAL_FEATURES, *STANDARD_FEATURES):  # type: ignore  # pylint: disable=too-few-public-methods
    """
    The frontend subclass that mixes in to form the final Jishaku cog.
    """


async def async_setup(bot: commands.Bot):
    """
    The async setup function defining the jishaku.cog and jishaku extensions.
    """

    await bot.add_cog(Jishaku(bot=bot))  # type: ignore


def setup(bot: commands.Bot):  # pylint: disable=inconsistent-return-statements
    """
    The setup function defining the jishaku.cog and jishaku extensions.
    """

    if inspect.iscoroutinefunction(bot.add_cog):
        return async_setup(bot)

    bot.add_cog(Jishaku(bot=bot))  # type: ignore[reportUnusedCoroutine]

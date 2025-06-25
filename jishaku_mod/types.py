# -*- coding: utf-8 -*-

"""
jishaku.types
~~~~~~~~~~~~~

Declarations for type checking

:copyright: (c) 2021 Devon (scarletcafe) R
:license: MIT, see LICENSE for more details.

"""

import typing

class Bot:...
class AutoShardedBot:...
class Cog:...

_Bot = typing.Union["Bot", "AutoShardedBot"]
# from discord.ext import commands
BotTT = typing.TypeVar("BotTT", bound=_Bot, covariant=True)
CogT = typing.TypeVar('CogT', bound='typing.Optional[Cog]')
class Context(typing.Generic[BotTT]):
    pass

BotT = _Bot
ContextT = typing.TypeVar('ContextT', Context[Bot], Context[AutoShardedBot])
ContextA = Context[BotT]

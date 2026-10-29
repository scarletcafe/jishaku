"""
jishaku.codeblocks
~~~~~~~~~~~~~~~~~~

Converters for detecting and obtaining codeblock content

:copyright: (c) 2021 Devon (scarletcafe) R
:license: MIT, see LICENSE for more details.

"""

import collections
import re
import typing

from discord.ext import commands

__all__ = ('Codeblock',)


class Codeblock(typing.NamedTuple):
    """
    Represents a parsed codeblock from codeblock_converter
    """

    language: str | None
    content: str

    @classmethod
    def convert(cls, ctx: commands.Context[typing.Any], argument: str) -> typing.Self:
        """
        A converter that strips codeblock markdown if it exists.

        Returns a namedtuple of (language, content).

        :attr:`Codeblock.language` is an empty string if no language was given with this codeblock.
        It is ``None`` if the input was not a complete codeblock.
        """

        # Remove direction-controlling characters sometimes inserted by Discord around codeblocks
        # https://github.com/scarletcafe/jishaku/issues/253#issuecomment-3831488396
        argument = re.sub('[\u2066-\u206D]', '', argument).strip()

        if not argument.startswith('`'):
            return cls(None, argument)

        # keep a small buffer of the last chars we've seen
        last: collections.deque[str] = collections.deque(maxlen=3)
        backticks = 0
        in_language = False
        in_code = False
        language: list[str] = []
        code: list[str] = []

        for char in argument:
            if char == '`' and not in_code and not in_language:
                backticks += 1  # to help keep track of closing backticks
            if last and last[-1] == '`' and char != '`' or in_code and ''.join(last) != '`' * backticks:
                in_code = True
                code.append(char)
            if char == '\n':  # \n delimits language and code
                in_language = False
                in_code = True
            # we're not seeing a newline yet but we also passed the opening ```
            elif ''.join(last) == '`' * 3 and char != '`':
                in_language = True
                language.append(char)
            elif in_language:  # we're in the language after the first non-backtick character
                if char != '\n':
                    language.append(char)

            last.append(char)

        if not code and not language:
            code[:] = last

        return cls(''.join(language), ''.join(code[len(language):-backticks]))

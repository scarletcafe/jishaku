# -*- coding: utf-8 -*-

"""
jishaku.repl
~~~~~~~~~~~~

Repl-related operations and tools for Jishaku.

:copyright: (c) 2021 Devon (scarletcafe) R
:license: MIT, see LICENSE for more details.

"""

from jishaku.repl.compilation import *  # noqa: F403
from jishaku.repl.disassembly import create_tree, disassemble, get_adaptive_spans  # type: ignore  # noqa: F401
from jishaku.repl.inspections import all_inspections  # type: ignore  # noqa: F401
from jishaku.repl.repl_builtins import get_var_dict_from_ctx  # type: ignore  # noqa: F401
from jishaku.repl.scope import *  # noqa: F403

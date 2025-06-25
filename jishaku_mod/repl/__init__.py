# -*- coding: utf-8 -*-

"""
jishaku.repl
~~~~~~~~~~~~

Repl-related operations and tools for Jishaku.

:copyright: (c) 2021 Devon (scarletcafe) R
:license: MIT, see LICENSE for more details.

"""

# pylint: disable=wildcard-import
from jishaku_mod.repl.compilation import *  # noqa: F401
from jishaku_mod.repl.disassembly import create_tree, disassemble, get_adaptive_spans  # type: ignore  # noqa: F401
from jishaku_mod.repl.inspections import all_inspections  # type: ignore  # noqa: F401
from jishaku_mod.repl.repl_builtins import get_var_dict_from_ctx  # type: ignore  # noqa: F401
from jishaku_mod.repl.scope import *  # noqa: F401

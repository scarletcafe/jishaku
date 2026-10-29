"""
jishaku converter test
~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2021 Devon (scarletcafe) R
:license: MIT, see LICENSE for more details.

"""

import inspect

from jishaku.codeblocks import Codeblock


def test_codeblock_converter():
    text = """
    ```py
    one
    ```
    """

    codeblock = Codeblock.convert_raw(inspect.cleandoc(text))

    assert isinstance(codeblock, Codeblock)
    assert codeblock.content.strip() == 'one'
    assert codeblock.language == 'py'

    text = """
    ```sql
    two
    ```
    """

    codeblock = Codeblock.convert_raw(inspect.cleandoc(text))

    assert isinstance(codeblock, Codeblock)
    assert codeblock.content.strip() == 'two'
    assert codeblock.language == 'sql'

    text = """
    ```txt
    three
    ```
    """

    codeblock = Codeblock.convert_raw(inspect.cleandoc(text))

    assert isinstance(codeblock, Codeblock)
    assert codeblock.content.strip() == 'three'
    assert codeblock.language == 'txt'

    text = """
    ```
    four
    ```
    """

    codeblock = Codeblock.convert_raw(inspect.cleandoc(text))

    assert isinstance(codeblock, Codeblock)
    assert codeblock.content.strip() == 'four'
    assert not codeblock.language

    text = "five"

    codeblock = Codeblock.convert_raw(inspect.cleandoc(text))

    assert isinstance(codeblock, Codeblock)
    assert codeblock.content.strip() == 'five'
    assert not codeblock.language

    text = """
    six
    ```
    """

    codeblock = Codeblock.convert_raw(inspect.cleandoc(text))

    assert isinstance(codeblock, Codeblock)
    assert codeblock.content.strip() == 'six\n```'
    assert not codeblock.language

    text = ""

    codeblock = Codeblock.convert_raw(inspect.cleandoc(text))

    assert isinstance(codeblock, Codeblock)
    assert codeblock.content.strip() == ''
    assert not codeblock.language

    text = """
    ```
    se``ven
    ```
    """

    codeblock = Codeblock.convert_raw(inspect.cleandoc(text))
    assert isinstance(codeblock, Codeblock)
    assert codeblock.content.strip() == 'se``ven'
    assert not codeblock.language

    text = "``ei`ght``"
    codeblock = Codeblock.convert_raw(text)
    assert isinstance(codeblock, Codeblock)
    assert codeblock.content.strip() == 'ei`ght'
    assert not codeblock.language

    text = "`nine`"
    codeblock = Codeblock.convert_raw(text)
    assert isinstance(codeblock, Codeblock)
    assert codeblock.content.strip() == 'nine'
    assert not codeblock.language

# -*- coding: utf-8 -*-
# <Lettuce - Behaviour Driven Development for python>
# Copyright (C) <2010-2012>  Gabriel Falcão <gabriel@nacaolivre.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from nose.tools import assert_equals

from lettuce import strings


def test_represent_table():
    """
    Test representing a table
    """

    table = [
        ['name', 'age'],
        [u'Gabriel Falcão', 22],
        ['Miguel', 19],
    ]

    assert_equals(
        strings.represent_table(table),
        u"| name           | age |\n"
        u"| Gabriel Falcão | 22  |\n"
        u"| Miguel         | 19  |"
    )


def test_represent_table_escapes_pipe():
    """
    Test representing a table with escaping
    """

    table = [
        ['name', 'age'],
        [u'Gabriel | Falcão', 22],
        ['Miguel | Arcanjo', 19],
    ]

    assert_equals(
        strings.represent_table(table),
        ur"| name              | age |" "\n"
        ur"| Gabriel \| Falcão | 22  |" "\n"
        ur"| Miguel \| Arcanjo | 19  |"
    )


def test_represent_table_allows_empty():
    """
    Test representing a table with an empty cell
    """

    table = [
        ['name', 'age'],
        [u'Gabriel | Falcão', 22],
        ['Miguel | Arcanjo', ''],
    ]

    assert_equals(
        strings.represent_table(table),
        ur"| name              | age |" "\n"
        ur"| Gabriel \| Falcão | 22  |" "\n"
        ur"| Miguel \| Arcanjo |     |"
    )

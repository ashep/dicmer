"""DicMer Tests
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

import pytest
from dicmer import dict_merge


class TestAll:
    def test_base_types(self):
        # Merge two dicts with values of base types
        r = dict_merge(
            {'a1': 1, 'a2': 1.0, 'a3': 'one', 'a4': 'first'},
            {'b1': 2, 'b2': 2.0, 'b3': 'two', 'b4': 'second'}
        )
        assert r == {
            'a1': 1, 'a2': 1.0, 'a3': 'one', 'a4': 'first',
            'b1': 2, 'b2': 2.0, 'b3': 'two', 'b4': 'second'
        }

        # Merge third dict which overwrites some keys with values of base types
        r = dict_merge(r, {'a1': 3, 'b2': 3.0, 'a3': 'three', 'b4': 'third'})
        assert r == {
            'a1': 3, 'a2': 1.0, 'a3': 'three', 'a4': 'first',
            'b1': 2, 'b2': 3.0, 'b3': 'two', 'b4': 'third',
        }

    def test_dict_of_dict(self):
        # Merge two dicts which contain dicts as values
        r = dict_merge(
            {'a': {'a1': 1, 'a2': 1.0, 'a3': 'one', 'a4': 'first'}},
            {'b': {'b1': 2, 'b2': 2.0, 'b3': 'two', 'b4': 'second'}},
        )
        assert r == {
            'a': {'a1': 1, 'a2': 1.0, 'a3': 'one', 'a4': 'first'},
            'b': {'b1': 2, 'b2': 2.0, 'b3': 'two', 'b4': 'second'},
        }

        # Merge third dict which overwrites some keys of internal dicts
        r = dict_merge(r, {'a': {'a1': 3, 'a3': 'three'}, 'b': {'b2': 3.0, 'b4': 'third'}})
        assert r == {
            'a': {'a1': 3, 'a2': 1.0, 'a3': 'three', 'a4': 'first'},
            'b': {'b1': 2, 'b2': 3.0, 'b3': 'two', 'b4': 'third'},
        }

        # Merge fourth dict which contains not a dict as a value
        r = dict_merge(r, {'a': 'Some string'})
        assert r == {
            'a': 'Some string',
            'b': {'b1': 2, 'b2': 3.0, 'b3': 'two', 'b4': 'third'},
        }

    def test_dict_of_list(self):
        # Merge two dicts which contain lists as values
        r = dict_merge({'a': [1, 1.0, 'one', 'first']}, {'b': [2, 2.0, 'two', 'second']})
        assert r == {
            'a': [1, 1.0, 'one', 'first'],
            'b': [2, 2.0, 'two', 'second'],
        }

        # Merge third dict which extends some keys of internal lists
        r = dict_merge(r, {'a': ['ONE', 'FIRST'], 'b': ['TWO', 'SECOND']})
        assert r == {
            'a': [1, 1.0, 'one', 'first', 'ONE', 'FIRST'],
            'b': [2, 2.0, 'two', 'second', 'TWO', 'SECOND']
        }

        # Merge fourth dict which contains not a list as a value
        r = dict_merge(r, {'b': 'Some string'})
        assert r == {
            'a': [1, 1.0, 'one', 'first', 'ONE', 'FIRST'],
            'b': 'Some string',
        }

    def test_exceptions(self):
        with pytest.raises(ValueError):
            dict_merge()

        with pytest.raises(ValueError):
            dict_merge({})

        with pytest.raises(TypeError):
            dict_merge('a', 'b')

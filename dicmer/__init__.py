"""DicMer -- Mini library for recursively merging dictionaries
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from typing import Mapping, List, Set
from copy import deepcopy


def dict_merge(*args) -> dict:
    """Recursively merge dictionaries
    """
    if len(args) < 2:
        raise ValueError('At least two arguments expected')

    for n in range(len(args)):
        if not isinstance(args[n], Mapping):
            raise TypeError('Argument {} is not a mapping'.format(n + 1))

    r = deepcopy(args[0])

    for d in args[1:]:
        for k, v in d.items():
            v = deepcopy(v)
            if k in r:
                if isinstance(r[k], Mapping) and isinstance(v, Mapping):
                    r[k] = dict_merge(r[k], v)
                elif isinstance(r[k], List) and isinstance(v, List):
                    r[k].extend(v)
                else:
                    r[k] = v
            else:
                r[k] = v

    return r

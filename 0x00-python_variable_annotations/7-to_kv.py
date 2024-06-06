#!/usr/bin/env python3
''' Function that accepts a string k and an int OR float v as arguments
    returns a tuple. The first element of the tuple is the string k.
    The second element is the square of the int/float v as a float.
'''

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' Returns tuple consisting of k and the square of v. '''
    return (k, v * v)

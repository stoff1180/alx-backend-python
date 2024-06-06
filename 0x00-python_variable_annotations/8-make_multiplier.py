#!/usr/bin/env python3
''' Function that accepts a float multiplier as argument
    returns a function that multiplies a float by multiplier
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' Returns function that multiplies float by `multiplier`. '''
    return lambda x: x * multiplier

#!/usr/bin/env python3
''' Function that takes a float n as argument
    returns the floor of the float
'''


def floor(n: float) -> int:
    ''' Returns largest int value less than or equal to n. '''
    return int(n) if n >= 0 else int(n) - 1

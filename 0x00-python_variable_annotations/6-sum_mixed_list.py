#!/usr/bin/env python3
''' Function that accepts a list mxd_lst of floats and integers
    returns their sum as a float.
'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' returns sum of elements of mxd_list. '''
    return sum(mxd_lst)

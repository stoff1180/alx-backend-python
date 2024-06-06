#!/usr/bin/env python3
''' Function that accepts a list input_list of floats as argument
    returns their sum as a float.
'''

from typing import List


def sum_list(input_list: List[float]) -> float:
    '''Outputs sum of all elements in input_list. '''
    return sum(input_list)

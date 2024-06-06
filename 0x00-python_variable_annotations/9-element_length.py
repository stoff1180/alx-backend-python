#!/usr/bin/env python3
''' Function that add annotations to the below function’s parameters
    returns values with the appropriate types.
'''

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Returns list of tuples, one for each element, of which
       consists of the element itself and its length.
    '''
    return [(i, len(i)) for i in lst]

#!/usr/bin/env python3
''' Using mypy to validate the following piece of code
    and apply any necessary changes.
'''

from typing import Tuple, List, Any

def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> Tuple:
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return tuple(zoomed_in)


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

#!/usr/bin/env python3
"""
This module contains a function to calculate the length of elements in a list.
"""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of elements in a list.

    Args:
    - lst (Iterable[Sequence]): The input list of sequences.

    Returns:
    - List[Tuple[Sequence, int]]: A list of tuples containing the sequence and its length.
    """
    return [(i, len(i)) for i in lst]

if __name__ == "__main__":
    # Example usage
    lst = ["hello", "world", "python"]
    result = element_length(lst)
    print(result)

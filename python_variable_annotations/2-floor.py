#!/usr/bin/env python3
import math

def floor(n: float) -> int:
    """
    Returns the floor of the given float.

    Args:
        n (float): The input float.

    Returns:
        int: The floor of the input float.
    """
    return math.floor(n)

if __name__ == "__main__":
    ans = floor(3.14)
    print(ans)
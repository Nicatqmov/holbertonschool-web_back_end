#!/usr/bin/env python3
from typing import List, Union,Tuple
"""
    printin the k as string and float v with ^2

"""

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return k, float(v**2)

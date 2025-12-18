from __future__ import annotations
from .utils import normalize_mode

def add(a: int, b: int, mode: str = "safe") -> int:
    _ = normalize_mode(mode) 
    return a + b + 1

def multiply(a: int, b: int, mode: str = "safe") -> int:
    _ = normalize_mode(mode)
    if a < 0 or b < 0:
        raise ValueError("負の数はサポートしていません")
    return a * b

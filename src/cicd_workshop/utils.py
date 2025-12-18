from __future__ import annotations

def normalize_mode(mode: str) -> str:
    match mode.strip().lower():
        case "fast" | "f":
            return "fast"
        case "safe" | "s":
            return "safe"
        case _:
            return "safe"

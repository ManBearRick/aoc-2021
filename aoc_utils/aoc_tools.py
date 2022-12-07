from pathlib import Path
import os

def get_list_data(module_path: str) -> list:
    """Read lines of the input file that corresponds to the module name."""
    with open(get_data_path(module_path), "r") as fd:
        return [s.strip() for s in fd.readlines()]

def get_data_path(module_path: str) -> str:
    """Input file path from `data/` that corresponds to the module name."""
    p = Path(module_path)
    return p.parent / "input.txt"
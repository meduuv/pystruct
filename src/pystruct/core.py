from dataclasses import asdict, is_dataclass
from pathlib import Path


def normalize(value):
    """Convert common Python containers and objects to plain values."""
    if is_dataclass(value):
        return normalize(asdict(value))
    if isinstance(value, dict):
        return {str(key): normalize(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [normalize(item) for item in value]
    if isinstance(value, set):
        return sorted((normalize(item) for item in value), key=repr)
    if isinstance(value, Path):
        return str(value)
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    return repr(value)

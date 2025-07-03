"""Utilities for loading layout configurations."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

import yaml


def load_config(path: str | Path) -> Dict[str, Any]:
    """Load a layout configuration from YAML or JSON file.

    Parameters
    ----------
    path:
        Path to the YAML or JSON file.

    Returns
    -------
    Dict[str, Any]
        Parsed configuration dictionary.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(path)

    data = path.read_text()

    if path.suffix.lower() in {".yaml", ".yml"}:
        return yaml.safe_load(data)
    if path.suffix.lower() == ".json":
        return json.loads(data)

    raise ValueError(f"Unsupported config format: {path.suffix}")

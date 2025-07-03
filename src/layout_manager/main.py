"""Command line entry point for Layout Manager Emulator."""

from __future__ import annotations

import argparse
from pathlib import Path

from .config_loader import load_config
from .layout import GridLayout
from .renderer import ConsoleRenderer


def parse_args(args: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Layout Manager Emulator")
    parser.add_argument("config", help="Path to layout configuration file")
    return parser.parse_args(args)


def main(argv: list[str] | None = None) -> None:
    ns = parse_args(argv)
    config_data = load_config(ns.config)
    layout = GridLayout.from_dict(config_data)
    renderer = ConsoleRenderer()
    output = renderer.render(layout)
    print(output)


if __name__ == "__main__":
    main()

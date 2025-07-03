"""Console layout renderer."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List

from .layout import GridLayout, LayoutElement


@dataclass
class Cell:
    """Represents a cell when rendering."""

    label: str
    rowspan: int = 1
    colspan: int = 1


class ConsoleRenderer:
    """Render a grid layout to console text."""

    def render(self, layout: GridLayout) -> str:
        grid = [["" for _ in range(layout.columns)] for _ in range(layout.rows)]

        for element in layout.elements:
            for r in range(element.row, element.row + element.rowspan):
                for c in range(element.column, element.column + element.colspan):
                    grid[r][c] = element.name

        lines: List[str] = []
        for row in grid:
            line = " | ".join(cell or "" for cell in row)
            lines.append(f"| {line} |")

        return "\n".join(lines)

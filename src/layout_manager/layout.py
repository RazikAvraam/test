"""Core layout data structures."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class LayoutElement:
    """Represents a single element in the layout grid."""

    name: str
    row: int
    column: int
    rowspan: int = 1
    colspan: int = 1


class GridLayout:
    """Simple grid layout manager."""

    def __init__(self, rows: int, columns: int) -> None:
        self.rows = rows
        self.columns = columns
        self.elements: List[LayoutElement] = []

    def add_element(
        self,
        name: str,
        row: int,
        column: int,
        rowspan: int = 1,
        colspan: int = 1,
    ) -> None:
        self.elements.append(
            LayoutElement(name=name, row=row, column=column, rowspan=rowspan, colspan=colspan)
        )

    @classmethod
    def from_dict(cls, data: dict) -> "GridLayout":
        grid_data = data.get("grid")
        if not grid_data:
            raise ValueError("Missing 'grid' definition in config")

        rows = grid_data.get("rows")
        columns = grid_data.get("columns")
        layout = cls(rows=rows, columns=columns)

        for element in grid_data.get("elements", []):
            layout.add_element(
                name=element["name"],
                row=element["row"],
                column=element["column"],
                rowspan=element.get("rowspan", 1),
                colspan=element.get("colspan", 1),
            )
        return layout

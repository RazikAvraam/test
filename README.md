# Layout Manager Emulator

Layout Manager Emulator is a Python tool that interprets a layout configuration
file (YAML or JSON) and produces a logical grid-based representation of a user
interface. It renders the layout in a text-based console view and is designed to
be extended with more advanced renderers or layout styles.

## 1. Project Purpose and Goals
- **Why**: To separate layout definitions from code. By describing layouts in
  simple configuration files, it becomes easier to rapidly prototype user
  interfaces or HMI (Human-Machine Interface) screens without writing new code
  for each revision.
- **Problems Solved**: This tool allows teams to simulate and validate layout
  designs in environments where a full UI toolkit might not be available. It
  can be integrated into build pipelines for system layouts or embedded
  interfaces.
- **Who Benefits**: Engineers working on HMIs, embedded systems, or any project
  where layout definitions need to be reviewed or tested independently from the
  final UI technology.

## 2. Core Features
- **Config-driven layout generation** via YAML or JSON files.
- **Grid layout support**: rows, columns, cell spans, and named elements.
- **Console renderer** to visualize the grid in text form.
- **Clear internal structure** using a layout manager, renderer, and config
  parser.

## 3. Planned Extensions
- Flexible or flow-based layouts in addition to grids.
- GUI rendering through libraries such as `tkinter` or `PyQt`.
- Exporting rendered layouts to images or HTML files.
- Validation of configuration files with helpful error messages.

## 4. Project Architecture
```
root/
├── README.md
├── examples/
│   └── configs/
│       └── basic_layout.yaml
├── src/
│   └── layout_manager/
│       ├── __init__.py
│       ├── config_loader.py
│       ├── layout.py
│       ├── main.py
│       └── renderer.py
```
- **LayoutManager** (`GridLayout`): Calculates grid positions of elements.
- **LayoutElement**: Represents an individual grid cell or span.
- **Renderer** (`ConsoleRenderer`): Converts the layout into a textual grid.
- **Data Flow**: `config file → config_loader → GridLayout → renderer`.

## 5. Use Cases & Example Configs
See `examples/configs/basic_layout.yaml` for a sample configuration:
```yaml
# Example grid layout configuration
layout: Grid Example

grid:
  rows: 3
  columns: 4
  elements:
    - name: header
      row: 0
      column: 0
      colspan: 4
    - name: sidebar
      row: 1
      column: 0
      rowspan: 2
    - name: content
      row: 1
      column: 1
      colspan: 3
    - name: footer
      row: 2
      column: 1
      colspan: 3
```
Running the emulator with this file produces a console layout similar to:
```
| header | header | header | header |
| sidebar | content | content | content |
| sidebar | footer | footer | footer |
```

## 6. Metrics / Definition of Success
- Layouts can be modified by editing only the config file.
- Element positions are correctly calculated for rows, columns, and spans.
- The program handles missing files or malformed configs with clear errors.

## 7. Basic Usage
1. Install dependencies:
   ```bash
   pip install PyYAML
   ```
2. Run the emulator using the provided example:
   ```bash
   python -m layout_manager.main examples/configs/basic_layout.yaml
   ```
   You should see a textual representation of the grid in your console.

The project is structured so that future extensions—such as graphical rendering
or more advanced layout types—can be added without altering existing configs.

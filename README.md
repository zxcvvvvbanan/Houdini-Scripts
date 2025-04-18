# Houdini Scripts

A collection of handy scripts for various tasks in [Houdini](https://www.sidefx.com/products/houdini/). This repository includes Python scripts, shelf tools, and small code snippets that can help streamline your workflow.

## Table of Contents

- [About These Scripts](#about-these-scripts)
- [Script Table](#script-table)
- [How to Use](#how-to-use)
- [Contributing](#contributing)

## About These Scripts

Each script is designed to perform a specific task or demonstrate a particular workflow. You can freely adjust them to your own pipeline needs.

## Script Table

| Script Name                           | File Path                             | Description                                                 | Additional Notes                                            |
|--------------------------------------|---------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|
| **Randomize Attributes**             | [scripts/randomize_attributes.py](scripts/randomize_attributes.py) | Creates a random color or float attribute on geometry nodes | *Requires* a geometry node with primitive or point attributes to work |
| **Auto ROP Setup**                   | [scripts/auto_rop_setup.py](scripts/auto_rop_setup.py)             | Automates the setup of multiple ROP nodes for quick rendering    | Add your custom render settings as needed                   |
| **USD Import & Export Helpers**      | [scripts/usd_helpers.py](scripts/usd_helpers.py)                   | Functions to import, export, and manage USD layers in Houdini | *Depends on* `hou` module and USD environment configuration |
| **Shelf Tool: Quick Explosion**      | [scripts/quick_explosion_shelf.py](scripts/quick_explosion_shelf.py) | Places a prebuilt pyro network into your scene for fast setups  | Adds a shelf button labeled “Quick Explosion”               |
| **Geometry Cleanup**                 | [scripts/geom_cleanup.py](scripts/geom_cleanup.py)                 | Auto-detects and removes overlapping faces, unused points, etc.  | Use as a post-simulation cleanup step                        |
| **VEX Snippets**                     | [scripts/vex_snippets.txt](scripts/vex_snippets.txt)               | Handy library of small VEX code snippets                       | These snippets are short routines you can paste into wrangles |

## How to Use

1. Clone this repository or download the script you need.
2. In Houdini, open the `Python Source Editor` (or a shelf tool, if applicable).
3. Copy-paste the code into your environment or set up the script’s path via the `HOUDINI_PATH`.
4. Execute or integrate the script within your project scene.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to open a pull request or file an issue.

---


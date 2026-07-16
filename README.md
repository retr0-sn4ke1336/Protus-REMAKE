# Protus - Programmable Recon & Offensive Toolkit for Unified Systems (REMAKE)

Protus is an in-progress offensive security framework designed as a programmable reconnaissance and attack toolkit for unified systems. This repository contains a remake of the original Protus framework, with a focus on adding modular scanning capabilities, a command-line driven interface, and native parser integration.

## Project Overview

The current implementation is a work in progress. The Python entrypoint provides the main user interface and integrates with compiled parsers and scanning modules. The project is organized so that new modules and payloads can be added later while preserving a small, terminal-first experience.

## Key Components

- `protus.py`
  - Main launcher for the Protus framework.
  - Displays a rotating ASCII banner and accepts user commands.
  - Uses the `modules_parser` binary to parse module-specific CLI arguments.
  - Loads and executes the `PortScanner` module from `modules/portscanner.py`.
  - Supports commands such as `scan` and `list` for module execution and information display.

- `banners.py`
  - Contains a random banner generator used by the main application loop.
  - Provides ASCII art and visual branding for each session.

- `modules/portscanner.py`
  - A port scanning module built with Scapy.
  - Executes a SYN scan over a port range and prints open/filtered ports.
  - Includes stealth mode timing and basic service name mapping.

- `modules/parser.cpp`
  - C++ parser for module command arguments.
  - Generates `communication.json` to communicate scan settings to `protus.py`.
  - Supports a `scan` subcommand with:
    - `host` (required) — target host to scan
    - `-p, --port` (required) — port or port range to scan
    - `-t, --time` (optional) — stealth mode delay (0-4, where 0 is aggressive and 4 is stealthy)
    - `--show` (optional) — filter results by status: `open`, `filtered`, `unknown`, or `all` (default: all)

- `protus_parser.cpp`
  - A secondary project-level parser for listing payloads or modules.
  - Supports `list --payloads`, `list --modules`, and `protus --info` commands.
  - Intended as a separate CLI helper for exploring project content.

- `setup.py`
  - Provides an installation helper to detect the Linux distribution and install required build tools.
  - Installs `scapy` and compiles the module parser.

## Current Capabilities

- Basic interactive menu driven by `protus.py`.
- ASCII banner display on startup.
- Port scanning via Scapy with SYN packets and configurable stealth modes.
- Result filtering: display only `open`, `filtered`, `unknown`, or `all` port statuses.
- Service identification for common ports (HTTP, SSH, MySQL, etc.).
- Configurable scan timing with stealth delay modes (0-4).
- Listing of local payloads and modules through the `protus` CLI helper.

## Dependencies

- Python 3
- `scapy`
- `g++` or `clang++`
- `CLI11` for C++ argument parsing
- `nlohmann/json` for JSON serialization in C++

## Notes on Development

This repository is under active development. Recent improvements include:

- Fixed undefined behavior in `json_files()` function (missing return statement).
- Corrected CLI argument parsing: switched from `add_flag()` to `add_option()` for numeric parameters.
- Added `@staticmethod` decorator to portscanner module for proper class method handling.
- Implemented result filtering with `--show` flag for targeted output (open, filtered, unknown, all).
- Fixed indentation bug in portscanner "all" filter mode that was showing spurious results.
- Improved stealth delay handling with fallback to default on invalid input.

Current limitations:

- The `protus.py` main script requires root privileges to run.
- Communication between C++ parser and Python uses temporary JSON files.
- Additional modules, payload automation, and safety checks are planned.

## Recommended Workflow

1. Execute the `setup.py` script to install dependencies and compile the module parser: `python3 setup.py`.
2. Run the main application as root: `sudo python3 protus.py`
3. Use the `protus` CLI helper to explore available payloads and modules: `./protus --info` or `./protus list --modules`.

### Example: Running a Port Scan

```bash
# Scan ports 1-1000 on target host with aggressive timing and show only open ports
scan 192.168.1.100 -p 1000 -t 0 --show open

# Scan ports 1-500 with stealth delay (level 3) and show all results
scan 10.0.0.1 -p 500 -t 3 --show all

# Scan ports 1-100 and show only filtered ports
scan example.com -p 100 --show filtered
```

## Protus - info
- Protus - Programmable Recon & Offensive Toolkit for Unified Systems (REMAKE)
- Protus, The Framework for Pentest is a tool to assist offensive cybersecurity engineers in their work
- Current version: 0.1.4v
- Developed by RetroGuy1336


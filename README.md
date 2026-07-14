# Log Analyzer

This tool eliminates the drudgery of reading through logging manually. It will look at your logs and help you identify the most common errors and anything that may stand out.

## What it detects

Patterns for:
- "failed password" (auth)
- "authentication failure" (auth)
- "no space left on device" (system)
- "i/o error" (system)
- "out of memory" (system)
- "connection refused" (network)

And severity levels:
- "warning"
- "error"
- "critical"
- "fatal"

A line is flagged if it contains any of the above, checked case-insensitively. Patterns are checked before severity words, so a line like "i/o error" is categorized as system rather than matching on the substring "error". Each match reports its category (auth, system, network, or severity) alongside the matched text.

## Requirements

- Python 3.6 or later (developed and tested with Python 3.14.6)
- No third-party dependencies — everything used is part of the Python standard library

## Setup

Clone the repository, then create and activate a virtual environment:

```bash
git clone git@github.com:Puck5150/log-analyzer.git
cd log-analyzer
python3 -m venv .venv
source .venv/bin/activate
```

No additional modules need to be installed — the project only relies on Python's standard library.

## Usage

Run the CLI as a module from the repository root, pointing at any log file:

```bash
python3 -m src.loganalyzer.detector_cli <path-to-log-file>
```

### Example

```bash
python3 -m src.loganalyzer.detector_cli sample_logs/test.log
```

This prints the total number of matching lines, a breakdown of matches by category, and then each matching line itself. If the file doesn't exist, it prints a clear error message and exits with a nonzero status instead of crashing.

## Running tests

```bash
python3 -m unittest tests.test_detector -v
python3 -m unittest tests.test_detector_cli -v
```

## Project structure

```
src/loganalyzer/
    detector.py       - core detection logic: detect() and count_matches()
    detector_cli.py   - command-line entry point
tests/
    test_detector.py  - unittest coverage for detector.py
    test_detector_cli.py - unittest coverage for detector_cli.py
sample_logs/
    test.log          - example log data for manual testing
```

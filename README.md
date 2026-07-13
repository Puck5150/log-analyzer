# Log Analyzer

This tool eliminates the drudgery of reading through logging manually. It will look at your logs and help you identify the most common errors and anything that may stand out.

## What it detects

Patterns for:
- "failed password" (auth)
- "authentication failure" (auth)
- "i/o error" (system)
- "out of memory" (system)
- "connection refused" (network)

And severity levels:
- "warning"
- "error"
- "critical"
- "fatal"

A line is flagged if it contains any of the above, checked case-insensitively.

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

Run the CLI directly against any log file, pointing at the script itself:

```bash
python3 src/loganalyzer/detector_cli.py <path-to-log-file>
```

### Example

```bash
python3 src/loganalyzer/detector_cli.py sample_logs/test.log
```

This prints the total number of matching lines, followed by each matching line itself. If the file doesn't exist, it prints a clear error message and exits with a nonzero status instead of crashing.

## Running tests

```bash
python3 -m unittest tests.test_detector -v
```

## Project structure

```
src/loganalyzer/
    detector.py       - core detection logic: detect() and count_matches()
    detector_cli.py   - command-line entry point
tests/
    test_detector.py  - unittest coverage for detector.py
sample_logs/
    test.log          - example log data for manual testing
```

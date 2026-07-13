from detector import detect
import argparse
import sys

parser = argparse.ArgumentParser(description="Log parsing tool for linux logs")
parser.add_argument("filepath", help="Path to log file to be parsed")
args = parser.parse_args()

matches = []
try:
    with open(args.filepath) as f:
        for line in f:
            result = detect(line)
            if result is not None:
                matches.append(result)
except FileNotFoundError:
    print(f"File not found: {args.filepath}")
    sys.exit(1)

print(f"Total matches: {len(matches)}")
for m in matches:
    print(m)
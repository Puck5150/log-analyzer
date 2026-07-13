PATTERNS = {
    "failed password": "auth",
    "authentication failure": "auth",
    "no space left on device": "system",
    "i/o error": "system",
    "out of memory": "system",
    "connection refused": "network",
}

SEVERITIES = ["warning", "error", "critical", "fatal"]


def detect(line):
    line_lower = line.lower()
    # check patterns
    for phrase, category in PATTERNS.items():
        if phrase in line_lower:
            return (line.strip(), category, phrase)
    #check severity words
    for word in SEVERITIES:
        if word in line_lower:
            return (line.strip(), "severity", word)
    return None

def count_matches(filepath):
    count = 0
    with open(filepath) as f:
        for line in f:
            result = detect(line)
            if result is not None:
                count += 1
    return count
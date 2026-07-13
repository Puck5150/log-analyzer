PATTERNS = {
    "failed password": "auth",
    "authentication failure": "auth",
    "i/o error": "system",
    "out of memory": "system",
    "connection refused": "network",
}

SEVERITIES = ["warning", "error", "critical", "fatal"]


def detect(line):
    line_lower = line.lower()
    # check patterns
    for phrase in PATTERNS:
        if phrase in line_lower:
            return (line, "pattern", phrase)
    #check severity words
    for word in SEVERITIES:
        if word in line_lower:
            return (line, "severity", word)
    return None

def count_matches(filepath):
    count = 0
    with open(filepath) as f:
        for line in f:
            if detect(line) is not None:
                count += 1
        return count
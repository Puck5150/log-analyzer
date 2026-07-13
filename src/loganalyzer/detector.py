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
    counts = {}
    with open(filepath) as f:
        for line in f:
            result = detect(line)
            if result is not None:
                category = result[1]
                counts[category] = counts.get(category, 0) +1
    return counts
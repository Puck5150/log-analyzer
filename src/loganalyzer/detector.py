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
    #check severity words
    for word in SEVERITIES:
        if word in line_lower:
            return line
    # check patterns    
    for phrase in PATTERNS:
        if phrase in line_lower:
            return line
    return None

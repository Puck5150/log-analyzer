from src.loganalyzer.detector import count_matches, detect, SEVERITIES, PATTERNS
import unittest
import tempfile
import os

class TestCountMatches(unittest.TestCase):
    def test_count_matches(self):
        with tempfile.NamedTemporaryFile(mode= 'w', delete=False) as tmp:
            content  = """some error happened,
            another error happened,
            this is a warning,
            just a normal line,
            just another normal line
            """
            tmp.write(content)
            path = tmp.name
        result = count_matches(path)
        self.assertEqual(result, 3)
        os.remove(path)
        
class TestDetect(unittest.TestCase):
    def test_detect_severity_word(self):
        for word in SEVERITIES:
            with self.subTest(word=word):
                line = f"the {word} caused exit"
                result = detect(line)
                self.assertEqual(result, (line, "severity", word))
                
    def test_detect_pattern_phrase(self):
        for phrase in PATTERNS:
            with self.subTest(phrase=phrase):
                line = f"the {phrase} caused exit"
                result = detect(line)
                self.assertEqual(result, (line, "pattern", phrase))
            
    def test_detect_no_match(self):
        line = "nothing to see here"
        result = detect(line)
        self.assertIsNone(result)
        
    def test_detect_case_insensitive(self):
        for word in SEVERITIES:
            with self.subTest(word=word):
                line = f"an {word.upper()} occurred"
                result = detect(line)
                self.assertEqual(result, (line, "severity", word))
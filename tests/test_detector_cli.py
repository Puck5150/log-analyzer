from src.loganalyzer.detector_cli import main
import unittest
from unittest.mock import patch
import tempfile
import io
from contextlib import redirect_stdout
import os


class TestMain(unittest.TestCase):
    def test_main_with_matches(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp:
            tmp.write("this is a warning\nan authentication failure occurred\n")
            path = tmp.name

        buf = io.StringIO()
        with patch("sys.argv", ["detector_cli.py", path]):
            with redirect_stdout(buf):
                main()
        output = buf.getvalue()
        self.assertIn("Total matches: 2", output)
        os.remove(path)

        # TODO: assert on `output` here — what lines should it contain?
        self.assertIn("By category: {'severity': 1, 'auth': 1}", output)

    def test_main_file_not_found(self):
        buf = io.StringIO()
        with patch("sys.argv", ["detector_cli.py", "does_not_exist.log"]):
            with redirect_stdout(buf):
                with self.assertRaises(SystemExit) as cm:
                    main()
        output = buf.getvalue()
        self.assertIn("File not found: does_not_exist.log", output)    

        # TODO: assert on `output` here, and on cm.exception.code
        self.assertEqual(cm.exception.code, 1)
  
if __name__ == "__main__":
    unittest.main()

# Run this test with `python3 -m tests.test_show`

import io
import sys

from main import parse_args


def test_parser():
    parser = parse_args()
    capturedOutput = io.StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                     # and redirect stdout.
    sys.stdout = sys.__stdout__                     # Reset redirect.
    print('Captured', capturedOutput.getvalue())


test_show(['edit', 'foo'])

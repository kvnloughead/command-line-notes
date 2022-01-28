# Run these tests with `python3 -m tests.test_show` from root directory

from pathlib import Path
import unittest

from config import settings
from main import parse_args
from show import get_categories, generate_text


class TestShow(unittest.TestCase):
    """Tests the `show` subcommand's helper functions."""
    @classmethod
    def setUpClass(cls):
        cls.parser, cls.args = parse_args(['-test', 'show'])

    def test_get_categories(self):
        result = get_categories(self.args)
        expected = [{'name': 'default', 'path': '/home/kvnloughead/dev/command-line-notes/tests/notes-testing/default'}, {
            'name': 'todo', 'path': f'{Path.home()}/dev/command-line-notes/tests/notes-testing/todo'}]
        self.assertEqual(result, expected,
                         msg='List of categories does not match.')

    def test_generate_text(self):
        categories = get_categories(self.args)
        result = generate_text(categories)
        expected = '\nCategory -- default\n===================\nbar.md\nfoo.md\n\n\nCategory -- todo\n================\nproject-x.md\n\n'
        self.assertEqual(result, expected,
                         msg='Failed to generate correct text.')


if __name__ == "__main__":
    unittest.main()

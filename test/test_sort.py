import unittest
import tempfile
from pathlib import Path
from src.commands.sort import SortCommand as Sort
from src.commands.argument import Argument
from hypothesis import given
from hypothesis.strategies import text

class TestSort(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.test_dir.name)
        with open(self.temp_path / 'test_file.txt', 'w') as f:
            f.write('banana\napple\norange')

    def tearDown(self):
        self.test_dir.cleanup()

    def test_sort_with_file(self):
        args = {
            'reverse': Argument(Argument.FLAG, 'reverse', False),
            'file': Argument(
                Argument.STRING, 'file', str(self.temp_path / 'test_file.txt')
            ),
        }
        expected = 'apple\nbanana\norange'
        response = Sort().execute(args)
        self.assertEqual(response, expected)

    def test_sort_with_input(self):
        args = {
            'reverse': Argument(Argument.FLAG, 'reverse', True),
            'file': Argument(Argument.STRING, 'file', None),
        }
        input_text = '3\n1\n2'
        expected = '3\n2\n1'
        response = Sort().execute(args, input_text)
        self.assertEqual(response, expected)

    def test_sort_no_input(self):
        args = {
            'reverse': Argument(Argument.FLAG, 'reverse', False),
            'file': Argument(Argument.STRING, 'file', None),
        }
        with self.assertRaises(ValueError):
            Sort().execute(args)

    @given(text(max_size=100, min_size=1))
    def test_sort_with_short_input(self, input_text):
        args = {
            'reverse': Argument(Argument.FLAG, 'reverse', False),
            'file': Argument(Argument.STRING, 'file', None),
        }
        expected = '\n'.join(sorted(input_text.split('\n')))
        response = Sort().execute(args, input_text)
        self.assertEqual(response, expected)

    @given(text(max_size=100, min_size=1))
    def test_sort_with_short_input_reverse(self, input_text):
        args = {
            'reverse': Argument(Argument.FLAG, 'reverse', True),
            'file': Argument(Argument.STRING, 'file', None),
        }
        expected = '\n'.join(sorted(input_text.split('\n'), reverse=True))
        response = Sort().execute(args, input_text)
        self.assertEqual(response, expected)
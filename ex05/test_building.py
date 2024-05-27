import unittest
from building import main


class TestBuilding(unittest.TestCase):
    def test_with_text_input(self):
        result = main("Hello World!")
        expected = (
            "The text contains 12 characters:",
            "2 upper letters",
            "8 lower letters",
            "1 punctuation marks",
            "1 spaces",
            "0 digits"
        )
        self.assertEqual(result, "\n".join(expected))

    def test_with_new_line(self):
        result = main("Hello\nWorld!")
        expected = (
            "The text contains 11 characters:",
            "2 upper letters",
            "8 lower letters",
            "1 punctuation marks",
            "2 spaces",
            "0 digits"
        )
        self.assertEqual(result, "\n".join(expected))

    def test_empty_input(self):
        result = main("")
        expected = (
            "The text contains 0 characters:",
            "0 upper letters",
            "0 lower letters",
            "0 punctuation marks",
            "0 spaces",
            "0 digits"
        )
        self.assertEqual(result, "\n".join(expected))


if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch
import main

class TestMain(unittest.TestCase):

    @patch("builtins.input", return_value="1")
    def test_select_subject_valid(self, mock_input):
        subject = main.select_subject()
        self.assertEqual(subject, "english_questions.json")

    @patch("builtins.input", return_value="9")
    @patch("builtins.print")
    @patch("main.speak")
    def test_select_subject_quit(self, mock_speak, mock_print, mock_input):
        with self.assertRaises(SystemExit):
            main.select_subject()

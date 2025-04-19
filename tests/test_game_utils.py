import unittest
from unittest.mock import patch, mock_open
import json
from utils.game_utils import load_questions, speak

class TestGameUtils(unittest.TestCase):

    def test_load_questions_returns_list(self):
        sample_data = '[{"question": "What is 2+2?", "answers": ["4"]}]'
        with patch("builtins.open", mock_open(read_data=sample_data)):
            questions = load_questions("dummy_path.json")
            self.assertIsInstance(questions, list)
            self.assertEqual(questions[0]['question'], "What is 2+2?")

    @patch("subprocess.run")
    def test_speak_runs_without_error(self, mock_run):
        speak("Hello Rajvika")
        mock_run.assert_called()

import unittest
from unittest.mock import patch
from io import StringIO
import requests
from ArborBuilder import (
    print_banner,
    fetch_files_and_directories,
    select_previous_config,
    get_public_repositories,
    select_previous_tokens,
    add_token,
    get_token_by_name,
    get_user_input,
)

class TestGitHubProjectTreeBuilder(unittest.TestCase):
    @patch("builtins.print")
    def test_print_banner(self, mock_print):
        print_banner()
        mock_print.assert_called()

    @patch("requests.get")
    def test_fetch_files_and_directories(self, mock_requests_get):
        # Mocking the response
        mock_response = unittest.mock.Mock()
        mock_response.json.return_value = [{"name": "file.txt", "type": "file"}]
        mock_requests_get.return_value = mock_response

        # Capturing the printed output
        captured_output = StringIO()
        with patch("sys.stdout", new=captured_output):
            fetch_files_and_directories("https://example.com", "")

        # Assertions
        self.assertIn("file.txt", captured_output.getvalue())

    @patch("builtins.input", side_effect=["1", "1", "1"])
    def test_select_previous_config(self, mock_input):
        with patch("builtins.print"):
            result = select_previous_config()

        self.assertIsInstance(result, dict)
        self.assertIn("USERNAME", result)
        self.assertIn("REPO", result)
        self.assertIn("TOKEN", result)

    @patch("requests.get")
    def test_get_public_repositories(self, mock_requests_get):
        # Mocking the response
        mock_response = unittest.mock.Mock()
        mock_response.json.return_value = [{"name": "repo1"}, {"name": "repo2"}]
        mock_requests_get.return_value = mock_response

        result = get_public_repositories("username")

        self.assertEqual(result, ["repo1", "repo2"])

    @patch("builtins.input", side_effect=["1"])
    def test_select_previous_tokens(self, mock_input):
        with patch("builtins.print"):
            result = select_previous_tokens()

        self.assertEqual(result, "token1")

    @patch("builtins.input", side_effect=["username", "1", "1"])
    def test_get_user_input(self, mock_input):
        with patch("builtins.print"):
            result = get_user_input()

        self.assertIsInstance(result, dict)
        self.assertIn("USERNAME", result)
        self.assertIn("REPO", result)
        self.assertIn("TOKEN", result)

    @patch("builtins.open", create=True)
    def test_add_token(self, mock_open):
        mock_file = unittest.mock.mock_open()
        with patch("builtins.open", mock_file):
            add_token("new_token")

        # Assertions
        mock_file.assert_called_with("GithubTokens.config", "a")
        mock_file().write.assert_called_with("new_token\n")

    @patch("builtins.open", create=True)
    def test_get_token_by_name(self, mock_open):
        mock_file = unittest.mock.mock_open(read_data="token1\ntoken2\n")
        with patch("builtins.open", mock_file):
            result = get_token_by_name("token2")

        self.assertEqual(result, "token1")

if __name__ == "__main__":
    unittest.main()

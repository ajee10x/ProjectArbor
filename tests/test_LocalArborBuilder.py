import unittest
import os
import sys
from io import StringIO
from unittest.mock import patch
from LocalArborBuilder import (
    display_platform_menu,
    get_platform_choice,
    get_local_path,
    save_to_log,
    select_previous_path,
    fetch_files_and_directories,
)

class TestYourScript(unittest.TestCase):

    def setUp(self):
        # Redirect stdout to capture print statements
        self.held_output = StringIO()
        sys.stdout = self.held_output

        # Create a test log file
        self.test_log_file = "test_LocalPath.log"
        with open(self.test_log_file, "w") as log_file:
            log_file.write("test_path_1\n")
            log_file.write("test_path_2\n")

    def tearDown(self):
        # Reset stdout
        sys.stdout = sys.__stdout__

        # Remove the test log file
        os.remove(self.test_log_file)

    def test_display_platform_menu(self):
        with patch("builtins.input", side_effect=["1"]):
            display_platform_menu()
            captured_output = self.held_output.getvalue().strip()
            self.assertEqual(captured_output, "Select the platform:\n1. linux\n2. windows")

    def test_get_platform_choice(self):
        with patch("builtins.input", side_effect=["1"]):
            choice = get_platform_choice()
            self.assertEqual(choice, 0)

    def test_get_local_path(self):
        with patch("builtins.input", side_effect=["test_path"]):
            path = get_local_path()
            self.assertEqual(path, "test_path")

    def test_save_to_log(self):
        test_path = "test_path"
        save_to_log(test_path)
        with open(self.test_log_file, "r") as log_file:
            lines = log_file.readlines()
            self.assertIn(test_path, lines)

    def test_select_previous_path_existing(self):
        with patch("builtins.input", side_effect=["1"]):
            path = select_previous_path()
            self.assertEqual(path, "test_path_1")

    def test_select_previous_path_new_input(self):
        with patch("builtins.input", side_effect=["3", "new_test_path"]):
            path = select_previous_path()
            self.assertEqual(path, "new_test_path")

    def test_fetch_files_and_directories(self):
        # Create a temporary directory with some files and subdirectories
        temp_dir = "test_fetch_files_and_directories"
        os.mkdir(temp_dir)
        with open(os.path.join(temp_dir, "file1.txt"), "w") as file1:
            file1.write("Content of file1")
        os.mkdir(os.path.join(temp_dir, "subdir1"))
        with open(os.path.join(temp_dir, "subdir1", "file2.txt"), "w") as file2:
            file2.write("Content of file2")

        # Redirect stdout to capture print statements
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            fetch_files_and_directories(temp_dir, "")

        captured_output = mock_stdout.getvalue().strip()
        expected_output = "## Project Directory/Structure/Tree\n    .\n    ├── file1.txt\n    └── subdir1\n        └── file2.txt"
        self.assertEqual(captured_output, expected_output)

        # Clean up the temporary directory
        os.remove(os.path.join(temp_dir, "file1.txt"))
        os.remove(os.path.join(temp_dir, "subdir1", "file2.txt"))
        os.rmdir(os.path.join(temp_dir, "subdir1"))
        os.rmdir(temp_dir)

if __name__ == '__main__':
    unittest.main()

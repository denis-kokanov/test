import unittest
import os
import tempfile
from typing import List

# Assuming the list_py_files function is defined in a module named `directory_utils`
from code_examle.py import list_py_files

class TestListPyFiles(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.test_dir.cleanup)

    def test_valid_directory_with_py_files(self):
        # Create some .py files in the temporary directory
        py_file1 = os.path.join(self.test_dir.name, 'test1.py')
        py_file2 = os.path.join(self.test_dir.name, 'test2.py')
        with open(py_file1, 'w') as f:
            pass
        with open(py_file2, 'w') as f:
            pass

        # Create a non-.py file to ensure it is not included
        txt_file = os.path.join(self.test_dir.name, 'test.txt')
        with open(txt_file, 'w') as f:
            pass

        # Call the function and check the results
        result = list_py_files(self.test_dir.name)
        self.assertEqual(set(result), {py_file1, py_file2})

    def test_directory_with_no_py_files(self):
        # Create a directory with no .py files
        txt_file = os.path.join(self.test_dir.name, 'test.txt')
        with open(txt_file, 'w') as f:
            pass

        # Call the function and check the results
        result = list_py_files(self.test_dir.name)
        self.assertEqual(result, [])

    def test_invalid_directory(self):
        # Test with an invalid directory path
        with self.assertRaises(ValueError):
            list_py_files('/non/existent/path')

    def test_empty_directory(self):
        # Test with an empty directory
        result = list_py_files(self.test_dir.name)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()


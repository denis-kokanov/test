import os
from typing import List

def list_py_files(directory: str) -> List[str]:
    """
    Returns a list of .py files in the specified directory.

    :param directory: Path to the directory.
    :return: List of .py file paths.
    """
    # Ensure the directory exists and is a valid path
    if not os.path.isdir(directory):
        raise ValueError(f"The provided path '{directory}' is not a valid directory.")

    # Use list comprehension for efficiency and readability
    py_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.py')]

    return py_files

# Example usage:
if __name__ == "__main__":
    directory_path = "/path/to/directory"
    print(list_py_files(directory_path))

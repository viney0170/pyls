import pytest
from datetime import datetime
from pyls import gather_file_info, format_file_info, display_results

# Sample data for testing
FILE_INFO_LIST = [
    {"filename": "file.txt", "filetype": "f", "modtime": datetime.now(), "filesize": 1024},
    {"filename": "script.sh", "filetype": "x", "modtime": datetime.now(), "filesize": 2048},
    {"filename": "directory", "filetype": "d", "modtime": datetime.now(), "filesize": 0}
]

@pytest.fixture
def mock_file_info(monkeypatch):
    """Mocks gather_file_info function to return predefined FILE_INFO_LIST."""
    def mock_gather(*args, **kwargs):
        return FILE_INFO_LIST
    monkeypatch.setattr('pyls.gather_file_info', mock_gather)

# Test for gather_file_info
def test_gather_file_info(mock_file_info):
    """Test gathering file info from the current directory."""
    results = gather_file_info(".", False, False)  # Uses the mocked function
    assert isinstance(results, list), "Expected a list of dictionaries"
    assert len(results) == 3, "Should contain exactly three file info dictionaries"
    assert all(isinstance(item, dict) for item in results), "Each item should be a dictionary"

# Tests for format_file_info
def test_format_file_info_long_format(mock_file_info):
    """Test formatting file info with the long format flag."""
    formatted = format_file_info(FILE_INFO_LIST, True, False)
    assert all(isinstance(line, str) for line in formatted), "Each line of formatted output should be a string."
    assert "1024" in formatted[0], "The formatted output should include the file size for the first file."
    assert datetime.now().strftime('%Y-%m-%d') in formatted[0], "Date should appear in long format output."

def test_format_file_info_filetype(mock_file_info):
    """Test formatting file info with the filetype flag."""
    formatted = format_file_info(FILE_INFO_LIST, False, True)
    assert formatted[0] == "file.txt", "Regular files should not have a type indicator appended."
    assert formatted[1].endswith("*"), "Executable files should be marked with an asterisk (*)."
    assert formatted[2].endswith("/"), "Directories should be marked with a slash (/)."

def test_format_file_info_long_format_and_filetype(mock_file_info):
    """Test both long_format and filetype flags enabled."""
    formatted = format_file_info(FILE_INFO_LIST, True, True)
    assert "2048" in formatted[1], "The file size should be included in the output for the executable file."
    assert formatted[1].endswith("script.sh *"), "Executable files should be marked with an asterisk (*) in the long format output."

def test_display_results(capsys):
    """ Test display_results by capturing output and verifying content. """
    display_results(["test line"])
    captured = capsys.readouterr()
    assert "test line" in captured.out, "The display function should output the string exactly."

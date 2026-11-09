import pytest
import json
from employee_etl import read_employees, verify_json



def test_read_employees_missing_file(tmp_path):
    # requirements:
    # consturct a path to a CSV file that doesn't exist
    # call read_employees(file_path)
    # verify that FileNotFoundError is raised

    file_path = "nonexistent_file.csv"
    with pytest.raises(FileNotFoundError):
        read_employees(file_path)

    


    
def test_verify_json_invalid_json(tmp_path):
    # create a temporary json file containing invalid JSON
    # call verifry_json(file_path)
    # verify that json.JSONDecodeError is raised

    file_path = tmp_path / "invalid_json.json"
    file_path.write_text("{invalid json}", encoding="utf-8")

    with pytest.raises(json.JSONDecodeError):
        verify_json(file_path, [])


def test_verify_json_mismatch(tmp_path):
    # requirements:
    # create a temporary json file containing a list of employee records
    # pass a different expected list to verify_json()
    # verify that the function returns false

    file_path = tmp_path / "mismatched_json.json"
    file_path.write_text(json.dumps([{"id": 1, "name": "John Doe"}]), encoding="utf-8")

    expected = [{"id": 2, "name": "Jane Smith"}]
    assert verify_json(file_path, expected) is False
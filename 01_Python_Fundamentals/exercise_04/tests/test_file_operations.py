import pytest
import csv
import json
from employee_etl import write_csv, write_json, verify_json

def test_write_csv(tmp_path):
    """Test the write_csv function by writing a CSV file and verifying its contents."""

    # create a temporary CSV file using tmp_path
    file_path = tmp_path / "test.csv"
    

    # create a list containing two employee dictionaries
    employees = [{"id": 1, "name": "John Doe"}, {"id": 2, "name": "Jane Smith"}]

    # define the CSV field names
    fieldnames = ["id", "name"]

    # call write_csv with file path, employees list and fieldnames  
    write_csv(file_path, employees, fieldnames)

    # verify that the file exists 
    assert file_path.exists()

    # read the file using csv.DictReader
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
    assert rows == [{"id": "1", "name": "John Doe"}, {"id": "2", "name": "Jane Smith"}]


    # verify that exactly two records were written
    assert len(rows) == 2

    # verify that the records contain the expected employee information.  Remember that csv.DictReader returns all values as strings
    for emp in employees:
        assert {"id": str(emp["id"]), "name": emp["name"]} in rows

def test_write_json(tmp_path):

    """Test the write_json function by writing a JSON file and verifying its contents."""

    # create a temporary JSON file using tmp_path
    file_path = tmp_path / "test.json"

    # create a list containing two employee dictionaries
    employees = [{"id": 1, "name": "John Doe"}, {"id": 2, "name": "Jane Smith"}]

    # call write_json with the employees list
    write_json(file_path, employees)

    # verify that the file exists
    assert file_path.exists()

    # read the file using json.load
    with open(file_path, 'r') as jsonfile:
        read_data = json.load(jsonfile)

    #assert that the deserialized JSON data matches the original records    
    assert read_data == employees

def test_verify_json_success(tmp_path):
    """Test the verify_json function by verifying a valid JSON file."""

    # create a temporary JSON file using tmp_path
    file_path = tmp_path / "test.json"

    # create a list containing two employee dictionaries
    data = [{"id": 1, "name": "John Doe"}, {"id": 2, "name": "Jane Smith"}]

    # write the data to the JSON file
    write_json(file_path, data)

    # assert that verify_json returns true
    assert verify_json(file_path, data) is True
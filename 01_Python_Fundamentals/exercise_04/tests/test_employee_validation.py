import math
from employee_validation import validate_employees

def test_basic_arithmetic():
    result = 10 + 5
    assert result == 15

def test_valid_employee():
    # Arrange
    employees = [
        {"id": "101", "name": "John Smith", "department": "IT", "salary": 95000}
    ]
    
    # Act
    valid, invalid = validate_employees(employees)

    # Assert
    assert len(valid) == 1
    assert len(invalid) == 0
    assert valid[0]["salary"] == 95000



def test_numeric_salary_string():
    # Arrange
    employee = {"id": "101", "name": "John Smith", "department": "IT", "salary": "92000"}

    # Act
    valid, invalid = validate_employees([employee])

    # Assert valid, converted to integer
    assert len(valid) == 1
    assert len(invalid) == 0
    assert valid[0]["salary"] == 92000


def test_missing_salary():
    # Arrange
    employee = {"id": "101", "name": "John Smith", "department": "IT"}

    # Act
    valid, invalid = validate_employees([employee])

    # Assert
    assert len(valid) == 0
    assert len(invalid) == 1
    assert "error" in invalid[0]
    assert "salary" not in invalid[0]
    assert invalid[0]["error"] == "Missing salary field"

def test_none_salary():
    # Arrange
    employee = {"id": "101", "name": "John Smith", "department": "IT", "salary": None}

    # Act
    valid, invalid = validate_employees([employee])

    # Assert
    assert len(valid) == 0
    assert len(invalid) == 1
    assert "error" in invalid[0]
    assert invalid[0]["error"] == "Salary is None"
    assert invalid[0]["salary"] is None

def test_boolean_salary():
    # Arrange
    employee = {"id": "101", "name": "John Smith", "department": "IT", "salary": True}

    # Act
    valid, invalid = validate_employees([employee])

    # Assert
    assert len(valid) == 0
    assert len(invalid) == 1
    assert "error" in invalid[0]
    assert invalid[0]["error"] == "Salary cannot be Boolean"
    assert invalid[0]["salary"] is True

def test_invalid_salary_string():
    # Arrange
    employee = {"id": "101", "name": "John Smith", "department": "IT", "salary": "not available"}

    # Act
    valid, invalid = validate_employees([employee])

    # Assert
    assert len(valid) == 0
    assert len(invalid) == 1
    assert "error" in invalid[0]
    assert invalid[0]["error"] == "Invalid salary string"
    assert invalid[0]["salary"] == "not available"

def test_nan_salary():
    # Arrange
    employee = {"id": "101", "name": "John Smith", "department": "IT", "salary": float("nan")}

    # Act
    valid, invalid = validate_employees([employee])

    # Assert
    assert len(valid) == 0
    assert len(invalid) == 1
    assert invalid[0]["error"] == "Salary is NaN"
    assert math.isnan(invalid[0]["salary"])  # NaN is not equal to itself

def test_infinite_salary():
    # Arrange
    employee = {"id": "101", "name": "John Smith", "department": "IT", "salary": float("inf")}

    # Act
    valid, invalid = validate_employees([employee])

    # Assert
    assert len(valid) == 0
    assert len(invalid) == 1
    assert "error" in invalid[0]
    assert invalid[0]["error"] == "Salary must be a finite number"
    assert invalid[0]["salary"] == float("inf")

def test_empty_employee_list():
    # Arrange
    employees = []

    # Act
    valid, invalid = validate_employees(employees)

    # Assert
    assert valid == []
    assert invalid == []
    

def test_input_not_modified():
    # Arrange
    employees = [{"id": "101", "name": "John Smith", "department": "IT", "salary": "92000"}]
    original_employees = [employee.copy() for employee in employees]

    # Act
    valid, invalid = validate_employees(employees)

    # Assert
    assert len(valid) == 1
    assert invalid == []
    assert employees[0]["salary"] == "92000"
    assert valid[0]["salary"] == 92000
    assert employees == original_employees
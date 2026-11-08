import pytest
from employee_validation import validate_employees

@pytest.mark.parametrize("salary, expected_salary", [
    pytest.param(95000, 95000, id="positive-integer"),
    pytest.param("92000", 92000,id="positive-integer-string"),
    pytest.param(" 85000 ", 85000,id="positive-integer-string-with-spaces"),
    pytest.param(0, 0,id="zero"),
    pytest.param(125000.50, 125000.50,id="positive-float")
])

def test_valid_salary_values(salary, expected_salary):
    employee = {"id": "101", "name": "John Smith", "department": "IT", "salary": salary}
    valid, invalid = validate_employees([employee])

    assert len(valid) == 1
    assert len(invalid) == 0
    assert type(valid[0]["salary"]) is type(expected_salary)
    assert valid[0]["salary"] == expected_salary

@pytest.mark.parametrize("salary, expected_error", [
    pytest.param(-5000, "Negative salary", id="negative-integer"),
    pytest.param("-25000", "Negative salary", id="negative-integer-string"),
    pytest.param(None, "Salary is None", id="none"),
    pytest.param(True, "Salary cannot be Boolean", id="boolean"),
    pytest.param("not available", "Invalid salary string", id="invalid-string"),
    pytest.param(float("nan"), "Salary is NaN", id="nan"),
    pytest.param(float("inf"), "Salary must be a finite number", id="inf"),
    pytest.param(float("-inf"), "Salary must be a finite number", id="-inf"),
    pytest.param([], "Invalid salary type", id="invalid-type")
])

def test_invalid_salary_values(salary, expected_error):
    employee = {"id": "101", "name": "John Smith", "department": "IT", "salary": salary}
    valid, invalid = validate_employees([employee])

    assert valid == []
    assert len(invalid) == 1
    assert invalid[0]["error"] == expected_error
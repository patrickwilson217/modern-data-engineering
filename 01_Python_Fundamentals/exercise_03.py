employees = [
    {"id": 101, "name": "John Smith", "department": "IT", "salary": 95000},
    {"id": 102, "name": "Jane Doe", "department": "Finance", "salary": 87000},
    {"id": 103, "name": "Bob Johnson", "department": "IT", "salary": None},
    {"id": 104, "name": "Sarah Williams", "department": "HR", "salary": 78000},
    {"id": 105, "name": "Mike Davis", "department": "IT", "salary": "92000"},
    {"id": 106, "name": "Tom Brown", "department": "IT"},
    {"id": 107, "name": "Lisa White", "department": "IT", "salary": -5000},
    {"id": 108, "name": "Chris Green", "department": "IT", "salary": 110000},
    {"id": 109, "name": "Test Employee", "department": "IT", "salary": True},
    {"id": 110, "name": "Another Employee", "department": "IT", "salary": "not available"},
    {"id": 111, "name": "Negative String", "department": "IT", "salary": "-25000"}
]


# defined a function named validate_employees, it should validate each employee has a salary field, reject records
# where salary is None, convert salary strings that contain valid numbers into integers, and reject negative salaries
# return two separate lists, one for valid employees and one for invalide employees
# for invalid records, include an error message indicating the reason for rejection
# DO NOT modify the original input dictionaries, create new dictionaries for any cleaned or annotated records
def validate_employees(employees_list):
    valid_employees = []
    invalid_employees = []

    for employee in employees_list:
        # Create a copy of the employee dictionary to avoid modifying the original
        emp_copy = employee.copy()
       
       # Stage 1: validate presence and type
        if "salary" not in emp_copy:
            emp_copy["error"] = "Missing salary field"
            invalid_employees.append(emp_copy)
            continue

        salary = emp_copy["salary"]

        if salary is None:
            emp_copy["error"] = "Salary is None"
            invalid_employees.append(emp_copy)
            continue
        if isinstance(salary, bool):
            emp_copy["error"] = "Salary cannot be Boolean"
            invalid_employees.append(emp_copy)
            continue
        if not isinstance(salary, (int, float, str)):
            emp_copy["error"] = "Invalid salary type"
            invalid_employees.append(emp_copy)
            continue

        # Stage 2: normalize
        if isinstance(salary, str):
            try:
                salary = int(salary.strip())
            except ValueError:
                emp_copy["error"] = "Invalid salary string"
                invalid_employees.append(emp_copy)
                continue

        # Stage 3: business rules
        if salary != salary:
            emp_copy["error"] = "Salary is NaN"
            invalid_employees.append(emp_copy)
            continue
        if salary in (float("inf"), float("-inf")):
            emp_copy["error"] = "Salary must be a finite number"
            invalid_employees.append(emp_copy)
            continue
        if salary < 0:
            emp_copy["error"] = "Negative salary"
            invalid_employees.append(emp_copy)
            continue

        # Passed everything
        emp_copy["salary"] = salary
        valid_employees.append(emp_copy)
    
    return valid_employees, invalid_employees

valid, invalid = validate_employees(employees)


print(valid)
print(invalid)
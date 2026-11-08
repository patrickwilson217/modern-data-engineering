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
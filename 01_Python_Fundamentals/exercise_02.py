employees = [
    {"id": 101, "name": "John Smith", "department": "IT", "salary": 95000},
    {"id": 102, "name": "Jane Doe", "department": "Finance", "salary": 87000},
    {"id": 103, "name": "Bob Johnson", "department": "IT", "salary": 105000},
    {"id": 104, "name": "Sarah Williams", "department": "HR", "salary": 78000},
    {"id": 105, "name": "Mike Davis", "department": "IT", "salary": 92000}
]

# define a function called summarize_department that accepts a list of employee dictionaries and a department name as parameters.
#  The function should filter employees by the provided department, calculate average salary for that department
# and return a dictionary containing the department name, employee count, average salary, and a list of employees sorted by salary, highest first
# it should also handle the sitaution where department name contains no employees.  if there are no employees in the department, the function should return a dictionary with the department name, employee count as 0, average salary as none, and an empty list of employees.

def summarize_department(employees_list, department_name):
    # filter employees by department
    department_employees = [e for e in employees_list if e["department"] == department_name]

    # calculate average salary
    average_salary = sum(e["salary"] for e in department_employees) / len(department_employees) if department_employees else None

    # create a summary dictionary
    summary = {
        "department": department_name,
        "employee_count": len(department_employees),
        "average_salary": average_salary,
        "employees": sorted(
                        [
                            {
                                "id": e["id"],
                                "name": e["name"],
                                "salary": e["salary"]
                            } 
                            for e in department_employees
                        ],
                        key=lambda x: x["salary"],
                        reverse=True
                    )
    }

    return summary 

result = summarize_department(employees, "IT")
# result = summarize_department(employees, "Marketing") # Example with a department that has no employees
print(result)
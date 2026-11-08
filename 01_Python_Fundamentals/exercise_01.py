employees = [
    {"id": 101, "name": "John Smith", "department": "IT", "salary": 95000},
    {"id": 102, "name": "Jane Doe", "department": "Finance", "salary": 87000},
    {"id": 103, "name": "Bob Johnson", "department": "IT", "salary": 105000},
    {"id": 104, "name": "Sarah Williams", "department": "HR", "salary": 78000},
    {"id": 105, "name": "Mike Davis", "department": "IT", "salary": 92000}
]

#filter to IT department
it_employees = [e for e in employees if e["department"] == "IT"]

# average salary of IT employees
average_salary = sum(e["salary"] for e in it_employees) / len(it_employees) if it_employees else 0

# new list with only id, name, salary of IT employees
it_employee_summary = [
                        {
                            "id": e["id"], 
                            "name": e["name"], 
                            "salary": e["salary"]
                        } for e in it_employees
                    ]

# sort by salary, highest to lowest
it_employee_summary_sorted = sorted(it_employee_summary, key=lambda x: x["salary"], reverse=True)

# print results
print("IT Employees Summary (sorted by salary):")
for emp in it_employee_summary_sorted:
    print(f"ID: {emp['id']}, Name: {emp['name']}, Salary: ${emp['salary']:,.2f}")

print(f"\nAverage Salary of IT Employees: ${average_salary:,.2f}")
## Option 3: Create a Python scratch file

# This is particularly useful for our exercises.

# Inside `01_Python_Fundamentals`, create:

# ` scratch.py`

# You can use it to test small pieces of Python code without affecting your actual assignment.

# For example:

```python
employee = {"id": 103, "salary": None}

print(employee.get("salary"))

try:
    salary = int(employee["salary"])
except (ValueError, TypeError):
    print("Invalid salary value")



 # employees = []
    # try:
    #     employees = read_employees(file_path)

    #     valid_employees, invalid_employees = validate_employees(employees)

    #     # print(invalid_employees)

    #     # Write valid employees to a CSV file in the output directory
    #     valid_employees_file_path = output_dir / "valid_employees.csv"
    #     try:
    #         with open(valid_employees_file_path, "w", newline="", encoding="utf-8") as file:
    #             writer = csv.DictWriter(file, fieldnames=["id", "name", "department", "salary"])
    #             writer.writeheader()
    #             writer.writerows(valid_employees)
    #         print(f"Valid employees have been written to {valid_employees_file_path}.")
    #     except PermissionError:
    #         print(f"Error: Permission denied when trying to write to {valid_employees_file_path}.")
    #         sys.exit(1)
    #     # Write invalid employees to a CSV file in the output directory
    #     invalid_employees_file_path = output_dir / "invalid_employees.csv"
    #     try:
    #         with open(invalid_employees_file_path, "w", newline="", encoding="utf-8") as file:
    #             writer = csv.DictWriter(file, fieldnames=["id", "name", "department", "salary", "error"])
    #             writer.writeheader()
    #             writer.writerows(invalid_employees)
    #         print(f"Invalid employees have been written to {invalid_employees_file_path}.")
    #     except PermissionError:
    #         print(f"Error: Permission denied when trying to write to {invalid_employees_file_path}.")
    #         sys.exit(1) 

    #     # Write invalid employees to a JSON file in the output directory
    #     invalid_employees_json_file_path = output_dir / "invalid_employees.json"
    #     try:
    #         with open(invalid_employees_json_file_path, "w", encoding="utf-8") as file:
    #             json.dump(invalid_employees, file, indent=4)
    #         print(f"Invalid employees have been written to {invalid_employees_json_file_path}.")
    #     except OSError as exc:
    #         print(f"Error: {exc} when trying to write to {invalid_employees_json_file_path}.")
    #         sys.exit(1)
    # except FileNotFoundError:
    #     print(f"Error: The file {file_path} does not exist.")
    #     sys.exit(1)
    # except PermissionError:
    #     print(f"Error: Permission denied when trying to read the file {file_path}.")
    #     sys.exit(1)
    # except UnicodeDecodeError:
    #     print(f"Error: Failed to decode the file {file_path} as UTF-8.")
    #     sys.exit(1)




# Construct file paths

# employees = []
# try:
#     employees = read_employees(file_path)

#     valid_employees, invalid_employees = validate_employees(employees)

#     # print(invalid_employees)

#     # Write valid employees to a CSV file in the output directory
#     valid_employees_file_path = output_dir / "valid_employees.csv"
#     try:
#         with open(valid_employees_file_path, "w", newline="", encoding="utf-8") as file:
#             writer = csv.DictWriter(file, fieldnames=["id", "name", "department", "salary"])
#             writer.writeheader()
#             writer.writerows(valid_employees)
#         print(f"Valid employees have been written to {valid_employees_file_path}.")
#     except PermissionError:
#         print(f"Error: Permission denied when trying to write to {valid_employees_file_path}.")
#         sys.exit(1)
#     # Write invalid employees to a CSV file in the output directory
#     invalid_employees_file_path = output_dir / "invalid_employees.csv"
#     try:
#         with open(invalid_employees_file_path, "w", newline="", encoding="utf-8") as file:
#             writer = csv.DictWriter(file, fieldnames=["id", "name", "department", "salary", "error"])
#             writer.writeheader()
#             writer.writerows(invalid_employees)
#         print(f"Invalid employees have been written to {invalid_employees_file_path}.")
#     except PermissionError:
#         print(f"Error: Permission denied when trying to write to {invalid_employees_file_path}.")
#         sys.exit(1) 

#     # Write invalid employees to a JSON file in the output directory
#     invalid_employees_json_file_path = output_dir / "invalid_employees.json"
#     try:
#         with open(invalid_employees_json_file_path, "w", encoding="utf-8") as file:
#             json.dump(invalid_employees, file, indent=4)
#         print(f"Invalid employees have been written to {invalid_employees_json_file_path}.")
#     except OSError as exc:
#         print(f"Error: {exc} when trying to write to {invalid_employees_json_file_path}.")
#         sys.exit(1)

#     # Read invalid employees from the JSON file to verify the write operation
#     try:
#         with open(invalid_employees_json_file_path, "r", encoding="utf-8") as file:
#             read_invalid_employees = json.load(file)
#         print(f"Read {len(read_invalid_employees)} invalid employees from {invalid_employees_json_file_path}.")
#         if read_invalid_employees != invalid_employees:
#             print("Error: JSON output verification failed.")
#             sys.exit(1)
#     except json.JSONDecodeError as exc:
#         print(f"Error: Invalid JSON in {invalid_employees_json_file_path}: {exc}")
#         sys.exit(1)
#     except OSError as exc:
#         print(f"Error: {exc} when trying to read from {invalid_employees_json_file_path}.")
#         sys.exit(1)
           
# except FileNotFoundError:
#     print(f"Error: The file {file_path} does not exist.")
#     sys.exit(1)
# except PermissionError:
#     print(f"Error: Permission denied when trying to read the file {file_path}.")
#     sys.exit(1)
# except UnicodeDecodeError:
#     print(f"Error: The file {file_path} is not in a valid encoding format.")
#     sys.exit(1)

# print("CSV ingestion completed successfully.")
# print(f"Total employee records loaded: {len(employees)}.")
# print("Validation Results")
# print("------------------")
# print(f"Valid records: {len(valid_employees)}")
# print(f"Invalid records: {len(invalid_employees)}")
# print("Output Results")
# print("------------------")
# # add print statement to read "Successfully wrote N records to valid_employees_file_path"
# print(f"Successfully wrote {len(valid_employees)} records to {valid_employees_file_path}")
# print(f"Successfully wrote {len(invalid_employees)} records to {invalid_employees_file_path}")
# print(f"Successfully wrote {len(invalid_employees)} records to {invalid_employees_json_file_path}")
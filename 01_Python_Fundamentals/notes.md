# Python Training Notes

## Exercise 3 - Error Handling

### Things to remember
- Use try/except to catch errors.
- Use dict.get() to retrieve dictionary values safely.
- Use isinstance() to check data types.

### Code Examples

```python
try:
    salary = int(employee["salary"])
except (ValueError, TypeError):
    print("Invalid salary")


[1, 2, 3]          # list
{"a": 1, "b": 2}   # dictionary (key: value pairs)
{1, 2, 3}          # set (no colons)
{}                 # empty dictionary, not an empty set; use set() for that

# list of dictionaries
employees = [
    {"id": 101, "name": "John Smith", "department": "IT", "salary": 95000},
    {"id": 102, "name": "Jane Doe", "department": "Finance", "salary": 87000},
    {"id": 103, "name": "Bob Johnson", "department": "IT", "salary": None},
    {"id": 104, "name": "Sarah Williams", "department": "HR", "salary": 78000},
    {"id": 105, "name": "Mike Davis", "department": "IT", "salary": "92000"},
    {"id": 106, "name": "Tom Brown", "department": "IT"},
    {"id": 107, "name": "Lisa White", "department": "IT", "salary": -5000},
    {"id": 108, "name": "Chris Green", "department": "IT", "salary": 110000}
]

And ( ) is a tuple, like (1, 2, 3). A tuple is basically a list you can’t change.

# create a copy of provided data.  important to do before making modifications via validation 
emp_copy = employee.copy()

# original data
{"id": 105, "salary": "92000"}

# after validation and cleaning
{"id": 105, "salary": 92000}

# This is an important principle in ETL development: preserve raw source data while creating validated, transformed records.

# One technical distinction: .copy() creates a shallow copy. That's sufficient for our current dataset because the dictionary values are simple types. With nested dictionaries or lists, we'd need to consider whether a deeper copy is necessary.

# separating valid and invalid records
return valid_employees, invalid_employees

# this is a good design.  returning two collections that downstream processes can handle independently

# example
valid, invalid = validate_employees(employees)

# A production pipeline might then write the valid records to a Silver Delta table and the invalid records to a quarantine table for investigation.

# This pattern is commonly called data quality quarantine.

# Remember the distinction:
# Operation	File	String
# Serialize	json.dump()	json.dumps()
# Deserialize	json.load()	json.loads()


# These four functions are worth remembering because you'll encounter them frequently when working with APIs and configuration files.


# 2. Understanding Python Logging Levels

# Python provides five standard logging levels you'll use regularly.
# Level	Numeric value	Purpose	Data engineering example
# DEBUG	10	Detailed diagnostic information	Processing employee ID 105
# INFO	20	Normal operational events	Successfully loaded 11 records
# WARNING	30	Unexpected but recoverable conditions	Six records failed validation
# ERROR	40	An operation failed	Unable to write output file
# CRITICAL	50	Severe application failure	Required configuration unavailable

# format="%(asctime)s | %(levelname)s | %(message)s"

# Placeholder	Description

# %(asctime)s	Timestamp
# %(levelname)s	Logging severity
# %(message)s	Your message
# %(name)s	Logger name
# %(filename)s	Python source filename
# %(lineno)d	Line number
# %(funcName)s	Function that generated the message

# import logging
# from pathlib import Path

# log_dir = Path("logs")
# log_dir.mkdir(exist_ok=True)


# configured two handlers
# FileHandler - writes messages to a file
# StreamHandler -  writes messages to console

# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s | %(levelname)s | %(message)s",
#     handlers=[
#         logging.FileHandler(log_dir / "pipeline.log", encoding="utf-8"),
#         logging.StreamHandler()
#     ]
# )

# logger = logging.getLogger(__name__)

# logger.info("Pipeline started")
# logger.info("Reading source data")
# logger.warning("Some records failed validation")
# logger.info("Pipeline completed")

# | Method | Behavior |
# |---|---|
# | `logger.error()` | Logs an error message |
# | `logger.exception()` | Logs an error message plus the exception traceback |

# In Python logging, %s is a placeholder for a string representation, while %d is a placeholder for an integer.

# when it comes to logging...
# use this:
# logger.info("Loaded %d records", len(employees))

# instead of this:
# logger.info(f"Loaded {len(employees)} records")



# Tests

# Run All Tests
python -m pytest -v

# Run All Tests in One File
python -m pytest tests/test_file_operations.py -v

# Run One Specific Test Function
python -m pytest tests/test_file_operations.py::test_write_csv -v

# Run One specific parameterized test case
python -m pytest "tests/test_employee_validation_parameterized.py::test_invalid_salary_values[negative-integer]" -v

# Run Tests matching a keyword (-k) - you can use and, or, not in these commands
python -m pytest -k "salary and not negative" -v

# Run multiple specific test files
python -m pytest tests/test_file_operations.py tests/test_exceptions.py -v

# Stop testing after the first failure
python -m pytest -x -v

# Rerun only tests that failed previously
python -m pytest --lf -v


GIT commands while inside the pager:
| Key | Action |
|---|---|
| `Q` | Quit and return to PowerShell |
| `Space` | Move forward one page |
| `B` | Move backward one page |
| `↑` / `↓` | Scroll one line |
| `/text` | Search for text |

prevent git from opening the pager
git --no-pager diff --cached --stat


common commit message conventions:
| Prefix | Purpose |
|---|---|
| `feat:` | New functionality |
| `fix:` | Bug fix |
| `docs:` | Documentation changes |
| `test:` | Adding or modifying tests |
| `refactor:` | Code restructuring without changing behavior |
| `chore:` | Maintenance tasks |
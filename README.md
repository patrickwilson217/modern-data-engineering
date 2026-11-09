# Modern Data Engineering Career Transition

This repository documents my ongoing development of modern cloud and distributed data engineering skills, building on more than 25 years of professional experience in database development, enterprise data integration, and data architecture.

My professional background includes SQL Server development and administration, enterprise data warehousing, ETL development, Python scripting, and orchestration of production data pipelines.

Through hands-on projects, I'm expanding that experience into technologies such as PySpark, Azure Databricks, Delta Lake, and modern cloud-based data engineering architectures.

## Technologies

**Current project:**
- Python 3.12
- pytest
- Git / GitHub
- VS Code

**Professional experience:**
- SQL Server and T-SQL
- PostgreSQL
- Enterprise ETL and data integration
- Data warehousing
- Python scripting
- Azure infrastructure

## Python ETL Pipeline

The current project demonstrates a Python-based ETL pipeline that reads employee records from a CSV file, validates employee and salary data, separates valid and invalid records, and writes the results to CSV and JSON files.

The pipeline incorporates structured logging, exception handling, reusable functions, and automated testing.

### Features

- CSV data ingestion
- Employee record validation
- Salary data type conversion and validation
- Separation of valid and invalid records
- CSV and JSON output generation
- Exception handling
- Execution logging
- Automated testing with pytest

### Project Structure

```text
DataEngineering/
├── README.md
├── .gitignore
├── pytest.ini
└── 01_Python_Fundamentals/
    ├── exercise_01.py
    ├── exercise_02.py
    ├── exercise_03.py
    └── exercise_04/
        ├── employee_etl.py
        ├── employee_validation.py
        ├── employees.csv
        └── tests/
            ├── test_employee_validation.py
            ├── test_employee_validation_parameterized.py
            ├── test_exceptions.py
            └── test_file_operations.py
```

## Automated Testing

The project includes **31 passing automated tests** using pytest.

Tests cover:

- Employee validation rules
- Parameterized salary validation scenarios
- Exception handling
- CSV and JSON file operations
- Input data integrity

The test suite uses temporary files and directories to validate file operations without modifying production or sample input data.

## Running the Project

### 1. Prerequisites

- Python 3.12
- pip

### 2. Environment Setup

From the repository root, create a virtual environment:

```powershell
python -m venv .venv
```

Activate the environment (Windows PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

Install pytest:

```powershell
python -m pip install pytest
```

### 3. Run the ETL Pipeline

From the repository root:

```powershell
python 01_Python_Fundamentals/exercise_04/employee_etl.py
```

The pipeline reads the sample employee data, validates the records, and generates CSV and JSON output files.

### 4. Run Automated Tests

From the repository root:

```powershell
python -m pytest -v
```

The pytest configuration allows all tests to execute without manually modifying Python import paths.

**Current status: 31 tests passing.**

## Learning Roadmap

Planned additions to this repository include:

- **PySpark:** Distributed data processing
- **Azure Data Lake Storage:** Cloud-based data storage
- **Azure Data Factory:** Data pipeline orchestration
- **Azure Databricks:** Spark-based data transformations
- **Delta Lake:** Reliable, versioned data tables
- **Data Quality:** Expanded validation and monitoring
- **CI/CD:** Automated testing and deployment workflows

The goal is to progressively build end-to-end data engineering solutions that combine established database engineering practices with modern cloud and distributed technologies.
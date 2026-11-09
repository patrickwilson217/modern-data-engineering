**# Modern Data Engineering Career Transition**

This repository documents my transition from traditional SQL Server-based data engineering into modern cloud and distributed data engineering.

Building on my experience with SQL Server, stored procedures, SQL Agent, Python, and third-party orchestration tools, I'm developing hands-on skills in PySpark, Azure, Databricks, and modern data engineering practices.

## Technologies

Technologies used in the current project

- Python 3.12
- SQL Server
- pytest
- Git/GitHub
- VS Code

## Python ETL Pipeline

**The Python ETL pipeline reads employee records from a CSV file, validates salary data, separates valid and invalid records, and writes the results to CSV and JSON files. The pipeline includes exception handling, execution logging, and automated testing.**



- CSV Ingestion
- Employee Data validation
- Invalid record handling
- JSON and CSV output
- Logging
- Exception handling

## Automated Testing

I'm using pytest to test validation logic, exception handling, and file operations
I've currently authored 31 passing tests covering the following areas:
- Employee validtion rules
- Parameterized salary validation
- Exception handling
- CSV and JSON file operations
- Input data integrity

## Running the Project

**1. Prerequisites**
- Python 3.12
- pytest

**2. Environment setup**

   Create and activate virtual environment and install pytest

- `python -m venv .venv`

- `.\.venv\Scripts\Activate.ps1`

- `python -m pip install pytest`

**3. Run the ETL pipeline**

- `cd 01_Python_Fundamentals\exercise_04`
- `python exercise_04a.py`

**4. Running automated tests** 

- `python -m pytest -v`

## Learning Roadmap

Planned additions to this project:

- **PySpark** for distributed data processing
- **Azure Data Lake Storage** for cloud storage
- **Azure Data Factory** for pipeline orchestration
- **Azure Databricks** for Spark-based transformation
- **Delta Lake** for reliable, versioned tables
- **Data quality checks** and orchestration
- **CI/CD** for automated testing and deployment
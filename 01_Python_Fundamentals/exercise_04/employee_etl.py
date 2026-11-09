import csv
import json
from logging.handlers import RotatingFileHandler
import sys
import logging
import time
from pathlib import Path

from employee_validation import validate_employees


# Determine the directory containing this Python script
BASE_PATH = Path(__file__).parent


def read_employees(file_path: str | Path) -> list[dict]:
    """Read employees from a CSV file and return a list of dictionaries.

    Args:
        file_path (str or Path): The path to the CSV file.

    Returns:
        list[dict]: A list of dictionaries representing the employees.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If there is a permission error reading the file.
        UnicodeDecodeError: If there is an error decoding the file as UTF-8.
    """
    employees = []
    
    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            employee = {
                "id": row["id"],
                "name": row["name"],
                "department": row["department"],
                "salary": row["salary"]
            }
            employees.append(employee)
   
    return employees


def write_csv(file_path: str | Path, records: list[dict], fieldnames: list[str]) -> None:
    """Write records to a CSV file with the specified field names.

    Args:
        file_path (str or Path): The path to the CSV file.
        records (list[dict]): The list of records to write.
        fieldnames (list[str]): The list of field names for the CSV header.

    Raises:
        PermissionError: If there is a permission error writing to the file.
        UnicodeEncodeError: If there is an error encoding the data as UTF-8.
    """
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)
    
    


def write_json(file_path: str | Path, records: list[dict]) -> None:
    """Write records to a JSON file with indentation.

    Args:
        file_path (str or Path): The path to the JSON file.
        records (list[dict]): The list of records to write.

    Raises:
        PermissionError: If there is a permission error writing to the file.
        UnicodeEncodeError: If there is an error encoding the data as UTF-8.
    """
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=4)
    
   

def verify_json(file_path: str | Path, expected_records: list[dict]) -> bool:
    """Verify that the JSON file contains the expected records.

    Args:
        file_path (str or Path): The path to the JSON file.
        expected_records (list[dict]): The expected list of records.

    Returns:
        bool: True if the actual records match the expected records, False otherwise.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If there is a permission error reading the file.
        UnicodeDecodeError: If there is an error decoding the file as UTF-8.
        json.JSONDecodeError: If there is an error decoding the JSON content.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        actual_records = json.load(file)
    return actual_records == expected_records

def make_directory(dir_path: str | Path) -> None:
    """Create a directory if it does not exist.

    Args:
        dir_path (str or Path): The path to the directory to create.

    Raises:
        PermissionError: If there is a permission error creating the directory.
        OSError: If there is an error creating the directory.
    """
    Path(dir_path).mkdir(parents=True, exist_ok=True)

def configure_logging(log_dir: str | Path) -> logging.Logger:
    """Configure logging to write to a file and the console.

    Args:
        log_dir (str or Path): The directory where the log file will be stored.
    """
    log_dir = Path(log_dir)
    log_dir.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            RotatingFileHandler(log_dir / "pipeline.log", maxBytes=1_000_000, backupCount=3, encoding="utf-8"),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)


def main(logger: logging.Logger) -> None:
    """Main function to run the CSV ingestion, validation, and output process."""
    
    start_time = time.perf_counter()
    logger.info("ETL pipeline started")

    
    # Construct the path to the CSV file
    file_path = BASE_PATH / "employees.csv"
    # Construct the path to the fake CSV file
    # file_path = BASE_PATH / "employees_backup.csv"

    # Try to construct the output directory        
    output_dir = BASE_PATH / "output"
    make_directory(output_dir)
    

    # call read_employees function to read the CSV file
    employees = read_employees(file_path)
    logger.info("Source CSV successfully loaded from %s", file_path)

    # call validate_employees function to validate the employees
    # only write the warning if at least one invalid employee record exists
    valid_employees, invalid_employees = validate_employees(employees)
    logger.info("Validation completed. Valid employee records: %d, Invalid records: %d", len(valid_employees), len(invalid_employees))
    invalid_employees_count = len(invalid_employees)
    rejection_rate = invalid_employees_count / len(employees) if employees else 0
    
    if invalid_employees:
        logger.warning("Rejected %d employee records", invalid_employees_count)
    
    logger.info("Rejection rate: %.2f%%", rejection_rate * 100)

    # call write_csv for valid_employees
    valid_employees_file_path = output_dir / "valid_employees.csv"
    valid_fields = ["id", "name", "department", "salary"]
    write_csv(valid_employees_file_path, valid_employees, valid_fields)
    logger.info("Valid CSV file successfully written. Wrote %d records to %s", len(valid_employees), valid_employees_file_path)

    # call write_csv for invalid_employees
    invalid_employees_file_path = output_dir / "invalid_employees.csv"
    invalid_fields = ["id", "name", "department", "salary", "error"]
    write_csv(invalid_employees_file_path, invalid_employees, invalid_fields)
    logger.info("Invalid CSV file successfully written. Wrote %d records to %s", len(invalid_employees), invalid_employees_file_path)

    # call write_json for invalid_employees
    invalid_employees_json_file_path = output_dir / "invalid_employees.json"
    write_json(invalid_employees_json_file_path, invalid_employees)
    logger.info("Invalid JSON file successfully written. Wrote %d records to %s", len(invalid_employees), invalid_employees_json_file_path)

    # call verify_json, check if verification is successful, raise a runtime error if it fails
    json_verification = verify_json(invalid_employees_json_file_path, invalid_employees)
    if not json_verification:
        raise RuntimeError("JSON verification failed.")

    logger.info("JSON verification passed.")

    logger.info("Pipeline completed successfully.")
    elapsed_seconds = time.perf_counter() - start_time
    logger.info("Total execution time: %.2f seconds", elapsed_seconds)
    logger.info("Pipeline Summary: Total=%d, Valid=%d, Invalid=%d, Rejection Rate=%.2f%%, Duration=%.2f seconds", len(employees), len(valid_employees), invalid_employees_count, rejection_rate * 100, elapsed_seconds)
    


   
if __name__ == "__main__":
    logging_dir = BASE_PATH / "logs"
    logger = None

    
    try:
        logger = configure_logging(logging_dir)
        main(logger)
    except Exception:
        if logger is not None:
            logger.exception("ETL pipeline failed")
        else:
            logging.exception("ETL pipeline failed during logging initialization")
    
    sys.exit(1)
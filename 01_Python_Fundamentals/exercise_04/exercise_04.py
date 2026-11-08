import csv
from pathlib import Path

# Determine the directory containing this Python script
base_path = Path(__file__).parent

# Construct the path to the CSV file
file_path = base_path / "employees.csv"

# Open and read the CSV file
with open(file_path, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
from pyspark.sql import SparkSession
from pyspark.sql.types import (
        StructType,
        StructField,
        IntegerType,
        StringType  
    )

def main():
    spark = (
        SparkSession.builder
        .appName("EmployeeDataFrameExercise")
        .master("local[*]")
        .getOrCreate()
    )


    try:
        spark.sparkContext.setLogLevel("ERROR")

        # Your exercise code goes here
        employees = [
            (101, "Alice", "IT", 95000),
            (102, "Bob", "Finance", 72000),
            (103, "Charlie", "IT", 88000),
            (104, "Diana", "HR", 65000),
            (105, "Ethan", "Finance", 81000),
            (106, "Fiona", "IT", 105000),
            (107, "George", "HR", 59000),
            (108, "Hannah", "Finance", 92000),
        ]

        # define the schema for the employee dataframe
        employee_schema = StructType([
            StructField("id", IntegerType(), nullable=False),
            StructField("name", StringType(), nullable=False),
            StructField("department", StringType(), nullable=False),
            StructField("salary", IntegerType(), nullable=False)
        ])
        
        employee_df = spark.createDataFrame(employees, employee_schema)
      
        print("Original employee dataframe schema")
        employee_df.printSchema()

        invalid_employee = [
            (109, "Invalid Employee", "IT", None)
        ]

        # attempt to create a dataframe using explicit schema using invalid_employee
        try:
            invalid_employee_df = spark.createDataFrame(invalid_employee, employee_schema)
        except Exception as e:
            print(f"Exeption type: {type(e).__name__}")
            print(f"Exception message: {e}")


    finally:
        spark.stop()
    

if __name__ == "__main__":
    main()
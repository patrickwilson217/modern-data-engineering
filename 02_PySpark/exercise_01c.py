from pyspark.sql import SparkSession
from pyspark.sql.types import (
        StructType,
        StructField,
        IntegerType,
        StringType  
    )
from pyspark.sql.functions import (
    count,
    avg,
    max,
    min,
    desc
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

        employee_df.createOrReplaceTempView("employees")

        # Example query using the temporary view
        result_df = spark.sql("""
            SELECT 
                department,
                COUNT(*) AS employee_count,
                AVG(salary) AS average_salary,
                MAX(salary) AS max_salary,
                MIN(salary) AS min_salary
            FROM employees
            GROUP BY department
            ORDER BY average_salary DESC
        """)
        result_df.show()

        filter_df = spark.sql("""
            SELECT 
                name as employee_name,
                department,
                salary
            FROM employees
            WHERE salary > 80000
            ORDER BY salary DESC
        """)
        filter_df.show()

        # recreate result_df using DataFrame API
        result_df_api = (
            employee_df
            .groupBy("department")
            .agg(
                count("*").alias("employee_count"),
                avg("salary").alias("average_salary"),
                max("salary").alias("max_salary"),
                min("salary").alias("min_salary")
            )
            .orderBy(desc("average_salary"))
        )
        result_df_api.show()

    finally:
        spark.stop()

if __name__ == "__main__":
    main()
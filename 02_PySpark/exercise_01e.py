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

        print(f"Original partitions: {employee_df.rdd.getNumPartitions()}")

        repartitioned_df = employee_df.repartition(4)
        print(f"Repartitioned partitions: {repartitioned_df.rdd.getNumPartitions()}")

        repartitioned_df.explain(mode="formatted")

        coalesced_df = repartitioned_df.coalesce(2)
        print(f"Coalesced partitions: {coalesced_df.rdd.getNumPartitions()}")
        coalesced_df.explain(mode="formatted")

        
    finally:
        spark.stop()

if __name__ == "__main__":
    main()
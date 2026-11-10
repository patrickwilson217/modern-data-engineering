from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent
OUTPUT_PATH = BASE_PATH/ "output" / "employees"
COALESCED_OUTPUT_PATH = BASE_PATH / "output" / "employees_single"


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

   
        
        employees_df = spark.createDataFrame(employees, employee_schema)


        employees_df.write.mode("overwrite").parquet(str(OUTPUT_PATH))
      
        employees_parquet_df = spark.read.parquet(str(OUTPUT_PATH))
        employees_parquet_df.show()
        #print schema of the parquet dataframe
        employees_parquet_df.printSchema()
        #print the number of rows in the parquet dataframe
        print(f"Number of rows: {employees_parquet_df.count()}")

        #compare employees_df schema with employees_parquet_df schema
        print("Original employee dataframe schema")
        employees_df.printSchema()
        print("Parquet employee dataframe schema")
        employees_parquet_df.printSchema()

        #use pathlib tolist the files created inside parquet output directory
        print("Files created inside parquet output directory:")
        for file in Path(OUTPUT_PATH).iterdir():
            print(file)

        employees_coalesced_df = employees_df.coalesce(1)

        #list the files created inside coalesced parquet output directory
        print("Files created inside coalesced parquet output directory:")
        for file in Path(COALESCED_OUTPUT_PATH).iterdir():
            print(file) 
        
        employees_coalesced_df.write.mode("overwrite").parquet(str(COALESCED_OUTPUT_PATH))

        parquet_files = list(COALESCED_OUTPUT_PATH.glob("*.parquet"))
        print(f"Number of Parquet files: {len(parquet_files)}")




    finally:
        spark.stop()
    

if __name__ == "__main__":
    main()
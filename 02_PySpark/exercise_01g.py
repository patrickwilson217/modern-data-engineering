from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent
OUTPUT_PATH = BASE_PATH.parent/ "output" / "exercise_01g"
INPUT_PATH = BASE_PATH / "data" 


from pyspark.sql import SparkSession, DataFrame, functions as F
from pyspark.sql.types import StructType, StructField, StringType, IntegerType


def create_spark_session(session_name: str) -> SparkSession:
    
    return SparkSession.builder.appName(session_name).getOrCreate()

def read_csv_input(
            spark: SparkSession,
            input_path: str, 
            schema: StructType
            ) -> DataFrame:
    return spark.read.csv(input_path, header=True, schema=schema)

def validate_employees(employee_df: DataFrame) -> tuple[DataFrame, DataFrame]:
    """
    Validates the employee DataFrame based on a set of rules.
    Adds a 'validation_result' column ("Valid"/"Invalid") and a 'rejection_reason' column
    (comma-separated list of failures, null when valid).
    Returns two DataFrames: one for valid employees and one for invalid employees.
    
    """

    def is_blank(col_name: str):
        return F.col(col_name).isNull() | (F.trim(F.col(col_name)) == "")

    salary_num = F.col("salary").cast("double")

    salary_missing = is_blank("salary")

    salary_not_numeric = (
        ~salary_missing 
        & salary_num.isNull() 
    )


    salary_not_finite = (
       F.isnan(salary_num)
       | (salary_num == float("inf"))
       | (salary_num == float("-inf"))
    )

    salary_is_finite = (
        ~salary_missing 
        & ~salary_not_numeric
        & ~salary_not_finite
    )

    # (failure condition, message)
    rules = [
        (F.col("employee_id").isNull(),                                         "employee_id is null"),
        (is_blank("name"),                                                      "name is null or empty"),
        (is_blank("department"),                                                "department is null or empty"),
        (salary_missing,                                                        "salary is null or empty"),
        (salary_not_numeric,                                                    "salary is not numeric"),
        (salary_not_finite,                                                     "salary must be finite"),
        (salary_is_finite & (salary_num <= 0),                                  "salary must be positive"),
        (salary_is_finite & (salary_num != F.floor(salary_num)),                "salary must be an integer"),
        (salary_is_finite & (salary_num > 2147483647),                          "salary exceeds supported range")
    ]

    # concat_ws skips nulls, so only failed rules contribute; all pass -> ""
    reasons = F.concat_ws(", ", *[F.when(cond, msg) for cond, msg in rules])

    validated_df = (
        employee_df
        .withColumn("validation_result", F.when(reasons == "", "Valid").otherwise("Invalid"))
        .withColumn("rejection_reason", F.when(reasons != "", reasons))
    )
    valid_df = validated_df.filter(F.col("validation_result") == "Valid")
    # valid_df.explain(mode="formatted")
    invalid_df = validated_df.filter(F.col("validation_result") == "Invalid")
    # invalid_df.explain(mode="formatted")
    return valid_df, invalid_df

def transform_employees(valid_employee_df: DataFrame) -> DataFrame:
    """
    Transforms only valid employees, there's no need to check if is valid.
    Cast salary to integer and assign a salary_band for valid employees only.
    Returns only valid employees; invalid rows are not included.


    Salary bands:
        < 75,000          -> "Low"
        75,000 - 99,999   -> "Medium"
        >= 100,000        -> "High"
    """
    salary_int = F.col("salary").cast("integer")

    salary_band = (
        F.when(salary_int < 75000, "Low")
         .when(salary_int < 100000, "Medium")
         .otherwise("High")
    )

    return (
        valid_employee_df
        .withColumn("salary_band", salary_band)
        .withColumn("salary", salary_int)
    )


def write_outputs(
        df: DataFrame,
        output_path: str
) -> None:
    """
    Writes the given DataFrame to the specified output path in Parquet format.
    Uses overwrite mode to ensure the pipeline can be re-run without errors.
    Preserves the existing schema of the DataFrame.
    """ 
    df.write.mode("overwrite").parquet(output_path)
    
    

    
    

def calculate_pipeline_metrics(source_df: DataFrame, valid_df: DataFrame, invalid_df: DataFrame) -> dict:
    """
    Calculates pipeline metrics including total records, valid records, invalid records, and the ratio of valid to total records.
    Returns a dictionary with the following keys:
        - total_records
        - valid_records
        - invalid_records
        - valid_ratio
    """
    total_records = source_df.count()
    valid_records = valid_df.count()
    invalid_records = invalid_df.count()
    valid_ratio = valid_records / total_records if total_records > 0 else 0.0


    return {
        "source_records": total_records,
        "valid_records": valid_records,
        "invalid_records": invalid_records,
        "valid_ratio": valid_ratio,
        "reconciliation": "PASSED" if valid_records + invalid_records == total_records else "FAILED"
    }   



def main():
    spark = create_spark_session("employee_etl_spark")

    try:
        # Your main logic here
        # define the schema for the employee dataframe
        
        employee_schema = StructType([
            StructField("employee_id", IntegerType(), True),
            StructField("name", StringType(), True),
            StructField("department", StringType(), True),
            StructField("salary", StringType(), True)
        ])

        employee_df = read_csv_input(spark, str(INPUT_PATH / "employees.csv"), employee_schema)
        valid_employee_df, invalid_employee_df = validate_employees(employee_df)
        
        valid_employee_df = transform_employees(valid_employee_df)

        # valid_employee_df should only include columns employee_id, name, department, salary, salary_band
        valid_employee_df = valid_employee_df.select("employee_id", "name", "department", "salary", "salary_band")
        valid_employee_df.show()

        # invalid_employee_df should only include columns employee_id, name, department, salary, rejection_reason
        invalid_employee_df = invalid_employee_df.select("employee_id", "name", "department", "salary", "rejection_reason")
        invalid_employee_df.show()

        valid_employee_df.printSchema()

        pipeline_metrics = calculate_pipeline_metrics(employee_df, valid_employee_df, invalid_employee_df)

        if pipeline_metrics["reconciliation"] == "FAILED":
           
            raise ValueError(f"Record reconciliation failed: source={pipeline_metrics['source_records']}, valid={pipeline_metrics['valid_records']}, invalid={pipeline_metrics['invalid_records']}")
       

        write_outputs(valid_employee_df, str(OUTPUT_PATH / "valid_employees"))
        write_outputs(invalid_employee_df, str(OUTPUT_PATH / "invalid_employees"))

        #display pipeline execution summary
        print("Pipeline Execution Summary")
        print("-----------------------------------------")
        print(f"Source Records: {pipeline_metrics['source_records']}")
        print(f"Valid Records: {pipeline_metrics['valid_records']}")
        print(f"Invalid Records: {pipeline_metrics['invalid_records']}")
        print(f"Valid Ratio: {pipeline_metrics['valid_records'] / pipeline_metrics['source_records'] * 100:.2f}%")
        print(f"Reconciliation: {pipeline_metrics['reconciliation']}")
            
      
    finally:
        spark.stop()

    

if __name__ == "__main__":
    main()
from pyspark.sql import SparkSession


def main():
    spark = (
        SparkSession.builder
        .appName("FirstPySparkApplication")
        .master("local[*]")
        .getOrCreate()
    )

    print(f"Spark version: {spark.version}")
    
    spark.stop()

if __name__ == "__main__":
    main()
from pyspark.sql import SparkSession
from pyspark.sql.functions import desc



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
        
        employee_df = spark.createDataFrame(employees, ["id", "name", "department", "salary"])
        print("Original employee DataFrame")
        employee_df.show()

        employee_df.printSchema()

        filtered_employees_df = employee_df.filter(employee_df["salary"] > 80000)
        print("Employees making more than 80000")
        filtered_employees_df.show()

        # from filtered_employees_df select specific columns name, department, salary
        selected_columns_df = filtered_employees_df.select("name", "department", "salary")
        print("Selected columns from employees making more than 80000")
        selected_columns_df.show()

        # sort filtered_employees_df by salary in descending order
        print("Filtered employees sorted by salary in descending order")
        sorted_employees_df = filtered_employees_df.orderBy(desc("salary"))
        sorted_employees_df.show()

        # count the total number of employees
        total_employees_count = employee_df.count()
        print(f"Total number of employees: {total_employees_count}")

        pass
    finally:
        spark.stop()
    

if __name__ == "__main__":
    main()
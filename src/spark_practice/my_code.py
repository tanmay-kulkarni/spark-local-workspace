from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, count

def main():
    # Initialize Spark session
    spark: SparkSession = SparkSession.builder \
        .appName("CSVProcessing") \
        .master("local[*]") \
        .getOrCreate()

    # Read CSV file
    df = spark.read \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .csv("/app/data/data.csv")

    # Perform aggregations
    agg_results = df.select(
        count("*").alias("total_records"),
        avg("age").alias("average_age")
    ).collect()

    # Group by age and count
    age_distribution = df.groupBy("age") \
        .count() \
        .orderBy("age") \
        .collect()

    # Print results
    print("\nHere are the Aggregation Results:")
    print(f"Total Records: {agg_results[0]['total_records']}")
    print(f"Average Age: {agg_results[0]['average_age']:.2f}")

    print("\nAge Distribution:")
    age_df = spark.createDataFrame(age_distribution)
    age_df.show()

    # Stop Spark session
    spark.stop()

if __name__ == "__main__":
    main()

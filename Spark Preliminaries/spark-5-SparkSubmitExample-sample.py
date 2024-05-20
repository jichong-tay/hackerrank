# importing packages
import pyspark
from pyspark.sql import SparkSession

# Spark Preliminaries: Spark Submit Example


def main():
    spark = SparkSession.builder.appName("Spark Preliminaries").getOrCreate()
    columns = ["Name", "Age"]
    data = [("Hari", "23"), ("Sree", "22"), ("Subi", "30"), ("Alex", "47")]
    rdd = spark.createDataFrame(data, columns)
    rdd.coalesce(1).write.parquet("/projects/challenge/Data")


if __name__ == "__main__":
    main()

1. Spark Preliminaries: RDD Creation

#Steps to complete the Handson:

1. Click on Terminal --> New to open the terminal.
2. Use spark-shell to solve this challenge
3. Install all the necessary dependencies

In this hands-on, you will create a RDD using basic methods.

##Steps:
Step 1: Enter the spark shell and Import all required SparkSession packages.
Step 2: Create a SparkSession object.
Step 3: Create an Array of integers 'data' = [1,2,3,4,5].
Step 4: Create a RDD named as 'rdd' from the given data.
Step 5: Now, store the rdd data into a text file named as rdd in a single partition. [hint: coalesce(1).saveAsTextFile()]

Click on RUN TESTS for validation and SUBMIT button for Submission.

##Git Instructions
Use the following commands to work with this project.

Run

```
echo done
```

Test

```
bash score.sh
```

Install

```
echo "installation is not required for this challenge."
```

====================================================

##Solutions
Reference:
https://spark.apache.org/docs/latest/quick-start.html
https://sparkbyexamples.com/spark/sparksession-explained-with-examples/

Scala Approach
Step 1:
To enter spark shell

```
spark-shell
```

Step 2,3,4 (run line by line)
run the command in the terminal:

```
import org.apache.spark.sql.SparkSession
val spark = SparkSession.builder.appName("Spark1").master("local[*]").getOrCreate()
val data = Array(1, 2, 3, 4, 5)
val rdd = spark.sparkContext.parallelize(data)
rdd.coalesce(1).saveAsTextFile("rdd")
```

Python Approach
Step 1:
To enter spark shell

```
pyshark
```

Step 2,3,4 (run line by line)
run the command in the terminal:

```
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Spark1").master("local[*]").getOrCreate()
data = [1, 2, 3, 4, 5]
rdd = spark.sparkContext.parallelize(data)
rdd.coalesce(1).saveAsTextFile("rdd")
```

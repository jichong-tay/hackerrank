1. Spark Preliminaries: Create DataFrames and SQL Operations

#Steps to complete the Handson:

1. Click on Terminal --> New to open the terminal.
2. Install all the necessary dependencies using the INSTALL option from the Project Menu.

In this hands-on, you will start working on Spark SQL Data Set.
Follow the below instructions to complete the hands-on:

Note: Use spark-shell to solve this challenge.

##Steps:
Step 1: Create a json file called "Students.json" using the command `vim Students.json` in the terminal, and then copy the following data to the file.

{"name":"Ben","age":"23"}
{"name":"Alen","age":"22"}
{"name":"Jonny","age":"25"}
{"name":"Steve","age":"27"}
{"name":"Stark","age":"21"}

Step 2: Enter into spark-shell and import all the required Spark packages.
Step 3: Create a SparkSession object as 'spark'.
Step 4: Create an 'sqlContext' from the 'SparkContext sc'
Step 5: Read the 'json' file using the 'sqlContext' created..
Step 6: Display the results to 'stdout'.
Step 7: Register a Temporary Table students
Step 8: Run the QL query to display details under the age of 25.
Step 9: And, Store the values in the csv file named as 'result' as a single partiion with header. [hint:coalesce(1).write.csv()]

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
Bash Score Script

```
#!/bin/bash
SCORE=0
PASS=0
TOTAL_TESTS=7

if [ -e /projects/challenge/Students.json ]
  then PASS=$((PASS+1));
fi;

if  (( $(grep -i "import org.apache.spark.sql.SparkSession" /home/user/.scala_history | wc -l) >=1 ))
  then PASS=$((PASS+1));
fi;

if (( $(grep -i "sqlContext" /home/user/.scala_history |wc -l) >=1 ))
  then PASS=$((PASS+1));
fi;

if (( $(grep -i "registerTempTable\|createOrReplaceTempView" /home/user/.scala_history | wc -l ) >=1 ))
   then PASS=$((PASS+1));
fi;

if (( $(grep -i "sql" /home/user/.scala_history | wc -l ) >=1 ))
   then PASS=$((PASS+1));
fi;

if (( $(ls /projects/challenge/result | grep -io -e "_SUCCESS" | wc -l) ==1 ))
  then PASS=$((PASS+1));
fi;

if (( $(cat /projects/challenge/result/part* | grep -io -e "age,name" -e "23,Ben" -e "22,Alen" -e "21,Stark" | wc -l) ==4))
  then PASS=$((PASS+1));
fi;

echo "TESTCASES:$TOTAL_TESTS"
echo "PASS:$PASS"
SCORE=$(($PASS*100 / $TOTAL_TESTS))
echo "FS_SCORE:$SCORE%"

```

====================================================
"""

Scala Approach
Step 1:
To enter spark shell

```
spark-shell
```

Remaining Steps (run line by line)

run the command in the terminal:

```
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.SQLContext
val spark = SparkSession.builder.appName("Spark2").master("local[*]").getOrCreate()
val sc = spark.sparkContext
val sqlContext = new SQLContext(sc)
val students_df = sqlContext.read.json("Students.json")
students_df.show()
students_df.createOrReplaceTempView("students")
val result_df = spark.sql("SELECT * FROM students WHERE age < 25")
result_df.show()
result_df.coalesce(1).write.format("csv").option("header", "true").save("result")
```

Python Approach (Do not use as the score is done by scala approach)

Create the json file first.

Step 1:
To enter spark shell

```
pyshark
```

Remaining Steps (run line by line)

run the command in the terminal:

```
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Spark2").master("local[*]").getOrCreate()
sqlContext = spark._wrapped
students_df = sqlContext.read.json("Students.json")
students_df.show()
students_df.createOrReplaceTempView("students")
result_df = spark.sql("SELECT \* FROM students WHERE age < 25")
result_df.show()
result_df.coalesce(1).write.csv("result", header=True)
```

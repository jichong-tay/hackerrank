1. Spark Preliminaries: Word Count Problem using Spark RDD

#Steps to complete the Handson:

1. Click on Terminal --> New to open the terminal in HR.
2. Use spark-shell to solve this challenge.
3. Install all the necessary dependencies using the INSATLL option from the Project Menu.

This hands-on will help you perform basic operations of Spark RDD.

##Steps:
Step 1: Create a textfile file called "fresco.txt" by using the command `vim fresco.txt` in terminal, and then copy the following data to the file.

Hi Friends Welcome to Fresco Play the digital learning platform

Step 2: Enter the spark shell and import all required SparkSession packages.
Step 3: Create a SparkSession object.
Step 4: Create the text file RDD `newrdd` using the textfile in the path 'projects/challenge/fresco.txt' by using Spark Context's textFile method.
Step 5: Count the total number of 'words' in the rdd and Save the result as a texxt file named as 'WordCount' in a single partition. [hint: coalesce(1).saveAsTextFile()]
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
TOTAL_TESTS=6

if [ -e /projects/challenge/fresco.txt ]
    then PASS=$((PASS+1));
fi;

if  (( $(grep -i "import org.apache.spark.sql.SparkSession" /home/user/.scala_history | wc -l) >=1 ))
  then PASS=$((PASS+1));
fi;

if (( $(grep -i "textFile" /home/user/.scala_history |wc -l) >=1 ))
  then PASS=$((PASS+1));
fi;

if [ -d /projects/challenge/Wordcount ]
   then PASS=$((PASS+1));
fi;

if (( $(ls /projects/challenge/Wordcount/ | grep -io -e "_SUCCESS" | wc -l) ==1 ))
  then PASS=$((PASS+1));
fi;

if (( $(cat /projects/challenge/Wordcount/part* | grep -io -e "(learning,1)" -e "(Fresco,1)" -e "(Welcome,1)" -e "(digital,1)" -e "(Play,1)" -e "(Friends,1)" -e "(to,1)" -e "(platform,1)" -e "(Hi,1)" -e "(the,1)" | wc -l) ==10 ))
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
Create text file fresco.txt

```
vim fresco.txt
i
Hi Friends Welcome to Fresco Play the digital learning platform
:wq
```

Step 2:
To enter spark shell

```
spark-shell
```

Remaining Steps (run line by line)

run the command in the terminal:

```
import org.apache.spark.sql.SparkSession
val spark = SparkSession.builder.appName("Spark4").master("local[*]").getOrCreate()
val newrdd = spark.sparkContext.textFile("fresco.txt")
val Wordcount = newrdd.flatMap(line => line.split(" ")).map(word => (word, 1)).reduceByKey(_ + _)
Wordcount.coalesce(1).saveAsTextFile("Wordcount")
```

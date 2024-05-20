1. Spark Preliminaries: Spark Submit Example

#Steps to complete the Handson:

1. Click on Terminal --> New to open the terminal in HR.
2. All the necessary dependencies are already made available
   In this hands-on, you will run a Spark Program using Spark Submit.

STEPS:
Step 1: Enter into spark-shell and Import all required Spark packages.
Step 2: Create a SparkSession object as 'spark' .
Step 3: Exit the spark shell after completion of steps 1 and 2 (Use Ctrl+d to exit)

Stay in the Terminal and run the sample python file using the "spark-submit sample.py" command 
Once the file is executed, your challenge is completed
Click on RUN TESTS for validation and SUBMIT button for Submission.

====================================================
Bash Score Script

```
#!/bin/bash
SCORE=0
PASS=0
TOTAL_TESTS=3

if  (( $(grep -i "import org.apache.spark.sql.SparkSession" /home/user/.scala_history | wc -l) >=1 ))
  then PASS=$((PASS+1));
fi;

if (( $(grep -i "val spark" /home/user/.scala_history |wc -l) >=1 ))
  then PASS=$((PASS+1));
fi;

DIR="/projects/challenge/Data"
if [ -d "$DIR" ];
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
val spark = SparkSession.builder.appName("Spark5").master("local[*]").getOrCreate()
ctrl+d
spark-submit sample.py
```

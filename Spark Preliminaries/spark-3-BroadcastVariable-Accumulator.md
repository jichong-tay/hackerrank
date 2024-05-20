1. Spark Preliminaries: Broadcast Variable and Accumulator

#Steps to complete the Handson:

1. Click on Terminal --> New to open the terminal.
2. Install all the necessary dependencies using the INSTALL option from the Project Menu.

This hands-on will help you perform basic operations of Broadcast Variable and Accumulator.

##Steps:
Step 1: Enter into spark-shell and import all required Spark packages.
Step 2: Create a SparkSession object as 'spark'.
Step 3: Create a Broadcast Variable broadcastVar from the Array of elements (1,2,3,4,5) and use required commands to start using it.
Step 4: Create a numeric accumulator 'accum' using the longAccumulator() method named "Fresco Accumulator".
Step 5: Create an RDD named as 'data' it contains (Seq(1,2,3,4,5)) values.
Step 6: Find the sum of elements of the 'data' using the accumulator:
Step 7: Store the accum value in a variable called accumulatorVal.
Step 8: Create an RDD with the sequence of accumulatorVal named as 'AccumulatorRdd'.
Step 9: Now, Finally store the AccumulatorRdd value in a text File named as 'Sum'
[hint: coalesce(1).saveAsTextFile("Sum")]

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

TOTAL_TESTS=8



if  (( $(grep -i "import org.apache.spark.sql.SparkSession" /home/user/.scala_history | wc -l) >=1 ))
  then PASS=$((PASS+1));
fi;

if (( $(grep -i "broadcastVar" /home/user/.scala_history |wc -l) >=1 ))
  then PASS=$((PASS+1));
fi;

if (( $(grep -i "broadcastVar.value" /home/user/.scala_history | wc -l ) >=1 ))
   then PASS=$((PASS+1));
fi;

if (( $(grep -i "longAccumulator" /home/user/.scala_history | wc -l ) >=1 ))
   then PASS=$((PASS+1));
fi;


if (( $(grep -i "accum" /home/user/.scala_history | wc -l ) >=1 ))
   then PASS=$((PASS+1));
fi;


if (( $(grep -i "accum.value" /home/user/.scala_history | wc -l ) >=1 ))
   then PASS=$((PASS+1));
fi;

if (( $(ls /projects/challenge/Sum/ | grep -io -e "_SUCCESS" |wc -l) == 1 ))
  then PASS=$((PASS+1));
fi;

if (( $(cat /projects/challenge/Sum/part* | grep -io -e "15" | wc -l ) ==1 ))
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
import org.apache.spark.util.LongAccumulator
val spark = SparkSession.builder.appName("Spark3").master("local[*]").getOrCreate()
val broadcastVar = spark.sparkContext.broadcast(Array(1, 2, 3, 4, 5))
broadcastVar.value
val accum: LongAccumulator = spark.sparkContext.longAccumulator("Fresco Accumulator")
val data = spark.sparkContext.parallelize(Seq(1, 2, 3, 4, 5))
data.foreach(x => accum.add(x))
accum.value
val accumulatorVal = accum.value
val AccumulatorRdd = spark.sparkContext.parallelize(Seq(accumulatorVal))
AccumulatorRdd.coalesce(1).saveAsTextFile("Sum")

```

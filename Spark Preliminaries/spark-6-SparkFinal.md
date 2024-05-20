1. Spark Preliminaries: Final Hands-On

#Steps to complete the Handson:

1. Click on Terminal --> New to open the terminal in HR.
2. Use spark-shell to solve this challenge.
3. Install all the necessary dependencies using INSTALL option from the Project menu.

In this hands-on you will get some insights from the IPL match dataset given to you.

Data set decription:
`id,season,city,date,team1,team2,toss_winner,toss_decision,result,dl_applied,winner,win_by_runs,win_by_wickets,player_of_match,venue,umpire1,umpire2,umpire3`

Your task is to find the top 5 players with maximum number of man of the match awards.
Note: Here man of the match is same as the player_of_match.

##STEPS
Step 1: Enter into spark-shell and Import all required Spark packages.
Step 2: Create a SparkSession object as 'spark'.
Step 3: REad the CSV file to the rdd variable 'data'.
The path is as follows: 'projects/challenge/data.csv'
Step 5: Split the csv file with respect to ',' using map method.
Step 6: Extract the required set of data, man of the match details.
Step 7: Find the total number of man of the match associated with each player, and get the 'top 5 players' with maximum number of man of the match awards:
Step 8: Save the top 5 values in a text file as a single partition in the following patch:
'projects/challenge/IPLData'.

sample data:
(john,32)
(bob,21)
(Mark,18)

Note: The sample data is not the actual data. this data is given to check the format of the output.

Click on RUN TESTS for validation and SUBMIT button for Submission.

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

if  (( $(grep -i "import org.apache.spark.sql.SparkSession" /home/user/.scala_history | wc -l) >=1 ))
then PASS=$((PASS+1));
fi;

if (( $(grep -i ".split" /home/user/.scala_history | wc -l ) >=1 ))
then PASS=$((PASS+1));
fi;

if (( $(grep -i "reduceByKey" /home/user/.scala_history | wc -l ) >=1 ))
then PASS=$((PASS+1));
fi;

if (( $(grep -i "sortBy" /home/user/.scala_history | wc -l ) >=1 ))
then PASS=$((PASS+1));
fi;

if [ -d /projects/challenge/IPLData ]
then PASS=$((PASS+1));
fi;

if (( $(ls /projects/challenge/IPLData/ | grep -io -e "_SUCCESS" | wc -l) ==1 ))
then PASS=$((PASS+1));
fi;

if (( $(cat /projects/challenge/IPLData/part* | grep -io -e "(CH Gayle,17)" -e "(YK Pathan,16)" -e "(AB de Villiers,15)" -e "(DA Warner,14)" -e "(SK Raina,13)" | wc -l) ==5 ))
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
val spark = SparkSession.builder.appName("Spark6").master("local[*]").getOrCreate()
val data = spark.sparkContext.textFile("data.csv")
val splitData = data.map(line => line.split(","))
val playerOfMatch = splitData.map(fields => fields(13))
val playerCounts = playerOfMatch.map(player => (player, 1)).reduceByKey(_ + _).sortBy(_._2, ascending = false)
val top5Players = playerCounts.take(5)
spark.sparkContext.parallelize(top5Players).coalesce(1).saveAsTextFile("IPLData")
```

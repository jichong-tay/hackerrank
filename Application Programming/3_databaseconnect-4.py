"""
4. Database Connectivity 4 - Update records
- Write a script to update the following items with new quantitiy_in_stock values:
 - 103 -> 4
 - 101 -> 2
 - 105 -> 0

Expected Output
[(101, 2), (102, 5), (103, 4), (104, 5), (105, 0)]

"""

import sys
import os
import sqlite3


# Complete the function below.


def main():
    conn = sqlite3.connect("SAMPLE.db")
    cursor = conn.cursor()
    cursor.execute("drop table if exists ITEMS")

    sql_statement = """CREATE TABLE ITEMS
    (item_id integer not null, item_name varchar(300), 
    item_description text, item_category text, 
    quantity_in_stock integer)"""

    cursor.execute(sql_statement)

    items = [
        (101, "Nik D300", "Nik D300", "DSLR Camera", 3),
        (102, "Can 1300", "Can 1300", "DSLR Camera", 5),
        (103, "gPhone 13S", "gPhone 13S", "Mobile", 10),
        (104, "Mic canvas", "Mic canvas", "Tab", 5),
        (105, "SnDisk 10T", "SnDisk 10T", "Hard Drive", 1),
    ]
    try:
        cursor.executemany("Insert into ITEMS values (?,?,?,?,?)", items)

        # Add code for updating quantity_in_stock
        items2 = [
            (4, 103),
            (2, 101),
            (0, 105),
        ]
        sql = "update ITEMS set quantity_in_stock = ? where item_id = ?"
        cursor.executemany(sql, items2)

        cursor.execute("select item_id,quantity_in_stock from ITEMS")
    except:
        "Unable to perform the transaction."
    rowout = []
    for row in cursor.fetchall():
        rowout.append(row)
    return rowout
    conn.close()


main()

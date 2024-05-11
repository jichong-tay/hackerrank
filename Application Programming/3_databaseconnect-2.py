"""
2. Database Connectivity 2 - Insert records in table.
 - Write a script that inserts multiple rows (representing various items) at a tme in a table ITEMS. 
  Do not use a loop.
Hint: Use the following data and create a list:

 - Use the list to insert records in the ITEMS table.
 
Expected Output:
[
  (101, 'Nik D300', 'Nik D300', 'DSLR Camera', 3), 
  (102, 'Can 1300', 'Can 1300', 'DSLR Camera', 5), 
  (103, 'gPhone 13S', 'gPhone 13S', 'Mobile', 10), 
  (104, 'Mic canvas', 'Mic canvas', 'Tab', 5), 
  (105, 'SnDisk 10T', 'SnDisk 10T', 'Hard Drive', 1)
]

"""

import sys
import os
import sqlite3


def main():

    conn = sqlite3.connect("SAMPLE.db")
    cursor = conn.cursor()

    cursor.execute("drop table if exists ITEMS")

    sql_statement = """
    CREATE TABLE ITEMS
    (item_id integer not null, 
    item_name varchar(300), 
    item_description text, 
    item_category text, 
    quantity_in_stock integer)
    """

    cursor.execute(sql_statement)

    items = [
        (101, "Nik D300", "Nik D300", "DSLR Camera", 3),
        (102, "Can 1300", "Can 1300", "DSLR Camera", 5),
        (103, "gPhone 13S", "gPhone 13S", "Mobile", 10),
        (104, "Mic canvas", "Mic canvas", "Tab", 5),
        (105, "SnDisk 10T", "SnDisk 10T", "Hard Drive", 1),
    ]

    # Add code to insert records to ITEM table
    sql = """
    insert into ITEMS values 
    (?, ?, ?, ?, ?)
    """
    cursor.executemany(sql, items)

    try:
        cursor.execute("select * from ITEMS")
    except:
        return "Unable to perform the transaction."
    rowout = []
    for row in cursor.fetchall():
        rowout.append(row)
    return rowout

    conn.close()


main()

"""
3. Database Connectivity 3 - Select records from table
- Write a script to read the ITEMS table, and display records for item_id < 103

Expected Output
[(101, 'Nik D300', 'Nik D300', 'DSLR Camera', 3), (102, 'Can 1300', 'Can 1300', 'DSLR Camera', 5)]

"""

import sys
import os
import sqlite3


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
        conn.commit()
        # Add code to select items here

        sql = "select * from ITEMS where item_id < 103"
        cursor.execute(sql)

    except:
        return "Unable to perform the transaction."
    rowout = []
    for row in cursor.fetchall():
        rowout.append(row)
    return rowout
    conn.close()


main()

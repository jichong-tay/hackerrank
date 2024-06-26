"""
5. Database Connectivity 5 - Delete records
- Complete the function to delete item_id 105, assuming that the item will be no longer available in the market.

Expected Output
[(101,), (102,), (103,), (104,)]

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
        cursor.executemany(
            "update ITEMS set quantity_in_stock = ? where item_id = ?",
            [(4, 103), (2, 101), (0, 105)],
        )
        # Add code below to delete items
        sql = "delete from ITEMS where item_id = 105"
        cursor.execute(sql)

        cursor.execute("select item_id from ITEMS")
    except:
        return "Unable to perform the transaction."
    rowout = []
    for row in cursor.fetchall():
        rowout.append(row)
    return rowout
    conn.close()


main()

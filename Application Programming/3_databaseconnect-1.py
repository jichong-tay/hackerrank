"""
1.  Database Connectivity 1 - Connect to Database and create Table
- Connect a sample database 'SAMPLE.db'
Hint: Use sqlite as backend databasem and sqlite3 DB-API
  - Create a connection cursor.
  - Create table ITEMS with attributes
    - item_name,
    - item_description,
    - item_category,
    - quantity_in_stock
- Coomit and close the connection.


"""

import sys
import os
import sqlite3


def main():

    try:
        conn = sqlite3.connect("SAMPLE.db")
        # create connection cursor
        cur = conn.cursor()

        # create table ITEMS using the cursor
        cur.execute(
            """
          CREATE TABLE ITEMS(
              item_name,
              item_description,
              item_category,
              quantity_in_stock
          )"""
        )
        # commit connection
        conn.commit()

        # close connection
        conn.close()
    except Exception as e:
        print(e)
        sys.exit(1)
    else:
        print("Table created successfully")


main()

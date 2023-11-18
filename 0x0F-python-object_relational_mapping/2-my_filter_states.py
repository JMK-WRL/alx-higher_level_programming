#!/usr/bin/python3

"""
Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)


    username, password, database, state_name = sys.argv[1:]

    db = MySQLdb.connect(
            host="localhost",
            post=3306,
            user=username,
            passwd=password,
            db=database
        )

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC", (state_name,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()

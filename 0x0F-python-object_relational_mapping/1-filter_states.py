#!/usr/bin/python3
"""
Script that lists all states with a name starting with N from the database
"""

import sys
import MySQLbd

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:]

    db = MySQLdb.connect(
            host="localhost",
            port=3308,
            user=username,
            passwd=password,
            db=database
        )

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()

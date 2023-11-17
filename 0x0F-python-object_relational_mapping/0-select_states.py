#!/usr/bin/python3

"""
Script that lists all states from the database hbtn_0e_0_usa.

"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    cursor = db.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa")

    cursor.execute("USE hbtn_0e_0_usa")

    cursor.execute("CREATE TABLE IF NOT EXISTS states (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY (id))")

    cursor.execute("SELECR * FROM states ORDER BY id")

    rows = cursor.fetchall();

    for row in rows:
        print(row)

    cursor.close()
    db.close()

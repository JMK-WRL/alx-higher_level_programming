#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb

def main():
    """
    Lists all cities of a specified state from the database hbtn_0e_4_usa.
    """
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()
    query = """
    SELECT GROUP_CONCAT(name SEPARATOR ', ')
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cur.execute(query, (state_name,))
    result = cur.fetchone()
    if result:
        print(result[0])
    else:
        print("No cities found for the specified state.")
    cur.close()
    db.close()

if __name__ == "__main__":
    main()

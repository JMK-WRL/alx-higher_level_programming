#!/usr/bin/python3
"""
Script that lists all states with a name starting with N from the database
"""

import sys
import MySQLbd

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format

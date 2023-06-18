#!/usr/bin/python3
"""
This script takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Connect to MySQLdb"""
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         host='localhost',
                         port=3306)

    """Create a cursor object"""
    cur = db.cursor()

    """Execute SQL query -SELECT-"""
    cur.execute("SELECT * FROM states WHERE name LIKE \
                BINARY '{}' ORDER BY id ASC".format(argv[4]))

    """Fetch all rows and print them"""
    rows = cur.fetchall()
    for row in rows:
        print(row)

    """Close database cursor and database connection"""
    cur.close()
    db.close()

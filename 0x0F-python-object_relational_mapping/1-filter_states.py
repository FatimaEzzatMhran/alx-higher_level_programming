#!/usr/bin/python3
"""
This script lists all states with a name starting with N
from the database hbtn_0e_0_iusa.
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
                BINARY 'N%' ORDER BY id ASC")

    """Fetch all rows and print them"""
    rows = cur.fetchall()
    for row in rows:
        print(row)

    """Close database cursor and database connection"""
    cur.close()
    db.close()

#!/usr/bin/python3
"""
This script takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa.
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
    cur.execute("SELECT cities.name \
                 FROM cities JOIN states \
                 ON cities.state_id = states.id \
                 WHERE states.name LIKE BINARY %s \
                 ORDER BY cities.id ASC", (argv[4],))

    """Fetch all rows and print them"""
    rows = cur.fetchall()
    for row in rows:
        print(row)

    """Close database cursor and database connection"""
    cur.close()
    db.close()

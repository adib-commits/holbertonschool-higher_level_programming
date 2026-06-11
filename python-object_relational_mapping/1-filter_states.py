#!/usr/bin/python3
"""
Lists all states starting with N.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    user=sys.argv[1],
    password=sys.argv[2],
    db_name=sys.argv[3]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwrd=password,
        db=db_name
    )

    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states "
        "WHERE name LIKE BINARY 'N%' "
        "ORDER BY state.id ASC"
    )

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()

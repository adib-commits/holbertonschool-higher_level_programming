#!/usr/bin/python3
"""Displays states matching a user-provided name safely."""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()

    query = (
        "SELECT id, name FROM states "
        "WHERE name = %s "
        "ORDER BY id ASC"
    )

    cur.execute(query, (sys.argv[4],))

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()

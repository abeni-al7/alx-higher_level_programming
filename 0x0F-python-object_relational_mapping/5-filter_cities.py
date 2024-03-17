#!/usr/bin/python3
"""A script that provides a searched result from a database"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    connection = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=db_name,
        port=3306
    )
    cursor = connection.cursor()
    cursor.execute("SELECT c.name FROM cities AS c\
                   JOIN states AS s\
                   ON c.state_id = s.id\
                   WHERE s.name = %s\
                   ORDER BY c.id", (state_name,))
    result = cursor.fetchall()

    for i, row in enumerate(result):
        if i < len(result) - 1:
            print(row[0], end=", ")
        else:
            print(row[0])
    cursor.close()
    connection.close()

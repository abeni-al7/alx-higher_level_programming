#!/usr/bin/python3
"""A script that lists all states with names starting with N from a database"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    connection = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=db_name,
        port=3306
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states\
                   WHERE states.name LIKE 'N%'\
                   ORDER BY states.id")
    result = cursor.fetchall()

    for row in result:
        print(row)

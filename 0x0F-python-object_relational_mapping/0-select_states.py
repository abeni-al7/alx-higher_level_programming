#!/usr/bin/python3
import MySQLdb
import sys
"""A script that lists all states from a database"""

args = sys.argv
if len(args) > 3:
    username = args[1]
    password = args[2]
    db_name = args[3]
else:
    username = ""
    password = ""
    db_name = ""

connection = MySQLdb.connect(
    host="localhost",
    user=username,
    passwd=password,
    db=db_name,
    port=3306
)
cursor = connection.cursor()
cursor.execute("SELECT * FROM states ORDER BY states.id")
result = cursor.fetchall()

for row in result:
    print(row)

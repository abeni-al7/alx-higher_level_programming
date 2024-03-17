#!/usr/bin/python3
"""Searches data from a database"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Retrieve command line arguments
    username, password, db_name, state_name = sys.argv[1:]

    # Connect to MySQL server
    connection = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=db_name,
        port=3306
    )

    # Create cursor
    cursor = connection.cursor()

    # Prepare SQL query
    query = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cursor.execute(query, (state_name,))

    # Fetch results
    results = cursor.fetchall()

    # Display results
    for row in results:
        print(row)

    # Close cursor and connection
    cursor.close()
    connection.close()

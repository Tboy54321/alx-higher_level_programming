#!/usr/bin/python3
'''
Write a script that lists all states with a name
starting with N (upper N) from the database
'''
import MySQLdb
import sys


def list_states(username, password, database_name, name_searched):

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
            )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                   (name_searched,))

    rows = cursor.fetchall()

    for row in rows:
        print("({}, '{}')".format(row[0], row[1]))

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database_name>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        name_searched = sys.argv[4]
        list_states(username, password, database_name, name_searched)

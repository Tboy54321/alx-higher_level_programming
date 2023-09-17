#!/usr/bin/python3
'''
Write a script that lists all states from the database
'''
import MySQLdb
import sys


def list_states(username, password, database_name, state_name):

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
            )

    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name LIKE BINARY %(state_name)s ORDER BY cities.id", (state_name,))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database_name>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        state_name = sys.argv[4]
        list_states(username, password, database_name, state_name)

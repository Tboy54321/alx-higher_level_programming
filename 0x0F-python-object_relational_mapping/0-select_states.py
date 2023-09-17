#!/usr/bin/python3
import MySQLdb
import sys

def list_states(username, password, database_name):

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database_name)

    cursor = db.cursor()


    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    print(rows)
    for row in rows:
        print(row)
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
    else:
        username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, database_name)

#!/usr/bin/python3
""" Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""


def select_states():
    """List all the states in the states table"""
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}'".format(argv[4]))
    rows = cur.fetchall()
    for i in rows:
        if i[1][0].isupper():
            print(i)
    db.close()


if __name__ == "__main__":
    select_states()

#!/usr/bin/python3
"""list all states from database"""

if __name__ == '__main__':
    import sys
    import MySQLdb as driver

    user, passwd, db = sys.argv[1:]
    db = driver.connect(host='localhost', port=3306, user=user, passwd=passwd, db=db)
    cur = db.cursor()

    cur.execute('select * from states order by states.id asc')
    rows = cur.fetchall()

    for row in rows:
        print(row)


#!/usr/bin/python3
"""filter states using name column"""

if __name__ == '__main__':
    import sys
    import MySQLdb as driver

    user, passwd, db = sys.argv[1:]
    db = driver.connect(host='localhost', port=3306,
                        user=user, passwd=passwd, db=db)

    cur = db.cursor()
    cur.execute("select * from states where name like binary 'N%' order by id asc")

    for r in cur.fetchall():
        print(r)

    cur.close()
    db.close()

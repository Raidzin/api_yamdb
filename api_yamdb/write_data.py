import sqlite3
import os

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

os.chdir('static')
os.chdir('data')

sql_file = open('db.sqlite3.sql', 'r')
while True:
    line = sql_file.readline()
    if not line:
        break
    cur.execute(line.strip())
sql_file.close()




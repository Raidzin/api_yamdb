import sqlite3
import os

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

os.chdir('static')
os.chdir('data')
# файл db.sqlite3.sql создан из данных в csv
sql_file = open('db.sqlite3.sql', 'r', encoding='utf-8')
inserts = sql_file.read()
sql_file.close()
inserts = inserts.split(';')
for insert in inserts:
    cur.execute(insert)
sql_file.close()

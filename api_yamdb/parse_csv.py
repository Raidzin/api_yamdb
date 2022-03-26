import sqlite3
import os

INSERT = "INSERT INTO {0} ({1}) VALUES ({2});"

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

os.chdir('static')
os.chdir('data')

file_names = [file for file in os.listdir() if file.endswith('.csv')]
print(file_names)

for file_name in file_names:
    with open(file_name, 'r', encoding='utf-8') as file:
        columns = file.readline().strip()
        line = file.readline().strip()
        line = line.split(',')
        line = [f"'{word}'" for word in line]
        line = ', '.join(line)
        while line:
            print(INSERT.format('reviews_' + file_name[:-4], columns, line))
            cur.execute(INSERT.format('reviews_' + file_name[:-4], columns, line))
            line = file.readline().strip()
            if not line:
                break
            line = line.split(',')
            line = [f"'{word}'" for word in line]
            line = ', '.join(line)

cur.execute('COMMIT;')
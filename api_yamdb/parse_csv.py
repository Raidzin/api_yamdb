import sqlite3
import os
import csv

INSERT = "INSERT INTO {0} ({1}) VALUES ({2});"

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

os.chdir('static')
os.chdir('data')

file_names = [file for file in os.listdir() if file.endswith('.csv')]

for file_name in file_names:
    table_name = 'reviews_' + file_name[:-4]
    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            into = list(row.keys())
            values = list(row.values())
            for i, value in enumerate(values):
                value = value.replace("'", "''")
                values[i] = f"'{value}'"

            if table_name == 'reviews_user':
                into.extend(('password', 'is_superuser',
                             'is_staff', 'is_active', 'date_joined'))
                values.extend(('0', '0', '0', '0', '0'))
            try:
                into = ', '.join(into)
                values = ', '.join(values)
                cur.execute(INSERT.format(table_name, into, values))
            except Exception as error:
                print()
                print(INSERT.format(table_name, into, values))
                print(error, end='\n\n')
cur.execute('COMMIT;')

# Хорошо что скрип записи данных не проходит ревью...

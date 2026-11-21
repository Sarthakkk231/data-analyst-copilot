import sqlite3

conn = sqlite3.connect("sales.db")

cursor = conn.cursor()

cursor.execute("PRAGMA table_info(sales)")

for column in cursor.fetchall():
    print(column)

conn.close()
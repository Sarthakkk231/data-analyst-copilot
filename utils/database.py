import sqlite3
import pandas as pd

df = pd.read_csv("data/sales.csv", encoding="latin1")

conn = sqlite3.connect("sales.db")

df.to_sql("sales", conn, if_exists="replace", index=False)

conn.close()

print("Database created successfully!")
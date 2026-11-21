import sqlite3
import pandas as pd

def execute_dynamic_query(sql_query):

    conn = sqlite3.connect("temp.db")

    df = pd.read_sql_query(
        sql_query,
        conn
    )

    conn.close()

    return df
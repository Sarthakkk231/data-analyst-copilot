import sqlite3

def create_temp_database(df):

    conn = sqlite3.connect("temp.db")

    df.to_sql(
        "uploaded_data",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()
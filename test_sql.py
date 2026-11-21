from utils.gemini_helper import generate_sql
from utils.sql_executor import execute_query

question = "Show top 5 products by sales"

sql_query = generate_sql(question)

print("\nGenerated SQL:")
print(sql_query)

print("\nResults:")
df = execute_query(sql_query)

print(df)
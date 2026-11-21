from utils.gemini_helper import generate_sql

question = "Show top 5 products by sales"

print("Question:")
print(question)

print("\nGenerated SQL:")
sql_query = generate_sql(question)

print(sql_query)
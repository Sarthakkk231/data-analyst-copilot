import google.generativeai as genai

model = genai.GenerativeModel("gemini-2.0-flash")


def generate_analysis(question, schema):

    prompt = f"""
You are a data analyst AI.

You must return ONLY valid JSON.

Schema:
{schema}

User Question:
{question}

Return format:
{{
  "sql": "SQL query here",
  "insights": "short business insights (max 80 words)",
  "chart_type": "bar or line or scatter"
}}

Rules:
- SQL must be SQLite compatible
- No markdown
- No explanation
"""

    response = model.generate_content(prompt)

    return response.text
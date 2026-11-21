from utils.gemini_helper import model

def generate_insights(question, df):

    data_sample = df.head(20).to_string(index=False)

    prompt = f"""
You are a Senior Business Analyst.

User Question:
{question}

Query Result:
{data_sample}

Analyze the result and provide:

1. Key findings
2. Trends or patterns
3. Important business observations

Rules:
- Keep under 120 words
- Use bullet points
- Focus on business insights
- Do not explain SQL
"""

    response = model.generate_content(prompt)

    return response.text
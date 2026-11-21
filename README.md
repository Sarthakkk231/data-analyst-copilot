# Data Analyst Copilot

An AI-powered data analysis application that helps users explore datasets, execute SQL queries, generate visualizations, and obtain intelligent insights using natural language.

## Overview

Data Analyst Copilot combines Generative AI, Python, SQL, and data visualization to simplify data analysis.

Instead of manually writing complex SQL queries or creating charts, users can interact with their data using an AI-powered workflow.

The application uses Google Gemini for AI-powered assistance and provides database interaction and analytical capabilities.

## Key Features

- **AI-Powered Data Analysis:** Interact with datasets using natural language.
- **SQL Query Assistance:** Generate and execute SQL queries for data exploration.
- **Dynamic Database Operations:** Work with database tables and schemas.
- **Data Visualization:** Generate charts and visual representations of analytical results.
- **Intelligent Insights:** Generate AI-assisted observations from data.
- **CSV Data Support:** Load and analyze structured datasets.
- **Semantic Search:** Use FAISS and Sentence Transformers for vector-based retrieval.
- **Database Integration:** Work with SQLite databases.

## Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| AI / LLM | Google Gemini |
| AI Framework | LangChain |
| Embeddings | Sentence Transformers |
| Vector Database | FAISS |
| Data Processing | Pandas |
| Database | SQLite |
| Visualization | Plotly |
| Application Framework | Streamlit |
| Document Processing | PyMuPDF |

## Project Structure

```text
Data-Analyst-Copilot/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── charts/
│   └── visualizer.py
│
├── data/
│   └── sales.csv
│
├── utils/
│   ├── data_loader.py
│   ├── database.py
│   ├── dynamic_database.py
│   ├── dynamic_sql_executor.py
│   ├── gemini_helper.py
│   ├── insight_generator.py
│   ├── schema_helper.py
│   └── sql_executor.py
│
├── sales.db
├── temp.db
│
├── test_db.py
├── test_env.py
├── test_gemini.py
├── test_sql.py
└── test_temp_db.py
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Sarthakkk231/data-analyst-copilot.git
```

### 2. Navigate to the project directory

```bash
cd data-analyst-copilot
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Google Gemini API

This project requires a Google Gemini API key.

Get your API key from [Google AI Studio](https://aistudio.google.com/apikey).

Create a `.env` file in the root project directory and configure your API key using the environment variable expected by the application.

Keep your API key private. Never commit your `.env` file to GitHub.

### 6. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to access the application.

## Testing

The project includes test scripts for checking database operations, environment configuration, Gemini API connectivity, and SQL execution.

Run individual tests using:

```bash
python test_db.py
python test_env.py
python test_gemini.py
python test_sql.py
python test_temp_db.py
```

Some tests may require a configured Gemini API key and the local database files.

## Future Enhancements

- Advanced multi-agent data analysis.
- Improved natural language to SQL generation.
- Automated data quality checks.
- Interactive analytical dashboards.
- Support for additional database systems.
- Advanced AI-generated business recommendations.

## Author

**Sarthak Karade**

GitHub: [@Sarthakkk231](https://github.com/Sarthakkk231)

---

If you find this project interesting, consider giving the repository a ⭐ on GitHub.

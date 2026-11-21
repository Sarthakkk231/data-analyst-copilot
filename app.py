import streamlit as st
from utils.gemini_helper import generate_analysis
import json
from utils.dynamic_sql_executor import execute_dynamic_query
from charts.visualizer import create_chart
from utils.data_loader import load_dataset
from utils.dynamic_database import create_temp_database
from utils.schema_helper import get_schema

# Page Configuration
st.set_page_config(
    page_title="Data Analyst Copilot",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("Data Analyst Copilot")
st.markdown(
    "Ask business questions in natural language and get data-driven insights."
)

# Dataset Upload
uploaded_file = st.file_uploader(
    " Upload a Dataset",
    type=["csv", "xlsx"]
)
if uploaded_file:

    df_uploaded = load_dataset(uploaded_file)

    create_temp_database(df_uploaded)

    schema = get_schema(df_uploaded)

    st.success("Dataset loaded successfully!")

# KPI 

    st.subheader("Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)

    numeric_cols = df_uploaded.select_dtypes(include="number").shape[1]
    categorical_cols = df_uploaded.select_dtypes(exclude="number").shape[1]

    col1.metric("Rows", df_uploaded.shape[0])
    col2.metric("Columns", df_uploaded.shape[1])
    col3.metric("Numeric", numeric_cols)
    col4.metric("Categorical", categorical_cols)

    st.divider()

    st.subheader("Detected Schema")
    st.text(schema)

    st.subheader("Preview")
    st.dataframe(df_uploaded.head(), use_container_width=True)

# User Input
question = st.text_input(
    "Ask a business question:",
    placeholder="Example: Show top 10 products by total sales"
)

# Analyze Button
if st.button("Analyze"):

    if df_uploaded is None:
        st.error("Please upload a dataset first")

    elif not question:
        st.warning("Please enter a question")

    else:

        try:

            with st.spinner("Thinking..."):
                result = generate_analysis(question, schema)

                # clean JSON (important)
                result = result.replace("```json", "").replace("```", "")
                data = json.loads(result)

            sql_query = data["sql"]
            insights = data["insights"]

            st.subheader("Generated SQL")
            st.code(sql_query, language="sql")

            with st.spinner("Running query..."):
                df = execute_dynamic_query(sql_query)

            st.subheader("Results")
            st.dataframe(df, use_container_width=True)

            fig = create_chart(df)

            if fig:
                st.subheader("Visualization")
                st.plotly_chart(fig, use_container_width=True)

            st.subheader("AI Insights")
            st.info(insights)

        except Exception as e:
            st.error(f"Error: {str(e)}")
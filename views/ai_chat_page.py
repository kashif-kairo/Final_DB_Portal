import streamlit as st

import pandas as pd
 
from database.connection import engine
 
from database.reflection import (
    get_all_tables,
    get_schema_text
)
 
from ai.sql_generator import generate_sql
from ai.sql_validator import validate_sql
from ai.openrouter_client import ask_llm
 
 
def render_ai_chat_page():
 
    st.title("AI Data Analyst")
 
    tables = get_all_tables()
 
    if not tables:
        st.warning("No tables found")
        return
 
    selected_table = st.selectbox(
        "Select Table",
        tables
    )
 
    question = st.chat_input(
        "Ask a question about your data..."
    )
 
    if not question:
        return
 
    schema = get_schema_text(
        selected_table
    )
 
    sql_query = generate_sql(
        schema,
        question
    )
 
    st.subheader("Generated SQL")
 
    st.code(
        sql_query,
        language="sql"
    )
 
    if not validate_sql(sql_query):
 
        st.error(
            "Unsafe query blocked."
        )
 
        return
 
    try:
 
        df = pd.read_sql(
            sql_query,
            engine
        )
 
        st.subheader("Query Result")
 
        st.dataframe(
            df,
            use_container_width=True
        )
 
        explanation_prompt = f"""
User Question:
{question}
 
Query Result:
{df.head(20).to_string()}
 
Explain the answer in simple English.
"""
 
        answer = ask_llm(
            explanation_prompt
        )
 
        st.subheader(
            "AI Explanation"
        )
 
        st.write(answer)
 
    except Exception as e:
 
        st.error(str(e))
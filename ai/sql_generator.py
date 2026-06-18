from ai.openrouter_client import ask_llm
 
 
def generate_sql(schema, question):
 
    prompt = f"""
You are a MySQL expert.
 
Database Schema:
 
{schema}
 
Convert user question into SQL.
 
Rules:
1. Return ONLY SQL.
2. Use SELECT statements only.
3. Never generate UPDATE.
4. Never generate DELETE.
5. Never generate INSERT.
6. Never generate DROP.
 
Question:
{question}
"""
 
    return ask_llm(prompt)
 

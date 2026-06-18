FORBIDDEN = [
    "INSERT",
    "UPDATE",
    "DELETE",
    "DROP",
    "ALTER",
    "TRUNCATE",
    "CREATE"
]
 
 
def validate_sql(sql):
 
    sql_upper = sql.upper()
 
    for keyword in FORBIDDEN:
 
        if keyword in sql_upper:
            return False
 
    return sql_upper.strip().startswith(
        ("SELECT", "WITH")
    )
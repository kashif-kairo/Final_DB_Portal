import streamlit as st
import pandas as pd

from database.reflection import (
    get_all_tables,
    get_columns,
    get_primary_key
)


def render_tables_page():

    st.title(
        "Database Tables"
    )

    tables = get_all_tables()

    if not tables:

        st.warning(
            "No tables found"
        )

        return

    selected_table = st.selectbox(
        "Select Table",
        tables
    )

    st.subheader(
        f"Table: {selected_table}"
    )

    columns = get_columns(
        selected_table
    )

    st.dataframe(
        pd.DataFrame(columns),
        use_container_width=True
    )

    pk = get_primary_key(
        selected_table
    )

    st.success(
        f"Primary Key: {pk}"
    )
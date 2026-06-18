import streamlit as st
from sqlalchemy import (Integer, Float, Boolean, Date, DateTime)
from sqlalchemy.dialects.mysql import TINYINT

from auth.session import (
    is_admin
)

from auth.permissions import (
    can_insert_table
)

from crud.create import (
    insert_record
)

from database.reflection import (
    get_all_tables,
    get_table_object
)


def render_insert_page():

    st.title(
        "Insert Records"
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

    if not is_admin():

        if not can_insert_table(
            st.session_state.user_id,
            selected_table
        ):

            st.error(
                "No INSERT permission"
            )

            return

    table = get_table_object(
        selected_table
    )

    if table is None:

        st.error(
            "Table not found"
        )

        return

    form_data = {}

    st.subheader(
        f"Insert into {selected_table}"
    )

    for column in table.columns:
        # st.write(column.name,type(column.type),column.type)

        if column.primary_key:
            continue

        column_type = column.type 
        if (column.name.lower() == "is_active" or isinstance(column_type,TINYINT) or isinstance(column_type,Boolean)):
            form_data[column.name]=st.checkbox(column.name)

        elif isinstance(column_type,Float):
            form_data[column.name]=st.number_input(column.name, step =0.01)

        elif isinstance(column_type,Date):
            form_data[column.name]=st.date_input(column.name)

        elif isinstance(column_type, DateTime):
            form_data[column.name]=st.date_input(column.name)
        else:
            if 'email' in column.name.lower():
                form_data[column.name]=st.text_input(column.name,placeholder="user@example.com")
            else:
                form_data[column.name]=st.text_input(column.name)

    if st.button(
        "Insert Record"
    ):

        success, message = insert_record(
            selected_table,
            form_data
        )

        if success:

            st.success(
                message
            )

        else:

            st.error(
                message
            )
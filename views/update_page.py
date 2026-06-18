import streamlit as st
from sqlalchemy import (Integer, Float, Boolean, Date, DateTime)
from sqlalchemy.dialects.mysql import TINYINT


from auth.session import (
    is_admin
)

from auth.permissions import (
    can_update_table
)

from crud.update import (
    get_record_by_id,
    update_record
)

from database.reflection import (
    get_all_tables,
    get_table_object,
    get_primary_key
)


def render_update_page():

    st.title(
        "Update Records"
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

        if not can_update_table(
            st.session_state.user_id,
            selected_table
        ):

            st.error(
                "No UPDATE permission"
            )

            return

    pk = get_primary_key(
        selected_table
    )

    record_id = st.number_input(
        f"{pk}",
        min_value=1,
        step=1
    )

    if st.button(
        "Load Record"
    ):

        st.session_state.record = (
            get_record_by_id(
                selected_table,
                record_id
            )
        )

    if "record" not in st.session_state:

        return

    record = st.session_state.record

    if not record:

        st.error(
            "Record not found"
        )

        return

    table = get_table_object(
        selected_table
    )

    updated_data = {}

    st.subheader(
        "Edit Record"
    )

    for column in table.columns:

        if column.primary_key:
            continue

        column_type = column.type 
        if (column.name.lower() == "is_active" or isinstance(column_type,TINYINT) or isinstance(column_type,Boolean)):
            updated_data[column.name]=st.checkbox(column.name,value=bool(record.get(column.name,0)))

        elif isinstance(column_type,Float):
            updated_data[column.name]=st.number_input(column.name, value=float(record.get(column.name,0)) ,step =0.01)

        elif isinstance(column_type,Date):
            updated_data[column.name]=st.date_input(column.name,value=record.get(column.name))

        elif isinstance(column_type, DateTime):
            updated_data[column.name]=st.date_input(column.name)
        else:
            if 'email' in column.name.lower():
                updated_data[column.name]=st.text_input(column.name,placeholder="user@example.com",value=str(record.get(column.name,"")))
            else:
                updated_data[column.name]=st.text_input(column.name,value=str(record.get(column.name,"")))

        # updated_data[
        #     column.name
        # ] = st.text_input(
        #     column.name,
        #     value=str(
        #         record.get(
        #             column.name,
        #             ""
        #         )
        #     )
        # )

    if st.button(
        "Update Record"
    ):

        success, msg = (
            update_record(
                selected_table,
                record_id,
                updated_data
            )
        )

        if success:

            st.success(msg)

        else:

            st.error(msg)
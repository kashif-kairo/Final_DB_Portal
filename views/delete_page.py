import streamlit as st

from auth.session import (
    is_admin
)

from auth.permissions import (
    can_delete_table
)

from crud.delete import (
    delete_record
)

from database.reflection import (
    get_all_tables,
    get_primary_key
)


def render_delete_page():

    st.title(
        "Delete Records"
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

        if not can_delete_table(
            st.session_state.user_id,
            selected_table
        ):

            st.error(
                "No DELETE permission"
            )

            return

    pk = get_primary_key(
        selected_table
    )

    st.subheader(
        f"Delete from {selected_table}"
    )

    record_id = st.number_input(
        f"{pk}",
        min_value=1,
        step=1
    )

    st.warning(
        "This action cannot be undone."
    )

    confirm = st.checkbox(
        "I understand"
    )

    if st.button(
        "Delete Record",
        type="primary"
    ):

        if not confirm:

            st.error(
                "Please confirm deletion."
            )

            return

        success, msg = (
            delete_record(
                selected_table,
                record_id
            )
        )

        if success:

            st.success(msg)

        else:

            st.error(msg)
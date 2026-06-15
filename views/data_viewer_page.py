import streamlit as st
import pandas as pd

from auth.session import is_admin

from auth.permissions import (
    can_read_table
)

from crud.read import (
    get_table_data
)

from database.reflection import (
    get_all_tables
)


def render_data_viewer():

    st.title("Data Viewer")

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

    user_id = st.session_state.user_id

    if not is_admin():

        if not can_read_table(
            user_id,
            selected_table
        ):

            st.error(
                "You don't have READ permission."
            )

            return

    df = get_table_data(
        selected_table
    )

    if df.empty:

        st.warning(
            "No records found"
        )

        return

    st.subheader(
        f"{selected_table} Records"
    )

    search = st.text_input(
        "Search"
    )

    if search:

        mask = df.astype(
            str
        ).apply(
            lambda row:
            row.str.contains(
                search,
                case=False
            ).any(),
            axis=1
        )

        df = df[mask]

    page_size = 10

    total_rows = len(df)

    total_pages = (
        total_rows // page_size
    ) + (
        1 if total_rows %
        page_size else 0
    )

    page = st.number_input(
        "Page",
        min_value=1,
        max_value=max(
            total_pages,
            1
        ),
        value=1
    )

    start = (
        page - 1
    ) * page_size

    end = start + page_size

    st.dataframe(
        df.iloc[start:end],
        use_container_width=True
    )

    st.caption(
        f"Rows: {total_rows}"
    )
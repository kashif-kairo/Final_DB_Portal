import streamlit as st
import pandas as pd

from auth.session import is_admin

from crud.permissions_crud import (
    get_all_users,
    get_permissions,
    save_permission
)


def render_permissions_page():

    if not is_admin():

        st.error("Access Denied")
        st.stop()

    st.title("Permission Management")

    users = get_all_users()

    user_map = {
        f"{u.user_id} - {u.username}": u.user_id
        for u in users
    }

    selected_user = st.selectbox(
        "Select User",
        list(user_map.keys())
    )

    user_id = user_map[selected_user]

    table_name = st.text_input(
        "Table Name",
        placeholder="customers"
    )

    st.subheader("Permissions")

    can_read = st.checkbox("Read")

    can_insert = st.checkbox("Insert")

    can_update = st.checkbox("Update")

    can_delete = st.checkbox("Delete")

    if st.button("Save Permission"):

        save_permission(
            user_id,
            table_name,
            can_read,
            can_insert,
            can_update,
            can_delete
        )

        st.success(
            "Permission Saved"
        )

        st.rerun()

    st.divider()

    st.subheader(
        "Current Permissions"
    )

    permissions = get_permissions(
        user_id
    )

    data = []

    for p in permissions:

        data.append({
            "Table": p.table_name,
            "Read": p.can_read,
            "Insert": p.can_insert,
            "Update": p.can_update,
            "Delete": p.can_delete
        })

    st.dataframe(
        pd.DataFrame(data),
        use_container_width=True
    )
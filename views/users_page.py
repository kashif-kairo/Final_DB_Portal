import streamlit as st
import pandas as pd

from auth.session import is_admin

from crud.users_crud import (
    get_all_users,
    create_user,
    delete_user,
    toggle_user_status
)


def render_users_page():

    if not is_admin():

        st.error("Access Denied")

        st.stop()

    st.title("User Management")

    st.subheader("Create User")

    username = st.text_input(
        "Username"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    role = st.selectbox(
        "Role",
        [
            "admin",
            "editor",
            "viewer"
        ]
    )

    if st.button("Create User"):

        success, msg = create_user(
            username,
            password,
            role
        )

        if success:

            st.success(msg)

            st.rerun()

        else:

            st.error(msg)

    st.divider()

    users = get_all_users()

    data = []

    for user in users:

        data.append(
            {
                "ID": user.user_id,
                "Username": user.username,
                "Role": user.role,
                "Active": user.is_active
            }
        )

    st.subheader("Users")

    st.dataframe(
        pd.DataFrame(data),
        use_container_width=True
    )

    st.divider()

    st.subheader("Manage User")

    selected_id = st.number_input(
        "User ID",
        min_value=1,
        step=1
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button("Enable / Disable"):

            toggle_user_status(
                selected_id
            )

            st.success(
                "Status Updated"
            )

            st.rerun()

    with col2:

        if st.button("Delete User"):

            delete_user(
                selected_id
            )

            st.success(
                "User Deleted"
            )

            st.rerun()
import streamlit as st

from services.audit_service import (
    log_action
)


def login_user(user):

    st.session_state.logged_in = True

    st.session_state.user_id = user.user_id

    st.session_state.username = user.username

    st.session_state.role = user.role


def logout_user():

    username = (
        st.session_state.get(
            "username",
            "Unknown"
        )
    )

    log_action(
        username,
        "LOGOUT"
    )

    st.session_state.clear()


def is_logged_in():

    return st.session_state.get(
        "logged_in",
        False
    )


def is_admin():

    return (
        st.session_state.get(
            "role"
        )
        == "admin"
    )
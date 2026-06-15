import streamlit as st

from auth.login import authenticate_user
from auth.session import login_user


def render_login():

    st.title("DB Admin Portal")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        user = authenticate_user(
            username,
            password
        )

        if user:

            login_user(user)

            st.success(
                "Login Successful"
            )

            st.rerun()

        else:

            st.error(
                "Invalid Username or Password"
            )
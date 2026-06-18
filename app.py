import streamlit as st

from auth.session import (
    is_logged_in,
    logout_user,
    is_admin
)

from views.login_page import render_login
from views.users_page import render_users_page
from views.permissions_page import render_permissions_page
from views.tables_page import render_tables_page
from views.data_viewer_page import render_data_viewer
from views.insert_page import render_insert_page
from views.update_page import render_update_page
from views.delete_page import render_delete_page
from views.logs_page import render_logs_page
from views.ai_chat_page import render_ai_chat_page


st.set_page_config(
    page_title="DB Admin Portal",
    page_icon="🗄️",
    layout="wide"
)


def render_dashboard():

    st.title("🗄️ DB Admin Portal")

    st.subheader("Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "User",
            st.session_state.username
        )

    with col2:
        st.metric(
            "Role",
            st.session_state.role
        )

    with col3:
        st.metric(
            "Status",
            "Active"
        )

    st.divider()

    st.subheader(
        "Project Progress"
    )

    st.success(
        "✅ Authentication System"
    )

    st.success(
        "✅ User Management"
    )

    st.success(
        "✅ RBAC Permissions"
    )

    st.success(
        "✅ Dynamic Table Reflection"
    )

    st.success(
        "✅ Dynamic Read"
    )

    st.success(
        "✅ Dynamic Insert"
    )

    st.success(
        "✅ Dynamic Update"
    )

    st.success(
        "✅ Dynamic Delete"
    )

    st.success(
        "✅ Audit Logging"
    )

    st.warning(
        "⏳ CSV / Excel Export"
    )

    st.warning(
        "⏳ Bulk Upload"
    )

    st.warning(
        "⏳ Dashboard Analytics"
    )


def main():

    if not is_logged_in():

        render_login()

        return

    st.sidebar.title(
        "🗄️ DB Admin Portal"
    )

    st.sidebar.success(
        f"Welcome {st.session_state.username}"
    )

    st.sidebar.write(
        f"Role: {st.session_state.role}"
    )

    st.sidebar.divider()

    menu_options = [
        "Dashboard",
        "Tables",
        "Data Viewer",
        "Insert",
        "Update",
        "Delete",
        "AI ChatBot"
    ]

    if is_admin():

        menu_options.extend([
            "Users",
            "Permissions",
            "Logs"
        ])

    menu = st.sidebar.radio(
        "Navigation",
        menu_options
    )

    st.sidebar.divider()

    if st.sidebar.button(
        "Logout",
        use_container_width=True
    ):

        logout_user()

        st.rerun()

    # Routing

    if menu == "Dashboard":

        render_dashboard()

    elif menu == "Tables":

        render_tables_page()

    elif menu == "Data Viewer":

        render_data_viewer()

    elif menu == "Insert":

        render_insert_page()

    elif menu == "Update":

        render_update_page()

    elif menu == "Delete":

        render_delete_page()

    elif menu == "Users":

        render_users_page()

    elif menu == "Permissions":

        render_permissions_page()

    elif menu == "Logs":

        render_logs_page()
    
    elif menu == "AI ChatBot":
        render_ai_chat_page()


if __name__ == "__main__":

    main()
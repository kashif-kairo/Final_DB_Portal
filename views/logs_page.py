import streamlit as st
import pandas as pd

from auth.session import (
    is_admin
)

from database.session import (
    SessionLocal
)

from database.models import (
    AuditLog
)


def render_logs_page():

    if not is_admin():

        st.error(
            "Access Denied"
        )

        st.stop()

    st.title(
        "Audit Logs"
    )

    db = SessionLocal()

    try:

        logs = (
            db.query(AuditLog)
            .order_by(
                AuditLog.log_id.desc()
            )
            .all()
        )

        data = []

        for log in logs:

            data.append(
                {
                    "ID": log.log_id,
                    "User": log.username,
                    "Action": log.action,
                    "Table": log.table_name,
                    "Status": log.status,
                    "Error": log.error_message,
                    "Timestamp": log.timestamp
                }
            )

        st.dataframe(
            pd.DataFrame(data),
            use_container_width=True
        )

    finally:

        db.close()
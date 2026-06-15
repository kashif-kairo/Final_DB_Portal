from database.session import SessionLocal
from database.models import AuditLog


def log_action(
    username,
    action,
    table_name="",
    status="SUCCESS",
    error_message=""
):

    db = SessionLocal()

    try:

        log = AuditLog(
            username=username,
            action=action,
            table_name=table_name,
            status=status,
            error_message=error_message
        )

        db.add(log)

        db.commit()

    except Exception as e:

        print(
            f"Audit Log Error: {e}"
        )

        db.rollback()

    finally:

        db.close()
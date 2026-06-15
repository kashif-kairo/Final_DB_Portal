from database.session import SessionLocal
from database.models import TablePermission


def has_permission(
    user_id,
    table_name,
    action
):

    db = SessionLocal()

    try:

        permission = (
            db.query(TablePermission)
            .filter(
                TablePermission.user_id == user_id,
                TablePermission.table_name == table_name
            )
            .first()
        )

        if not permission:
            return False

        if action == "read":
            return permission.can_read

        if action == "insert":
            return permission.can_insert

        if action == "update":
            return permission.can_update

        if action == "delete":
            return permission.can_delete

        return False

    finally:
        db.close()

def can_read_table(
    user_id,
    table_name
):

    db = SessionLocal()

    try:

        permission = (
            db.query(TablePermission)
            .filter(
                TablePermission.user_id == user_id,
                TablePermission.table_name == table_name
            )
            .first()
        )

        if not permission:
            return False

        return permission.can_read

    finally:
        db.close()

def can_insert_table(
    user_id,
    table_name
):

    db = SessionLocal()

    try:

        permission = (
            db.query(TablePermission)
            .filter(
                TablePermission.user_id == user_id,
                TablePermission.table_name == table_name
            )
            .first()
        )

        if not permission:
            return False

        return permission.can_insert

    finally:
        db.close()
def can_update_table(
    user_id,
    table_name
):

    db = SessionLocal()

    try:

        permission = (
            db.query(TablePermission)
            .filter(
                TablePermission.user_id == user_id,
                TablePermission.table_name == table_name
            )
            .first()
        )

        if not permission:
            return False

        return permission.can_update

    finally:
        db.close()

def can_delete_table(
    user_id,
    table_name
):

    db = SessionLocal()

    try:

        permission = (
            db.query(TablePermission)
            .filter(
                TablePermission.user_id == user_id,
                TablePermission.table_name == table_name
            )
            .first()
        )

        if not permission:
            return False

        return permission.can_delete

    finally:
        db.close()
from database.session import SessionLocal
from database.models import (
    User,
    TablePermission
)


def get_all_users():

    db = SessionLocal()

    try:
        return db.query(User).all()

    finally:
        db.close()


def get_permissions(user_id):

    db = SessionLocal()

    try:

        return (
            db.query(TablePermission)
            .filter(
                TablePermission.user_id == user_id
            )
            .all()
        )

    finally:
        db.close()


def save_permission(
    user_id,
    table_name,
    can_read,
    can_insert,
    can_update,
    can_delete
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

        if permission:

            permission.can_read = can_read
            permission.can_insert = can_insert
            permission.can_update = can_update
            permission.can_delete = can_delete

        else:

            permission = TablePermission(
                user_id=user_id,
                table_name=table_name,
                can_read=can_read,
                can_insert=can_insert,
                can_update=can_update,
                can_delete=can_delete
            )

            db.add(permission)

        db.commit()

        return True

    finally:
        db.close()
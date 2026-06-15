from database.session import SessionLocal

from database.models import User

from auth.password_utils import (
    hash_password
)

from services.audit_service import (
    log_action
)


def get_all_users():

    db = SessionLocal()

    try:

        return (
            db.query(User)
            .order_by(
                User.user_id
            )
            .all()
        )

    finally:

        db.close()


def create_user(
    username,
    password,
    role
):

    db = SessionLocal()

    try:

        existing = (
            db.query(User)
            .filter(
                User.username == username
            )
            .first()
        )

        if existing:

            return (
                False,
                "Username already exists"
            )

        user = User(
            username=username,
            password=hash_password(password),
            role=role,
            is_active=True
        )

        db.add(user)

        db.commit()

        log_action(
            "admin",
            "CREATE_USER",
            "users"
        )

        return (
            True,
            "User Created"
        )

    except Exception as e:

        db.rollback()

        log_action(
            "admin",
            "CREATE_USER",
            "users",
            "FAILED",
            str(e)
        )

        return (
            False,
            str(e)
        )

    finally:

        db.close()


def delete_user(
    user_id
):

    db = SessionLocal()

    try:

        user = (
            db.query(User)
            .filter(
                User.user_id == user_id
            )
            .first()
        )

        if not user:

            return

        db.delete(user)

        db.commit()

        log_action(
            "admin",
            "DELETE_USER",
            "users"
        )

    except Exception as e:

        db.rollback()

        log_action(
            "admin",
            "DELETE_USER",
            "users",
            "FAILED",
            str(e)
        )

    finally:

        db.close()


def toggle_user_status(
    user_id
):

    db = SessionLocal()

    try:

        user = (
            db.query(User)
            .filter(
                User.user_id == user_id
            )
            .first()
        )

        if user:

            user.is_active = (
                not user.is_active
            )

            db.commit()

            log_action(
                "admin",
                "TOGGLE_USER_STATUS",
                "users"
            )

    except Exception as e:

        db.rollback()

        log_action(
            "admin",
            "TOGGLE_USER_STATUS",
            "users",
            "FAILED",
            str(e)
        )

    finally:

        db.close()
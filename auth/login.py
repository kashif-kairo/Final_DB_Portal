from database.session import SessionLocal
from database.models import User

from auth.password_utils import verify_password

from services.audit_service import log_action


def authenticate_user(
    username: str,
    password: str
):

    db = SessionLocal()

    try:

        user = (
            db.query(User)
            .filter(
                User.username == username
            )
            .first()
        )

        if not user:

            log_action(
                username,
                "LOGIN",
                "",
                "FAILED",
                "User not found"
            )

            return None

        if not user.is_active:

            log_action(
                username,
                "LOGIN",
                "",
                "FAILED",
                "Account disabled"
            )

            return None

        if not verify_password(
            password,
            user.password
        ):

            log_action(
                username,
                "LOGIN",
                "",
                "FAILED",
                "Wrong password"
            )

            return None

        log_action(
            username,
            "LOGIN"
        )

        return user

    finally:

        db.close()
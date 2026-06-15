from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text
)

from sqlalchemy.sql import func

from database.base import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)

    username = Column(String(100), unique=True, nullable=False)

    password = Column(String(255), nullable=False)

    role = Column(String(20), nullable=False)

    is_active = Column(Boolean, default=True)

    created_at = Column(
        DateTime,
        server_default=func.now()
    )


class TablePermission(Base):
    __tablename__ = "table_permissions"

    permission_id = Column(
        Integer,
        primary_key=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.user_id")
    )

    table_name = Column(
        String(255),
        nullable=False
    )

    can_read = Column(
        Boolean,
        default=False
    )

    can_insert = Column(
        Boolean,
        default=False
    )

    can_update = Column(
        Boolean,
        default=False
    )

    can_delete = Column(
        Boolean,
        default=False
    )


class AuditLog(Base):
    __tablename__ = "audit_logs"

    log_id = Column(
        Integer,
        primary_key=True
    )

    username = Column(
        String(100),
        nullable=False
    )

    action = Column(
        String(50),
        nullable=False
    )

    table_name = Column(
        String(255)
    )

    timestamp = Column(
        DateTime,
        server_default=func.now()
    )

    status = Column(
        String(20)
    )

    error_message = Column(
        Text
    )
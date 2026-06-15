from sqlalchemy import (
    select,
    update
)

from sqlalchemy.orm import Session

from database.connection import engine

from database.reflection import (
    get_table_object,
    get_primary_key
)

from services.audit_service import (
    log_action
)


def get_record_by_id(
    table_name,
    record_id
):

    table = get_table_object(
        table_name
    )

    if table is None:

        return None

    pk = get_primary_key(
        table_name
    )

    with Session(engine) as session:

        stmt = (
            select(table)
            .where(
                table.c[pk] == record_id
            )
        )

        result = session.execute(
            stmt
        ).first()

        if result:

            return dict(
                result._mapping
            )

        return None


def update_record(
    table_name,
    record_id,
    data
):

    table = get_table_object(
        table_name
    )

    if table is None:

        return (
            False,
            "Table not found"
        )

    pk = get_primary_key(
        table_name
    )

    try:

        with Session(engine) as session:

            stmt = (
                update(table)
                .where(
                    table.c[pk] == record_id
                )
                .values(**data)
            )

            result = session.execute(
                stmt
            )

            session.commit()

            if result.rowcount == 0:

                return (
                    False,
                    "Record not found"
                )

        log_action(
            "SYSTEM",
            "UPDATE",
            table_name
        )

        return (
            True,
            "Record updated successfully"
        )

    except Exception as e:

        log_action(
            "SYSTEM",
            "UPDATE",
            table_name,
            "FAILED",
            str(e)
        )

        return (
            False,
            str(e)
        )
from sqlalchemy import delete
from sqlalchemy.orm import Session

from database.connection import engine

from database.reflection import (
    get_table_object,
    get_primary_key
)

from services.audit_service import (
    log_action
)


def delete_record(
    table_name,
    record_id
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
                delete(table)
                .where(
                    table.c[pk] == record_id
                )
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
            "DELETE",
            table_name
        )

        return (
            True,
            "Record deleted successfully"
        )

    except Exception as e:

        log_action(
            "SYSTEM",
            "DELETE",
            table_name,
            "FAILED",
            str(e)
        )

        return (
            False,
            str(e)
        )
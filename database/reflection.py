from sqlalchemy import MetaData

from database.connection import engine


metadata = MetaData()


def refresh_metadata():
    """
    Reload metadata from database
    """

    metadata.clear()

    metadata.reflect(bind=engine)


# Initial reflection
refresh_metadata()


def get_all_tables():
    """
    Return all business tables
    """

    excluded_tables = {
        "users",
        "table_permissions",
        "audit_logs"
    }

    tables = []

    for table_name in metadata.tables.keys():

        if table_name not in excluded_tables:

            tables.append(table_name)

    return sorted(tables)


def get_table_object(table_name):
    """
    Return SQLAlchemy Table object
    """

    return metadata.tables.get(
        table_name,
        None
    )


def get_columns(table_name):
    """
    Return column metadata
    """

    table = get_table_object(
        table_name
    )

    if table is None:
        return []

    columns = []

    for column in table.columns:

        columns.append(
            {
                "name": column.name,
                "type": str(column.type),
                "nullable": column.nullable,
                "primary_key": column.primary_key
            }
        )

    return columns


def get_primary_key(table_name):
    """
    Return primary key column
    """

    table = get_table_object(
        table_name
    )

    if table is None:
        return None

    for column in table.columns:

        if column.primary_key:

            return column.name

    return None
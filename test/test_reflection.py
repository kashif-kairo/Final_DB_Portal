from database.reflection import (
    refresh_metadata,
    get_all_tables,
    get_columns,
    get_primary_key
)

refresh_metadata()

print("\nTables:\n")

tables = get_all_tables()

for table in tables:

    print(table)

    print(
        get_columns(table)
    )

    print(
        "PK:",
        get_primary_key(table)
    )

    print("-" * 50)
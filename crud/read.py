import pandas as pd

from sqlalchemy import select
from sqlalchemy.orm import Session

from database.connection import engine
from database.reflection import get_table_object


def get_table_data(table_name):

    table = get_table_object(table_name)

    if table is None:
        return pd.DataFrame()

    with Session(engine) as session:

        stmt = select(table)

        result = session.execute(stmt)

        rows = result.fetchall()

        if not rows:
            return pd.DataFrame()

        return pd.DataFrame(
            rows,
            columns=result.keys()
        )
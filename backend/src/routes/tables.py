from typing import Annotated

import fastapi
import psycopg_pool

from src import database

router = fastapi.APIRouter(prefix="/api", tags=["tables"])


@router.get("/tables", response_model=list[str])
async def fetch_tables(
    db_pool: Annotated[psycopg_pool.ConnectionPool, fastapi.Depends(database.get_pool)],
):
    tables: list[str] = []

    with db_pool.connection() as connection, connection.cursor() as cursor:
        cursor.execute("""SELECT table_name FROM information_schema.tables
        WHERE table_schema = 'public'""")
        for table in cursor.fetchall():
            tables.append(table[0])

    return tables

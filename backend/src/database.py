import psycopg_pool

from . import config

pool: psycopg_pool.ConnectionPool | None = None


def init_db():
    global pool
    pool = psycopg_pool.ConnectionPool(config.settings.database_url)


def close_db():
    if pool is not None:
        pool.close()


def get_pool() -> psycopg_pool.ConnectionPool:
    if pool is None:
        init_db()

    return pool  # pyright: ignore[reportReturnType]

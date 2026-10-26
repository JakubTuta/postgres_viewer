import psycopg_pool

from . import config

pool: psycopg_pool.ConnectionPool | None = None


def init_db():
    database_url = f"postgresql://{config.settings.postgres_user}:{config.settings.postgres_password}@{config.settings.postgres_host}:{config.settings.postgres_port}/{config.settings.postgres_name}"

    global pool
    pool = psycopg_pool.ConnectionPool(database_url)


def close_db():
    if pool is not None:
        pool.close()


def get_pool() -> psycopg_pool.ConnectionPool:
    if pool is None:
        init_db()

    return pool  # pyright: ignore[reportReturnType]

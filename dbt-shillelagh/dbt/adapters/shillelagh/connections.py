from contextlib import contextmanager
from dataclasses import dataclass

from dbt.adapters.sqlite.connections import SQLiteConnectionManager, SQLiteCredentials
from dbt.logger import GLOBAL_LOGGER as logger
from shillelagh.backends.apsw.db import connect


@dataclass
class ShillelaghCredentials(SQLiteCredentials):
    @property
    def type(self):
        return "shillelagh"

    def _connection_keys(self):
        return tuple()


class ShillelaghConnectionManager(SQLiteConnectionManager):
    TYPE = "shillelagh"

    @contextmanager
    def exception_handler(self, sql: str):
        with super().exception_handler(sql):
            try:
                yield
            except Exception as e:
                raise e

    @classmethod
    def open(cls, connection):
        if connection.state == "open":
            logger.debug("Connection is already open, skipping open.")
            return connection

        handle = connect(connection.credentials.database)

        connection.handle = handle
        connection.state = "open"
        return connection

    def cancel(self, connection):
        # todo: https://rogerbinns.github.io/apsw/example.html#progress-handler
        pass

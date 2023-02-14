from dataclasses import dataclass

from dbt.adapters.base import Credentials
from dbt.adapters.sqlite.connections import SQLiteConnectionManager
from dbt.logger import GLOBAL_LOGGER as logger
from shillelagh.backends.apsw.db import connect


@dataclass
class ShillelaghCredentials(Credentials):
    @property
    def type(self):
        return "shillelagh"

    @property
    def unique_field(self):
        return self.type

    def _connection_keys(self):
        return tuple()


class ShillelaghConnectionManager(SQLiteConnectionManager):
    TYPE = "shillelagh"

    @classmethod
    def open(cls, connection):
        if connection.state == "open":
            logger.debug("Connection is already open, skipping open.")
            return connection

        connection.handle = connect(":memory:")
        connection.state = "open"
        return connection

    def cancel(self, connection):
        # todo: https://rogerbinns.github.io/apsw/example.html#progress-handler
        pass

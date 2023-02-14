from dbt.adapters.shillelagh import ShillelaghConnectionManager
from dbt.adapters.sqlite import SQLiteAdapter


class ShillelaghAdapter(SQLiteAdapter):
    ConnectionManager = ShillelaghConnectionManager

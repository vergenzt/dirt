
from dbt.adapters.sqlite import SQLiteAdapter

from dbt.adapters.shillelagh import ShillelaghConnectionManager


class ShillelaghAdapter(SQLiteAdapter):
    ConnectionManager = ShillelaghConnectionManager

from dbt.adapters.shillelagh import ShillelaghConnectionManager
from dbt.adapters.sqlite import SQLiteAdapter
from dbt.adapters.sqlite.relation import SQLiteRelation


class ShillelaghAdapter(SQLiteAdapter):
    ConnectionManager = ShillelaghConnectionManager
    Relation = SQLiteRelation

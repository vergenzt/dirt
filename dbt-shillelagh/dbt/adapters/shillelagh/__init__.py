from dbt.adapters.shillelagh.connections import ShillelaghConnectionManager  # noqa
from dbt.adapters.shillelagh.connections import ShillelaghCredentials
from dbt.adapters.shillelagh.impl import ShillelaghAdapter

from dbt.adapters.base import AdapterPlugin
from dbt.include import shillelagh


Plugin = AdapterPlugin(
    adapter=ShillelaghAdapter,
    credentials=ShillelaghCredentials,
    include_path=shillelagh.PACKAGE_PATH,
)

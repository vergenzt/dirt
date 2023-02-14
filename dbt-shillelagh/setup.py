#!/usr/bin/env python
from setuptools import find_namespace_packages, setup

package_name = "dbt-shillelagh"
# make sure this always matches dbt/adapters/{adapter}/__version__.py
package_version = "0.1.0"
description = """The Shillelagh adapter plugin for dbt"""

setup(
    name=package_name,
    version=package_version,
    description=description,
    long_description=description,
    author="Tim Vergenz",
    author_email="vergenzt@gmail.com",
    url="https://github.com/vergenzt/dirt",
    packages=find_namespace_packages(include=["dbt", "dbt.*"]),
    include_package_data=True,
    install_requires=[
        "dbt-core~=1.4.0",
    ],
)

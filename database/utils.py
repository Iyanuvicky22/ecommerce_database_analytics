"""
Authors:
    Emmanuel Jolaiya
    Samuel Adedoyin

Date:
    01/10/2024

    # https://docs.sqlalchemy.org/en/14/orm/declarative_tables.html
"""

from enum import Enum

class db_info(Enum):
    TABLE_ENUMERATION = 'enumeration'
    TABLE_LOCALITY = 'locality'
    SCHEMA_NAME = 'npc'
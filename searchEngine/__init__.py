from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    DateTime
)

from datetime import datetime
import pandas as pd

meta_data = MetaData()

baseTable = Table(
    'base'
)
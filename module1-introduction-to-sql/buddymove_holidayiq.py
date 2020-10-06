import sqlite3
import pandas as pd
import numpy as np
import sqlalchemy

url = '~/dev/Unit3/sprint2/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/buddymove_holidayiq.csv'
df = pd.read_csv(url)

from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)

connection = engine.raw_connection()
df.to_sql('Buddy', con= connection)
engine.execute("SELECT * FROM Buddy").fetchall()
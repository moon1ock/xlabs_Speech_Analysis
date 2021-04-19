# %% Connect to DB
import sqlite3
import pandas as pd

con = sqlite3.connect("./auth.db")
data_db = pd.read_sql_query("SELECT * from user", con)
df = data_db[data_db.responseCounter == 6]
con.close()
df = df[["key","response4", "response5"]]




# %% Get list

df["key"].tolist()

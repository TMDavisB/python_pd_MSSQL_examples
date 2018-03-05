#!/usr/bin/python

import pyodbc
import pandas as pd


TableName = "owner"

DB = {
    'drivername': 'mssql+pyodbc',
    'servername': 'LAPTOP-CUJRHGN3',
    #'port': '5432',
    #'username': 'lynn',
    #'password': '',
    'database': 'TestDB',
    'driver': 'SQL Server Native Client 11.0',
    'trusted_connection': 'yes',  
    'legacy_schema_aliasing': False
}


# Parameters
server = 'LAPTOP-CUJRHGN3'
db = 'TestDB'

# Create the connection
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + DB['servername'] + ';DATABASE=' + DB['database'] + ';Trusted_Connection=yes')

# query db
sql = """

SELECT * FROM owner

"""
df = pd.read_sql(sql, conn)

df.to_excel('Master.xlsx')
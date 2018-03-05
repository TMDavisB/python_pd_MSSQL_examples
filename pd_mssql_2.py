#!/usr/bin/python

#import pyodbc
import pandas as pd
from sqlalchemy import create_engine
import sys

df = pd.read_excel('master.xlsx')

#update required key's value

DB = {
    'drivername': 'mssql+pyodbc',
    'servername': 'LAPTOP-CUJRHGN3',
    #'port': '0000',
    #'username': 'root',
    #'password': '',
    'database': 'TestDB',
    'driver': 'SQL Server Native Client 11.0',
    'trusted_connection': 'yes',  
    'legacy_schema_aliasing': False,
	'table':'owner'
}

# Create the connection
engine = create_engine(DB['drivername'] + '://' + DB['servername'] + '/' + DB['database'] + '?' + 'driver=' + DB['driver'] + ';' + 'trusted_connection=' + DB['trusted_connection'], legacy_schema_aliasing=DB['legacy_schema_aliasing'])

#calling connect method
conn = engine.connect()

# To append records in a existing table use below code
df.to_sql(name='owner',con=engine,if_exists='append',index=False)

# To load records in a empty table
#df.to_sql(name='owner',con=engine,if_exists='fail',index=False)

# select table query
query = ''' select * from ''' + DB['table']

# Read table to create a DataFrame
dataframe = pd.read_sql_query(query,conn)

dataframe.to_excel('result.xlsx')
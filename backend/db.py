import os
from config import Config
import subprocess
import textwrap
import mysql.connector

NYTdata = subprocess.run(['python3', 'backend/script.py'], capture_output= True, text= True)
data = textwrap.dedent(str(NYTdata.stdout.strip()))

mydb = mysql.connector.connect(
  host = Config.db_host,
  user = Config.db_user,
  password = Config.db_password,
  database = Config.db_database 
)

mycursor = mydb.cursor()

sql = "INSERT INTO mytable (address) VALUES (%s)"

mycursor.execute(sql, (data,))

mydb.commit()

print("Data success")

mydb.close()
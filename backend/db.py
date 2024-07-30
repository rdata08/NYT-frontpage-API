import os
import subprocess
import textwrap
import mysql.connector

NYTdata = subprocess.run(['python3', 'backend/app.py'], capture_output= True, text= True)
data = textwrap.dedent(str(NYTdata.stdout.strip()))
print(data)

# db_host = os.getenv("DB_HOST")
# db_user = os.getenv("DB_USER")
# db_password = os.getenv("DB_PASSWORD")
# db_database = os.getenv("DB_DATABASE")

# mydb = mysql.connector.connect(
#   host = db_host,
#   user = db_user,
#   password = db_password,
#   database = db_database 
# )

# mycursor = mydb.cursor()

# sql = "INSERT INTO mytable (address) VALUES (%s)"

# mycursor.execute(sql, (data,))

# mydb.commit()

# print("Data success")

# mydb.close()
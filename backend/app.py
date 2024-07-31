from flask import Flask
import requests
import psycopg2
import os
import time

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_database = os.getenv("DB_DATABASE")

app = Flask(__name__)

while True:
    try:
        connection = psycopg2.connect(host = db_host, database=db_database, user=db_user, password=db_password)
        print("Connection successful")
        break
    except Exception as e:
        print("Connection unsuccessful")
        print("Error", e)
        time.sleep(3)



if __name__ == "__main__":
    app.run(debug=True)
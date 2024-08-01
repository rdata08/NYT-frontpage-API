from flask import Flask, jsonify
from backend.config import Config
import mysql.connector
import time

app = Flask(__name__)

while True:
    try:
        connection = mysql.connector.connect(host = Config.db_host, database=Config.db_database, user=Config.db_user, password=Config.db_password)
        print("Connection successful")
        break
    except Exception as e:
        print("Connection unsuccessful")
        print("Error", e)
        time.sleep(3)

@app.route('/','GET')
def getOne():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM mytable LIMIT 1;")
    result = cursor.fetchone()
    cursor.close()
    
    if result:
        return jsonify({"data": result[0]})
    else:
        return jsonify({"data": "No data found"})


if __name__ == "__main__":
    app.run(debug=True)
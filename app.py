from flask import Flask, jsonify
from backend.config import Config
import backend.db

app = Flask(__name__)

DB = backend.db.DatabaseDriver()

@app.route('/', methods=['GET'])
def getRandom():
    result = DB.getRandom()
    if result:
        return jsonify({"data": result[0]})
    else:
        return jsonify({"data": "No data found"})


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, jsonify
import backend.db

app = Flask(__name__)

DB = backend.db.DatabaseDriver()

@app.route('/', methods=['GET'])
def getRandom():
    results = DB.getRandom()
    if results:
        return jsonify({"data": results})
    else:
        return jsonify({"data": "No data found"})

if __name__ == "__main__":
    app.run(debug=True)
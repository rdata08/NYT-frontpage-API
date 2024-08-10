import requests
from flask import Flask, jsonify
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET'])
def getPage():
    url = "https://www.nytimes.com/section/todayspaper"

    session = requests.Session()
    
    r = session.get(url)

    soup = BeautifulSoup(r.content, 'html.parser')

    if r.status_code == 200:
        # Parse the HTML content with BeautifulSoup
        return soup
    else:
        # Return an error message if the request failed
        return jsonify({"error": "Failed to retrieve the page"}), r.status_code


if __name__ == "__main__":
    app.run(debug=True)
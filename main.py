from flask import Flask, render_template
import requests
import sys
import json
app = Flask(__name__)
request = requests.get('http://localhost:4999/')
list_ = request.json()
meterusageList = []
for element in list_['meters']:
    meterusageList.append((element['meterusage'], element['time']))


@app.route('/', methods=['GET', 'POST'])
def frontEnd():
    return render_template("table.html", data=meterusageList)


if __name__ == "__main__":
    app.run(debug=True, port=5000)

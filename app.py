from flask import Flask, render_template, send_from_directory
from json import dumps

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route("/file/<filename>")
def download(filename):
    return send_from_directory('', filename)

@app.route("/data")
def data(words):
    return str(words)

if __name__=="__main__":
    app.run()
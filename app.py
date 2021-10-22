from flask import Flask, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from json import dumps

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://knmvydibdgtdar:90c0de41d7aec8ad8bfb0280c721bd04664bb930ee8cfe104685acfdbb2d2921@ec2-35-174-56-18.compute-1.amazonaws.com:5432/d83kspcknrffuv?sslmode=require"
db = SQLAlchemy(app)

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
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route("/file/<filename>")
def download(filename):
    return send_from_directory('data', filename)

if __name__=="__main__":
    app.run()
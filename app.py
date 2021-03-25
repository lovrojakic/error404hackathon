from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/index-1.html")
def i1():
    return render_template('index-1.html')

@app.route("/index-2.html")
def i2():
    return render_template('index-2.html')

@app.route("/index-3.html")
def i3():
    return render_template('index-3.html')

@app.route("/index-4.html")
def i4():
    return render_template('index-4.html')

from flask import Flask, request, render_template, jsonify, Response
from amadeus import Client, ResponseError
import requests
app = Flask(__name__)

amadeus = Client(
    client_id='CujnhbJ1hfGIco8AkJ6DktAzK1KW0ARp',
    client_secret='7OotVvuBVqcMmONt'
)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/index.html")
def i0():
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

@app.route("/json-test")
def jsontest():
    return (amadeus.reference_data.urls.checkin_links.get(airlineCode='BA')).result
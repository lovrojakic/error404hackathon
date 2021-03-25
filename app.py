from flask import Flask, request, render_template, jsonify, Response
import amadeus.amadeus
app = Flask(__name__)

amadeus = amadeus.Client(
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

@app.route("/query", methods=["POST"])
def query():
    leavingFrom = request.form["leavingFrom"].upper()
    goingTo = request.form["goingTo"].upper()
    print(leavingFrom, goingTo)
    return amadeus.shopping.flight_dates.get(origin=leavingFrom, destination=goingTo).result
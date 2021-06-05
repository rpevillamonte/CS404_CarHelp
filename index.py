import os
from flask import Flask, render_template, request, session

app = Flask(__name__, static_url_path='/static')
app.secret_key = "key"

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')    

@app.route('/about-us')
def about_us():
    return render_template('about-us.html')

@app.route('/carhelp')
def car_help():
    return render_template('carhelp.html')

@app.route('/understand-cars')
def understand_cars():
    return render_template('understand-cars.html')

app.run(debug=True)
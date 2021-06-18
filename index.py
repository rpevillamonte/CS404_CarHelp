import os
from flask import Flask, render_template, request, session, jsonify
from carexpert import solution

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
    lights = [['Oil Pressure Light', '/img/Icons/Oil_Pressure_Light.png'],
              ['Engine Temperature Light', '/img/Icons/Engine_Temperature_Light.png'],
              ['ABS Light', '/img/Icons/ABS_Light.png'],
              ['Handbrake/Parking Brake Light', '/img/Icons/Handbrake_Light.png'],
              ['Traction Control Light', '/img/Icons/Traction_Control_Light.png'],
              ['Engine Warning Light', '/img/Icons/Engine_Warning_Light.png'],
              ['Battery Alert Light', '/img/Icons/Battery_Alert_Light.png'],
              ['Tire Pressure Light', '/img/Icons/Tire_Pressure_Light.png'],
              ['Fuel Indicator', '/img/Icons/Fuel_Indicator_Light.png'],
              ['Air Bag Indicator', '/img/Icons/Airbag_Indicator_Light.png'],
              ['Seat Belt Indicator', '/img/Icons/Seatbelt_Warning_Light.png'],
              ['Washer Fluid Indicator', '/img/Icons/Washer_Fluid_Indicator.png']
             ]
    problems = ['Knocking on the engine', 'Steering wheel is shaking when at use', 'Squeaking or grinding noise when braking',
                'Steering feels heavy', 'Car does not accelerate, but RPM goes up', 'Car is consuming too much oil',
                'Battery is not charging (even if it is a newly replaced battery)', 'Radiator leaking fluid',
                'Turning the key and nothing happens', 'Too much smoke from the exhaust pipe', 'When changing gear, it will not engage easily / it will not stay in gear (Note: Applies to Manual Transmission)',
                'Fluid is leaking in the differential part', 'Grinding noise when steering and difficulty in steering',
                'Dropping gas mileage and loss of power']

    return render_template('carhelp.html', lights=lights, problems=problems)

#problem-choice: petrol or diesel
@app.route('/solution', methods=['POST'])
def solve():

    is_petrol = int(request.form['petrol_check'])
    light_check = int(request.form['light_check'])
    exp_index = int(request.form['problem'])
    knocking_score = int(request.form['knocking_score'])

    car_solution = solution(is_petrol, light_check, exp_index, knocking_score)
    return jsonify({'solution' : car_solution})

@app.route('/understand-cars')
def understand_cars():
    return render_template('understand-cars.html')

app.run(debug=True)

from flask import render_template, session, request, redirect, url_for, send_file
from models.car import Car 
import random

# @app.route('/')
def home():
    logged_in = session.get('logged_in', False)    
    # Чтение данных из cookie
    e_mail = request.cookies.get('e_mail') # e-mail для кнопки "Profile"
    all_cars = Car.get_all_cars_data()
    # случайные 4 без повторов
    random_cars = random.sample(all_cars, 4)

    # сортировка по ID (предположим, ID — это первый элемент)
    sorted_cars = sorted(random_cars, key=lambda x: x.id)

    return render_template('home.html', logged_in=logged_in, Profile = e_mail,
                           cars_models=sorted_cars, css_path=url_for('static', filename='css/home.css'))

def registration():
    """@app.route("/registration")"""
    return render_template("client/registration.html")



def login():
    """@app.route("/login")"""
    message_style = "no-message"
    return render_template("client/login.html", style = message_style)

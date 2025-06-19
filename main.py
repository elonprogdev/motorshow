from flask import Flask
from flask import render_template, session, request, redirect, url_for, send_file
from models.car import Car 
import sqlite3
import random

app = Flask("motorshow")

@app.route('/')
def index():
    all_cars = Car.get_all_cars_data()

    # случайные 4 без повторов
    random_cars = random.sample(all_cars, 4)

    # сортировка по ID (предположим, ID — это первый элемент)
    sorted_cars = sorted(random_cars, key=lambda x: x.id)

    return render_template('index.html',
                           cars_models=sorted_cars,
                           css_path=url_for('static', filename='css/home.css'))


                
        



app.run(debug=True)
from flask import Flask
from flask import render_template, session, request, redirect, url_for, send_file
import sqlite3
import random

app = Flask("motorshow")

@app.route('/')
def index():
    with sqlite3.connect('cars.db') as connect:
        cars_models = connect.cursor().execute(f"SELECT * FROM Cars").fetchall()
        print(cars_models)
        l = []
        for _ in range(4):
            index = random.randint(0, 19)
            if index not in l:
                l.append(cars_models[index])
                
        
    return render_template('index.html', models = l)


app.run(debug=True)
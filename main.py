from flask import Flask
from controllers import car_controller, info_controller, client_controller
import json, os

app = Flask("motorshow")


app.secret_key = 'youlkfdlk'

# app.config["MAX_CONTENT_LENGTH"] =  5 * 1024

file_path = r'static\data\counters.json'

# Проверяем существует ли файл .json, если нет, создаем его

if not os.path.exists(file_path): 
    with open(file_path, 'w') as file:
        json.dump({}, file)


# Функция для чтения данных о пользователях из файла JSON

def read_counters():
    with open(file_path, 'r') as file:
        users = json.load(file)
    return users


# Функция для записи данных в файл JSON

def write_counters(counters):
    with open(file_path, 'w') as file:
        json.dump(counters, file, indent=4)


app.add_url_rule("/", "home", info_controller.home)  
# app.add_url_rule("/about", "about", info_controller.about)
app.add_url_rule("/registration", "registration", info_controller.registration)
app.add_url_rule("/login", "login", info_controller.login)
app.add_url_rule("/advert", "advert", info_controller.advert)
 

app.add_url_rule("/register", "register", client_controller.register, methods=["GET"])
app.add_url_rule("/log_in", "log_in", client_controller.log_in, methods=["GET"])
app.add_url_rule("/logout", "logout", client_controller.logout, methods=["GET"])
app.add_url_rule("/profile", "profile", client_controller.profile, methods=["GET"] )

app.add_url_rule("/car_advert_create", "car_advert_create", car_controller.car_advert_create, methods=['POST'])

app.run(debug=True)
from flask import Flask
from controllers import info_controller

app = Flask("motorshow")



app.add_url_rule("/", "home", info_controller.home)       



app.run(debug=True)
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import CelestialBodies, Landmark, User, Passenger

@app.route('/')
def hello():
    return "App is running"

if __name__ == '__main__':
    app.run()

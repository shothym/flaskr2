from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('flaskr.config')
db = SQLAlchemy(app)


# なぜこのいち出ないとエラーが出るの？
import flaskr.views

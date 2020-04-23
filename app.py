import os
from os import path
from flask_pymongo import PyMongo
from flask import Flask, render_template

if path.exists('env.py'):
    import env

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')
app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

# Route for index
@app.route('/')
@app.route('/index')
def index():
    skills = mongo.db.skills.find()
    return render_template('index.html', skills=skills)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)

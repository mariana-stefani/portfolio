import os
from flask import Flask, render_template

if path.exists('env.py'):
    import env

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')
app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

@app.route(/)
def hello():
    return 'Hello World'


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
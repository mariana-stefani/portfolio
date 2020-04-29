import os
from os import path
from flask_pymongo import PyMongo
from flask import Flask, render_template, redirect, request, url_for, session, flash
from bson.objectid import ObjectId
from forms import LoginForm
import bcrypt

if path.exists('env.py'):
    import env

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')
app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

# Route for index
@app.route('/')
def index():
    skills = mongo.db.skills.find()
    skill = mongo.db.skills.find_one()
    return render_template('pages/index.html', skills=skills, skill=skill)

# Route for Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        users = mongo.db.users
        existing_user = users.find_one({'username': request.form['username']})
        if existing_user:
            if request.form['password'] == existing_user['password']:
                session['username'] = request.form['username']
                flash(f'Hi {form.username.data}! You have been logged in. Please scroll down to add, edit or delete a skill',
                      'success text-center')
                return redirect(url_for('index'))
            else:
                flash('Login Unsuccessful. Please check username and password',
                      'danger text-center')
        else:
            flash('Login Unsuccessful. Please check username and password',
                  'danger text-center')

    return render_template('pages/login.html', form=form)


# Logout Route
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


# Route to add new skill
@app.route('/skills')
def skills():
    skills = mongo.db.skills.find()
    return render_template('pages/add_skill.html', skills=skills)


# Route to insert new skill to MongoDB database
@app.route('/insert_skill', methods=['POST'])
def insert_skill():
    skills = mongo.db.skills
    skills.insert_one(request.form.to_dict())
    return redirect(url_for('index'))


# Route to display skill to be edited
@app.route('/edit_skill/<skill_id>')
def edit_skill(skill_id):
    skill = mongo.db.skills.find_one({'_id': ObjectId(skill_id)})
    skills = mongo.db.skills.find()
    return render_template('pages/edit_skill.html', skill=skill, skills=skills)


# Route to send updated skill to MongoDB database
@app.route('/update_skill/<skill_id>', methods=['POST'])
def update_skill(skill_id):
    skills = mongo.db.skills
    skills.update({'_id': ObjectId(skill_id)},
                  {'skill_name': request.form.get('skill_name'),
                   'percent': request.form.get('percent'),
                   'colour': request.form.get('colour'),
                   'icon': request.form.get('icon')
                   })
    return redirect(url_for('index'))


# Route to delete skill from MongoDB database
@app.route('/delete_skill/<skill_id>')
def delete_skill(skill_id):
    mongo.db.skills.remove({'_id': ObjectId(skill_id)})
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)

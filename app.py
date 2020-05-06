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
    """
    Render index template and find skills on MongoDB
    """
    skills = mongo.db.skills.find()
    skill = mongo.db.skills.find_one()
    return render_template('pages/index.html', skills=skills, skill=skill)

# Route for Login
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    """
    Render login page and checks if user exists. If it does log user in and display message.
    If not display message saying login was unsuccessful.
    """
    form = LoginForm()
    if form.validate_on_submit():
        users = mongo.db.users
        existing_user = users.find_one({'username': request.form['username']})
        if existing_user:
            if request.form['password'] == existing_user['password']:
                session['username'] = request.form['username']
                flash(f'Hi {form.username.data}! You have been logged in. Please scroll down to add, edit or delete a skill.',
                      'success text-center')
                return redirect(url_for('index'))
            else:
                flash('Login Unsuccessful. Please check username and password.')
        else:
            flash('Login Unsuccessful. Please check username and password.')

    return render_template('pages/login.html', form=form)


# Logout Route
@app.route('/logout')
def logout():
    """
    Clear session to log user out.
    """
    session.clear()
    return redirect(url_for('index'))


# Route to add new skill
@app.route('/admin/skills', methods=['GET', 'POST'])
def skills():
    """
    If request is GET displays add_skill page to be filled by user.
    If request is POST sends filled information to MongoDB.
    """
    if request.method == 'GET':
        skills = mongo.db.skills.find()
        return render_template('pages/add_skill.html', skills=skills)
    else:
        skills = mongo.db.skills
        skills.insert_one(request.form.to_dict())
        flash('Your skill has been successfully added.')
        return redirect(url_for('index'))


# Route to insert new skill to MongoDB database
@app.route('/admin/update_skill/<skill_id>', methods=['GET', 'POST'])
def update_skill(skill_id):
    """
    If request is GET displays edit_skill page that was previously filled by user.
    If request is POST sends updated information to MongoDB.
    """
    if request.method == 'GET':
        skill = mongo.db.skills.find_one({'_id': ObjectId(skill_id)})
        skills = mongo.db.skills.find()
        return render_template('pages/edit_skill.html', skill=skill, skills=skills)
    elif request.method == 'POST':
        skills = mongo.db.skills
        skills.update({'_id': ObjectId(skill_id)},
                      {'skill_name': request.form.get('skill_name'),
                       'percent': request.form.get('percent'),
                       'colour': request.form.get('colour'),
                       'icon': request.form.get('icon')
                       })
        flash('Your skill has been successfully updated.')
        return redirect(url_for('index'))


# Route to delete skill from MongoDB database
@app.route('/admin/delete_skill/<skill_id>')
def delete_skill(skill_id):
    """
    Deletes selected skill, identified by skill_id and display message saying skill was deleted.
    """
    mongo.db.skills.remove({'_id': ObjectId(skill_id)})
    flash('Your skill has been successfully deleted.')
    return redirect(url_for('index'))


# Route to add new skill
@app.route('/admin/projects', methods=['GET', 'POST'])
def projects():
    """
    If request is GET displays add_project page to be filled by user.
    If request is POST sends filled information to MongoDB.
    """
    if request.method == 'GET':
        projects = mongo.db.projects.find()
        return render_template('pages/add_project.html', projects=projects)
    else:
        projects = mongo.db.projects
        projects.insert_one(request.form.to_dict())
        flash('Your project has been successfully added.')
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)

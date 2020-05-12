# Portfolio (Third Milestone Project | Code Institute)

![Responsiveness across devices](static/images/portfolio.png)

## UX (User Experience)

### Project Goals

The goal of this project is the ability to present my professional profile, my skills and my abilities as a software developer for recruiters, employers and potential partners that are looking for a full-stack developer.
For myself, there is a possibility to login and then create, update and delete a skillset or a project from MongoDB.
The website is fully responsive, has a consistent flow and intuitive navigation.

#### **User Goals:**
As a user I expect/want/need:
* To easily find the developer's latest projects with buttons that will redirect me to the live website and the GitHub repository.
* To easily find the information about the developer’s skills proficiency.
* To contact the developer in a built-in contact form.
* To with a click of a button to be able to see the developer’s CV on a new tab instead of having to download it.

#### **User Stories:**

**Emily S.**

*“As a recruiter, I want to be able to find with easy the live website of the projects the developer has done in the past. The ideal website would have a section with these with a frame of the project. When I click on these frames I would expect it to redirect me to the live project.”*

**Jill G.**

*“Having a small startup, I’m always looking for partners for new projects. It’s very important when I’m on a portfolio website that I can easily find a way to contact the developer, ideally with a built-in form. Also, I feel more connected to the developer if there’s a picture of him/ her on the about me section.”*

**Mr. Bridgeman**

*“When I’m looking for a new employee it’s important to be able to see the developers code and what skills he or she have already learned. When looking through a portfolio I expect the skills section to be easily readable and to clearly show how much of each skill the developer knows approximately. I also expect a link to the developer’s GitHub repository, so I can go read the developer’s code.”*

#### **Site Owner Goals:**
As an admin user I expect/want/need:
* To be able to log in on a hidden page when using “/admin” at the end of the index URL.
* To be able to create and update a skillset and/or a project through a form to MongoDB.
* To be able to delete a skillset and/or a project from MongoDB.
* To receive interview offers through the use of contact form.
* To be able to attract attention to my projects.
* To sell myself in a profession but still personal way.



## User Requirements and Expectations:

**Requirements:**

* Navigate through the sections of the portfolio in one single page.
* Content displayed in a visually appealing manner.
* Be provided with a contact form, to easily contact the developer.
* Be able to see a live version of the developer projects.

**Expectations:**

* Navigation takes the user directly to the desired section of the portfolio.
* CV opens in a new tab when clicked.
* Form sends the message correctly.
* Content is well presented and visually satisfying.


## Wireframes

The wireframes for this project were created at [Moqups](https://moqups.com/).
View my wireframes [here](https://github.com/mariana-stefani/portfolio/tree/master/wireframes).


## Features
### Existing Features

**Navbar**
* For users, it includes the following links:
    * Home
    * About me
    * Portfolio
    * Resume
    * Get in Touch

* For admin user, it includes the following links:
    * Home
    * Logout

* Python will evaluate if the admin user is logged in by checking ```if 'username' in session``` and passes this data to Jinja to display the correct navbar.

* In smaller screens the navbar is collapsed and a burger icon is displayed.

#### **Index Page**

**Callout container**
* In this container, the user will find a brief introduction about myself.

**Callout Toast**
* When the user logs in, creates, edit, update or delete a project and/or a skillset a toast message is shown on the top of the page.

**About container**
* In this container the user will find my profile picture, a brief description about me and my skillset with the percentages learned of each skill.

**Skillset Progress Circle**
* This progress circle will move accordingly to the percentage learned in each skill.

**Projects Container**
* In this container, the user will find the projects I have worked on recently. It contains a picture of the project in a desktop screen along with a brief description of the project and two buttons for the project's GitHub repository and the project's live website. If the admin user is logged in, three buttons will be shown to add, edit and/or delete a project.

**Contact Form Container**
* In this container, there is a contact form where the user can enter his/her name, email address and send me a message.

**Contact Toast**
* When the user sends a message a toast message is shown above the contact form.

**Footer**
* It contains links to social media pages that the user can click if they would like to follow me on social media platforms. 

#### **Admin Page**

**Login form**
* This page has a login form with username, password and a login button.

**Login Toast**
* When the user fails to enter the correct username and/or password a toast message is shown above the login form.

#### **Add New Skill Page**
* This page has a form with 4 fields that can be filled with the new skill information to be sent to MongoDB.
* Next to each field title, there's a tooltip. When the admin user hovers the pointer over the tooltip it will display information about what the admin user is expected to write on that field.

#### **Edit Skill Page**
* This page has a form with 4 fields filled with information retrieved from MongoDB, based on the skill ID. These fields can be altered to update an existing skill.

#### **Add New Project Page**
* This page has a form with 7 fields that can be filled with the new project information to be sent to MongoDB.
* Next to each field title, there's a tooltip. When the admin user hovers the pointer over the tooltip it will display information about what the admin user is expected to write on that field.

#### **Edit Project Page**
*	This page has a form with 7 fields filled with information retrieved from MongoDB, based on the project ID. These fields can be altered to update an existing project.

### Features Left to implement

*	Add more projects.
*	Add more skills.
*   Add more classes for the skills colours.
*   Add a dropdown menu for the "Add New Skill" page and for the "Edit Skill" page, where the admin user can select among many skills so the skill colour and icon will be added with the selected skill.


## Information Architecture
### Database Choice

This project utilizes the NoSQL database MongoDB.

### Data Storage Types
For this project the following data types were stored in MongoDB:
* Integer
* ObjectID
* String

### Collections Data Structure
This uses three database collections:

#### Projects Collection

| Title                  | Key in DB       | Form Validation type | Data type |
|------------------------|-----------------|----------------------|-----------|
| Account ID             | _id             | None                 | ObjectId  |
| Project Name           | project_name    | text                 | string    |
| Description of Project | project_desc    | text, maxlength="60" | string    |
| Github Repository      | project_github  | text                 | string    |
| Project URL            | project_live    | text                 | string    |
| Project Image URL      | project_img     | text                 | string    |
| Project Order          | project_order   | text                 | string    |
| Project Divider Line   | project_divider | text                 | string    |

[Example JSON from the projects collection](https://github.com/mariana-stefani/portfolio/blob/master/data/schemas/projects.json)

#### Skills Collection

| Title              | Key in db  | Form Validation type       | Data type |
|--------------------|------------|----------------------------|-----------|
| Account ID         | _id        | None                       | ObjectId  |
| Skill              | skill_name | text                       | string    |
| Percentage learned | percent    | number, min="1", max="100" | integer   |
| Skill colour class | colour     | text                       | string    |
| Icon ID            | icon       | text                       | string    |

[Example JSON from the skills collection](https://github.com/mariana-stefani/portfolio/blob/master/data/schemas/skills.json)

#### Users Collection

| Title      | Key in db | Form Validation type | Data type |
|------------|-----------|----------------------|-----------|
| Account ID | _id       | None                 | ObjectId  |
| Username   | username  | text, maxlength="15" | string    |
| Password   | password  | text, maxlength="15" | string    |

[Example JSON from the users collection](https://github.com/mariana-stefani/portfolio/blob/master/data/schemas/users.json)


## Technologies Used
The technologies used were:

### Languages

* [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)
* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
* [Python](https://www.python.org/)

### Libraries

* [Bootstrap](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/#)
* [Font Awesome](https://fontawesome.com/icons)
* [Google Fonts](https://fonts.google.com/)
* [JQuery](https://jquery.com)
* [Pymongo](https://pymongo.readthedocs.io/en/stable/)

### Tools

* [Am I Responsive](http://ami.responsivedesign.is/)
* [Docdroid](https://www.docdroid.net/)
* [EmailJS](https://www.emailjs.com/)
* [Flat Icon](https://www.flaticon.com/)
* [Free Image Host](https://freeimage.host/)
* [Git](https://github.com/)
* [Heroku](http://www.heroku.com)
* [MongoBD Atlas](https://www.mongodb.com/cloud/atlas)
* [Moqups](https://moqups.com/)
* [Visual Studio Code](https://code.visualstudio.com/)


## Testing

**Navbar Links**
* **Plan:** User clicks on each navbar link and is scrolled to the chosen section.
* **Result:** This test passed.

**Callout Button**
* **Plan:** User clicks on “Let’s Talk” button and page scrolls down to contact me form.
* **Result:** This test has passed.

**About Buttons – When User is Logged In:**
* **Plan 1:** User clicks on Add New Skill and/or Edit button is redirected to Add New Skill and/or Edit Skill page.
* **Plan 2:** User clicks on the Delete button and the skill is deleted from the database.
* **Result:** Both tests have passed.

**Project Buttons**
* **Plan:** User clicks on the project repository page and/or project live website and is redirected to the pages in a separate tab on the browser.
* **Result:** This test has passed.

**Project Buttons – When User is Logged In**
* **Plan 1:** User clicks on Add New Project and/or Edit button is redirected to Add New Project and/or Edit Project page.
* **Plan 2:** User clicks on the Delete button and the project is deleted from the database.
* **Result:** Both tests have passed.

**Contact Me Form**
* **Plan:** After filling all necessary information email is successfully send and a toast message is shown above the form confirming the email was sent.
* **Result:** This test has passed.

**Login Page**
* **Plan 1:** A toast message is shown when the user tries to log in with a username and/or password that are different from the ones stored on the database.
* **Plan 2:** User is redirected to the index page and a toast message is shown if correct username and password are entered.
* **Result:** Both tests have passed.

## Note for the assessor
In order to test the CRUDs functionalities:
* Please enter ***/admin*** after the page URL.
* The username is ***testuser***.
* The password is ***test***.


## Bugs

* **Bug One** 
    * **Problem:** The project was failing to open when the “Open App” button was clicked on the Heroku website.
    * **Solution:** This was fixed by adding MONGO_DBNAME, MONGO_URI and SECRET_KEY to Heroku config vars.

* **Bug Two** 
    * **Problem:** On small screens, the navbar dropdown button was not working. 
    * **Solution:** I fixed the issue updating the JQuery script from version 3.5.0 to the version 3.5.

* **Bug Three** 
    * **Problem:** When importing the layout pages within jinja to base.html nothing was rendering. 
    * **Solution:** This was fixed when with some research I found that I had to include “{% include ‘XYZ’ %}”.


## Deployment 
* The project files were regularly pushed to my [GitHub repository](https://github.com/mariana-stefani/portfolio).

### Heroku Deployment 
#### To deploy this project to Heroku follow the steps below:
1. Install Heroku CLI in your computer by running ```$ brew tap heroku/brew && brew install heroku``` (Make sure to have homebrew installed in your machine).
2. On VSCode terminal run the command ```$ pip3 freeze --local > requirements.txt``` to create a ***requirements.txt*** file.
3. Run the command ```$ echo web: python app.py > Procfile``` to create a ***Procfile***.
4. Deploy each change to Github:
````
$ git add .
$ git commit -m 'Commit message'
$ git push
````
5. Create a free account on the [Heroku website](https://signup.heroku.com).
6. On your Heroku dashboard click on the ***New*** button and then on ***Create new app***. Give it a unique name and select Europe as the region.
7. From your dashboard click on ***Settings*** > ***Reveal Config Vars***.
8. Add the following config vars:

| KEY          | VALUE                                                                                                                  |
|--------------|------------------------------------------------------------------------------------------------------------------------|
| IP           | 0.0.0.0                                                                                                                |
| PORT         | 5000                                                                                                                   |
| MONGO_DBNAME | <project_name>                                                                                                         |
| MONGO_URI    | mongodb+srv://<username>:HsP6P7T7MUJ4Eniv@<cluster_name>-o5dej.mongodb.net/<database_name>?retryWrites=true&w=majority |
| SECRET_KEY   | <your_secret_key>                                                                                                      |
| DEBUG        | FALSE                                                                                                                  |

* To get your MONGO_URI log in to your MongoDB account > click on the cluster for this project > Click on connect > Select *Connect your application* > Copy the URI.
6. On VSCode terminal run the command ```$ heroku login``` to login to your account.
7. Link Heroku to git with the following by running ```$ heroku git:remote -a <yourproject>```.
8. Deploy your project to Heroku by running ```$ git push heroku master```.
9. Your project is now successfully deployed to Heroku.
10. On your Heroku dashboard click on the button ***Open app*** on the top right side to view your deployed project.

### Run the Code Locally

* This project was developed using [Visual Studio Code](https://code.visualstudio.com/) IDE and cloned to a [Git Repository](https://github.com/mariana-stefani/portfolio).

* To clone a Github repository:

	* Open the [repository](https://github.com/mariana-stefani/portfolio) on Github and click on *"Clone or download"* and copy the URL.

	* On VSCode open the *"Command Palette"*, select *"Git: Clone"* and paste the URL.

* The following **must** be installed in your machine:
	* [Git](https://www.atlassian.com/git/tutorials/install-git)
	* [MongoDB](https://docs.mongodb.com/manual/administration/install-community/)
    * [MongoDB Atlas Account](https://www.mongodb.com/cloud/atlas)
        * [Documentation](https://docs.atlas.mongodb.com/) to setup a MongoDB Atlas account.
	* [PIP](https://pip.pypa.io/en/stable/installing/)
	* [Python 3](https://www.python.org/downloads/)
* Install Pipenv Globally:
	* If needed, upgrade pip from your computer's terminal by running ```$ python3.8 -m pip install pip --upgrade```.
	*  To install Pipenv globally, run from your computer's terminal ```$ python3.8 -m pip install pipenv```.	
* Create a Virtual Environment with Pipenv:
	* Open VSCode and from its terminal make a *Projects* directory by running ```$ mkdir Projects```.
	*  Create an empty folder for this project inside the *˜/Projects* directory by running: 
	    ```
        mkdir ˜/Projects/Portfolio
        pipenv install --python 3.8
        ```	
	* Initialize the Virtual Environment: ```$ cd ~/Projects/Portolio```.
	* Activate the Virtual Environment: ```$ pipenv shell```.
	* On VSCode dialog will be shown asking if you'd like to select this new virtual environment for the workspace folder. Click yes.
	* Open the "Command Palette" and select *"Python: Select Interpreter"*.
	* Select the virtual environment that you just created.
* Install the necessary libraries by running ```$ pip3 install -r requirements.txt``` from VSCode terminal.
* Create an file called *"env.py"* and store your *SECRET_KEY* variable, your *MONGO_URI* to link to your on database, your cluster name in *MONGODB_NAME*. The cluster name for this project is ***Portfolio***. You will find the json structure for this cluster collections in the [schemas](https://github.com/mariana-stefani/portfolio/tree/master/data/schemas) folder.
    * Do not commit this file to Git.
	* To hide your environment variables, create a file called *".gitignore"* and write *"env.py"* on this file.
* Run your application with the command ```$ python3 app.py```.
* The project can be viewed at ***http://127.0.0.1:5000***.

## Credits
### Media
* Responsiveness across devices image from [Am I Responsive](http://ami.responsivedesign.is/).
* Icons used on contact me section is made by *iconixar* from [Flat Icon](https://www.flaticon.com/).


## Acknowledgments
All my gratitude to my wonderful husband and family who always have supported me. A big thank you to my mentor Simen Daehlin for your ideas, advise and support! Thank you to Anna Greaves, Haley Schafer, Luca Dettorre, Tim Nelson from Code Institute for your time and assistance. Thank you to Guillermo from Slack. Thank you to everyone from Code Institute!
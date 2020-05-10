# Portfolio (Third Milestone Project | Code Institute)


## UX (User Experience)

### Project Goals

The goal of this project is the ability to present my professional profile, my skills and my abilities as a software developer for recruiters, employers and potential partners that are looking for a full-stack developer.
For myself, there is a possibility to login and then create, update and delete a skillset or a project from MongoDB.
The website is fully responsive, has a consistent flow and intuitive navigation.

#### **User Goals:**
* As a user I expect to easily find the developer's latest projects with buttons that will redirect me to the live website and to the GitHub repository.
* As a user I expect to easily find the information about the developer’s skills proficiency.
* As a user I expect to contact the developer in a built in contact form.
* As a user I expect to with a click of a button to be able to see the developer’s CV on a new tab instead of having to download it.

#### **User Stories:**

**Emily S.**

*“As a recruiter, I want to be able to find with easy the live website of the projects the developer has done in the past. The ideal website would have a section with these with a frame of the project. When I click on these frames I would expect it to redirect me to the live project.”*

**Jill G.**

*“Having a small startup, I’m always looking for partners for new projects. It’s very important when I’m on a portfolio website that I can easily find a way to contact the developer, ideally with a built-in form. Also, I feel more connected to the developer if there’s a picture of him/ her on the about me section.”*

**Mr. Bridgeman**

*“When I’m looking for a new employee it’s important to be able to see the developers code and what skills he or she have already learned. When looking through a portfolio I expect the skills section to be easily readable and to clearly show how much of each skill the developer knows approximately. I also expect a link to the developer’s GitHub repository, so I can go read the developer’s code.”*

#### **Site Owner Goals:**

* Receive interview offers through the use of contact form.
* Be able to attract attention to my projects.
* Sell myself in a profession but still personal way.
* Be able to log in on a hidden page when using “/admin” at the end of the index URL.
* Be able to create and update a skillset and/or a project through a form to MongoDB.
* Be able to delete a skillset and/or a project from MongoDB.


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
View my wireframes [here](https://github.com/mariana-stefani/portfolio/tree/master/wireframes)


## Features
### Existing Features

**Navbar**
* For users it includes the following links:
    * Home
    * About me
    * Portfolio
    * Get in Touch

**Background colour**
* The gradient was done using CSS.

#### **Index Page**

**Callout container**
* In this container, the user will find a brief introduction about myself.

**Callout Button**
* This button scrolls the page to the contact form.

**About container**
* In this container the user will find my profile picture, a brief description about me and my skillset with the percentages learned of each skill.

**About Buttons**
* If the user is logged in, three buttons will be shown to add, edit and/or delete a skill.

**About Toast**
* When the user logs in, creates, edit and/or update a project and/or a skillset a toast message is shown on the top of the page.

**Skillset Progress Circle**
* This progress circle will move accordingly to the percentage learned in each skill.

**Projects Container**
* In this container, the user will find the projects I have worked on recently. It contains a picture of the project in a desktop resolution along with a brief description of the project. 

**Project Buttons**
* Below the description, there are two buttons that redirect the user to the project GitHub repository and to the live website.
* If the user is logged in, three buttons will be shown to add, edit and/or delete a project.

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

#### **Edit Skill Page**
* This page has a form with 4 fields filled with information retrieved from MongoDB, based on the skill ID. These fields can be altered to update an existing skill.

#### **Add New Project Page**
* This page has a form with 7 fields that can be filled with the new project information to be sent to MongoDB.

#### **Edit Project Page**
*	This page has a form with 7 fields filled with information retrieved from MongoDB, based on the project ID. These fields can be altered to update an existing project.

### Features Left to implement

*	Add more projects.
*	Add more skills.
*   Add more classes for the skills colours.


## Information Architecture
### Database Choice

This projects utilizes the NoSQL database MongoDB.

### Data Storage Types
For this project the following data types were stored in MongoDB:
* Integer
* ObjectID
* String

### Collections Data Structure
This uses three database collections:

#### Projects Collection

| Title                  | Key in db       | Form Validation type | Data type |
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

[HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)

* Is the markup language used for rendering the website. 

[CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)

* Is the language used to style the HTML website.

[JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

* Is used for the responsive and interactive elements of this project.

[Bootstrap](https://getbootstrap.com/docs/4.4/getting-started/introduction/)

* Is the front-end framework used to assist in page layout, navigation and modal.

[EmailJS](https://www.emailjs.com/)

* Is used as a third-party email service on this project.


[Flask](https://flask.palletsprojects.com/en/1.1.x/#)

* Is used as a Python microframework to construct and render pages.


[Flat Icon](https://www.flaticon.com/)

* Its icons were used on the Contact Me container.

[Font Awesome](https://fontawesome.com/icons)

* Its icons were used on the About Me buttons, Project buttons, Footer, Add and Edit New Skill and Add and Edit New Project pages.

[Git](https://github.com/)

* Local git repository was pushed to a remote repository on GitHub and site was published using GitHub pages.

[Google Fonts](https://fonts.google.com/)

* Its fonts were used on the website. Main theme font was *"Poppins"* and sub-theme font was *"Sans-Serif"*.

[Heroku](http://www.heroku.com)
* Is used to deploy the application.

[JQuery](https://jquery.com)

* Is used to simplify DOM manipulation when creating the markers on the map and to zoom on the map when a country is selected on the drop-down menu.

[MongoBD Atlas](https://www.mongodb.com/cloud/atlas)

* Is used as the non-relational database for this project.

[Python](https://www.python.org/)

*	Is used as the back-end programming language for this project

[Pymongo](https://pymongo.readthedocs.io/en/stable/)
*	Is used as Python’s API for MongoDB integration.

[Visual Studio Code](https://code.visualstudio.com/)
*	Was used as the IDE for this project.

For Additional technologies used please see requirements.txt


## Testing

**Navbar Links**
* Plan: User clicks on each navbar link and is scrolled to the chosen section.
* Result: This test passed.

**Callout Button**
* Plan: User clicks on “Let’s Talk” button and page scrolls down to contact me form.
* Result: This test has passed.

**About Buttons – When User is Logged In:**
* Plan 1: User clicks on Add New Skill and/or Edit button is redirected to Add New Skill and/or Edit Skill page
* Plan 2: User clicks on the Delete button and the skill is deleted from the database.
* Result: Both tests have passed.

**Project Buttons**
* Plan: User clicks on the project repository page and/or project live website and is redirected to the pages in a separate tab on the browser.
* Result: This test has passed.

**Project Buttons – When User is Logged In**
* Plan 1: User clicks on Add New Project and/or Edit button is redirected to Add New Project and/or Edit Project page.
* Plan 2: User clicks on the Delete button and the project is deleted from the database.
Result: Both tests have passed.

**Contact Me Form**
* Plan: After filling all necessary information email is successfully send and a toast message is shown above the form confirming the email was sent.
* Result: This test has passed.

**Login Page**
* Plan 1: A toast message is shown when the user tries to log in with a username and/or password that are different from the ones stored on the database.
* Plan 2: User is redirected to the index page and a toast message is shown if correct username and password are entered.
* Result: Both tests have passed.


## Bugs

* The project was failing to open when the “Open App” button was clicked on the Heroku website.
This was fixed adding MONGO_DBNAME, MONGO_URI and SECRET_KEY to Heroku config vars.

* On smaller resolutions, the navbar dropdown button was not working. I fixed the issue updating the JQuery script from version 3.5.0 to the version 3.5.1.

* When importing the layout pages within jinja to base.html nothing was rendering. This was fixed when with some research I found that I had to include “{% include ‘XYZ’ %}”.
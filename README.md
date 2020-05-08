# Portfolio (Third Milestone Project | Code Institute)


## UX (User Experience)

### Project Goals

The goal of this project is the ability to present my professional profile, my skills and my abilities as a software developer for recruiters, employers and potential partners that are looking for a full-stack developer.
For myself, there is a possibility to login and then create, update and delete a skillset or a project from MongoDB.
The website is fully responsive, has a consistent flow and intuitive navigation.

#### **User Goals:**
* A website where the developer’s works can easily be found with the live website and GitHub repository attached.
* Information about the developer’s skills proficiency.
* A contact form where the developer can be contacted directly.
* To be able to see the developer’s CV on a new tab instead of having to download it.

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


### **Wireframes**

The wireframes for this project were created at [Moqups](https://moqups.com/).
View my wireframes [here](https://github.com/mariana-stefani/portfolio/tree/master/wireframes)

## Features
### Existing Features

**Navbar**
* Bootstrap code was used to make the navbar.

**Background colour**
* The gradient was done using CSS.

#### Index Page

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

#### Admin Page

**Login form**
* This page has a login form with username, password and a login button.

**Login Toast**
* When the user fails to enter the correct username and/or password a toast message is shown above the login form.

#### Add New Skill Page
* This page has a form with 4 fields that can be filled with the new skill information to be sent to MongoDB.

#### Edit Skill Page
* This page has a form with 4 fields filled with information retrieved from MongoDB, based on the skill ID. These fields can be altered to update an existing skill.

#### Add New Project Page
* This page has a form with 7 fields that can be filled with the new project information to be sent to MongoDB.

#### Edit Project Page
*	This page has a form with 7 fields filled with information retrieved from MongoDB, based on the project ID. These fields can be altered to update an existing project.

# The Groomer's Network

Developer: [Helen Murugan](https://github.com/helenmurugan)<br>
Deployed website: [Link to website](https://the-groomers-network-96ece9118f5d.herokuapp.com/)<br>

![Main image](documentation/readme_landing_page.jpg)

The Groomer's Network is a Django web application that allows pet grooming professionals to network. It has a registration/login system that allows users to create and manage a personalised profile. Users can post content to promote themselves, share information and interact with other users through likes and comments. Users can also access information about upcoming events such as grooming workshops, seminars and competitions.

![GitHub Badge](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=fff&style=for-the-badge)
![Gitpod Badge](https://img.shields.io/badge/Gitpod-FFAE33?logo=gitpod&logoColor=fff&style=for-the-badge)
![Git Badge](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=fff&style=for-the-badge)
![Heroku Badge](https://img.shields.io/badge/Heroku-430098?logo=heroku&logoColor=fff&style=for-the-badge)
![PostgreSQL Badge](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=fff&style=for-the-badge)

![HTML5 Badge](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=fff&style=for-the-badge)
![CSS3 Badge](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=fff&style=for-the-badge)
![JSS Badge](https://img.shields.io/badge/JSS-F7DF1E?logo=jss&logoColor=000&style=for-the-badge)
![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=for-the-badge)
![Markdown Badge](https://img.shields.io/badge/Markdown-000?logo=markdown&logoColor=fff&style=for-the-badge)

![Bootstrap Badge](https://img.shields.io/badge/Bootstrap-7952B3?logo=bootstrap&logoColor=fff&style=for-the-badge)
![Django Badge](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=fff&style=for-the-badge)

---
## Contents
- [User Experience](#user-experience)
    + [User Stories](#user-stories)
    + [Site Goals](#site-goals)
    + [Justification](#justification)
    + [Target Audience](#target-audience)
- [UX Design](#ux-design)
    + [Wireframes](#wireframes)
    + [Colour](#colour)
    + [Fonts](#fonts)
    + [Database](#database)
    + [Models](#models)
- [Agile Methodology](#agile-methodology)
    + [Overview](#overview)
    + [EPICS](#epics)
    + [User Stories as Issues](#user-stories-as-issues)
    + [MoSCoW Prioritisation](#mosscow-prioritisation)
    + [GitHub Projects](#github-projects)
- [Features](#features)
    + [Landing Page](#landing-page)
    + [Registration/Log in](#registrationlog-in)
    + [Navigation](#navigation)
    + [User Profile](#user-profile)
    + [Posts/Home Page](#postshome-page)
    + [Events Page](#events)
    + [Log out](#log-out)
    + [Future Development](#future-development)
    + [Admin Panel](#admin-panel)
- [Testing](#testing)
- [Bugs](#bugs)
    + [Fixed Bugs](#fixed-bugs)
    + [Unfixed Bugs](#unfixed-bugs)
- [Technologies Used](#technologies-used)
    + [Languages](#languages)
    + [Frameworks](#frameworks)
    + [Database](#database)
    + [Technologies and Programs](#technologies-and-programs)
    + [Supporting Libraries and Packages](#supporting-libraries-and-packages)
- [Deployment](#deployment)
    + [ElephantSQL](#elephantsql)
    + [Cloudinary](#cloudinary)
    + [Before Deployment](#before-deployment)
    + [Deployment to Heroku](#deployment-to-heroku)
    + [Forking](#Forking)
    + [Cloning](#cloning)
- [Credits](#credits)
    + [Code](#code)
    + [Media](#media)
    + [Content](#content)
    + [Documentation and Useful Blogs](#documentation-and-useful-blogs)
    + [Acknowledgements](#acknowledgents)

---
## User Experience

### User Stories 

EPIC 1: New User Experience
- [Visually Appealing Landing Page](https://github.com/helenmurugan/the-groomers-network/issues/27) - As a Site User, I am welcomed by a visually appealing landing page with intuitive navigation so that I can select to register or sign in to the site.
- [Account Registration](https://github.com/helenmurugan/the-groomers-network/issues/5) - As a Site User, I can register for an account so that I can sign in and have access to the complete functionality of the site.
- [Immediate feedback through messages](https://github.com/helenmurugan/the-groomers-network/issues/39) - As a Site User, I can immediately receive feedback when I make changes to data so that I understand what action I have just performed.

EPIC 2: User Interaction With Posts and Comments
- [Create and Manage Posts](https://github.com/helenmurugan/the-groomers-network/issues/8) - As a Site User, I can create and manage my own posts so that I can network with other users.
- [Images](https://github.com/helenmurugan/the-groomers-network/issues/30) - As a Site User, I can upload and view images so that posts are meaningful and engaging.
- [View Posts](https://github.com/helenmurugan/the-groomers-network/issues/1) - As a Site User, I can view a list of posts so that I can click on a post to view the full content
- [Site Pagination for Posts](https://github.com/helenmurugan/the-groomers-network/issues/17) - As a Site User, I can view several posts on each page so that I can easily navigate between pages.
- [Interact Using Comments](https://github.com/helenmurugan/the-groomers-network/issues/20) - As a Site User, I can manage my comments on posts so that I can be a part of the conversation.
- [Like/Unlike Posts](https://github.com/helenmurugan/the-groomers-network/issues/7) - As a Site User, I can like or unlike a post so that I can interact with the content.

EPIC 3: Events
- [View Events](https://github.com/helenmurugan/the-groomers-network/issues/19) - As a Site User, I can view a list of events and click on an event so that I can read the full content.
- [Site Pagination for Events](https://github.com/helenmurugan/the-groomers-network/issues/37) - As a Site User, I can view several events on each page so that I can easily navigate between pages.
- [Like/Unlike Comments](https://github.com/helenmurugan/the-groomers-network/issues/3) - As a Site User, I can like or unlike an event so that I can interact with the content.
- [Create and Manage Events](https://github.com/helenmurugan/the-groomers-network/issues/35) - As a Site Admin, I can create and manage events so that they can be shared with the user.

EPIC 4: User Profiles
- [User Profile](https://github.com/helenmurugan/the-groomers-network/issues/25) - As a Site User, I can manage my profile so that I can display and update my details as necessary.
- [View Other User's Profiles](https://github.com/helenmurugan/the-groomers-network/issues/36) - As a Site User, I can click on the username of another user so that I can view their profile.

EPIC 5: Administration and Site Management
- [Site Management](https://github.com/helenmurugan/the-groomers-network/issues/16) - As a Site Admin, I can use a dedicated admin panel so that I can delete any inappropriate content and manage the content of the site.

### Site Goals
1. To provide users with a place to network with other pet grooming professionals.
3. To provide a place where users can post information such as articles, blogs or questions.
4. To provide users with the ability to interact with content through comments and likes.
2. To provide users with a place to access information about grooming events.
3. To provide users with the ability to create a personalised profile to increase their visibility within the grooming community.
5. To make the site accessible and responsive to all devices.
6. To provide administrators with the ability to manage all contents of the site.

### Justification
- Currently, professional pet groomers use private Facebook pages as a platform to ask questions to other groomers and promote events. The pages are very active and can be difficult to manage.
- The Groomer's Network provides a dedicated setting that encourages a more professional approach to networking. The majority of pet grooming professionals work alone, as small business owners, and therefore the need for this type of platform is real, to enhance professional standards through sharing of information.
- Often grooming events such as seminars, workshops, training and competitions are promoted solely on private Facebook pages which can be restrictive. The Groomer's Network provides an alternative site where all events can be listed in one place.

### Target Audience
The Groomer's Network is designed for pet grooming professionals who:
- Are committed to improving professional standards through sharing information.
- Seek to improve their knowledge and skills by attending professional events.
- Seek to network with others and raise their profile within the grooming community.
- Wish to stay updated with the latest trends, technologies and standards in their profession.

---
## UX Design
The principles of good UX design were followed when designing and creating The Groomer's Network, as detailed in this section.

### Wireframes
Wireframes were created during planning of this project using [Balsamiq Cloud](#https://balsamiq.cloud/).

* Landing Page

![Landing page wireframe](documentation/landing_page_wireframe.jpg)

* Registration Page

![Sign up wireframe](documentation/signup_wireframe.jpg)

* Login Page

![Login wireframe](documentation/login_wireframe.jpg)

* Home

![Home page wireframe](documentation/home_wireframe.jpg)

* Post Detail Page

![Post detail page wireframe](documentation/post_detail_wireframe.jpg)

* Events Page

![Event page wireframe](documentation/events_wireframe.jpg)

* Event Detail Page

![Event detail page wireframe](documentation/event_detail_wireframe.jpg)


* Profile Page

![Profile page wireframe](documentation/profile_wireframe.jpg)

### Colour
The following colours were selected for this project, with the intention of creating an environment that is calm, professional and visually appealing. The colour palette tool used during the design process was [Coolors](#https://coolors.co/).

![Colour palette](documentation/colours.jpg)

### Fonts
Lato was chosen from [Google Fonts](#https://fonts.google.com/specimen/Lato) as the font for this website. It is simple, easy to read and appropriate for a professional site.

![lato font](documentation/lato.jpg)

### Database
An entity-relationship diagram was created using [dbdiagram.io](https://dbdiagram.io).

![database schema](documentation/database.jpg)

### Models

1. User Table
    * The User model is built into Django AllAuth and is used for user authentication. 
    * Predefined fields for username, email and password come as standard. 
1. Profile Table
    * The profile model is a custom model that enables users to create a personalised profile.
    * The profile model is related to the user model with one-to-one relationship. One User can have one profile. 
    * Signals are used to automatically create a related profile when a new user is registered.
    * The profile table stores additional information that a user inputs to their profile. All profile fields except username are optional because the fields need to empty when the profile is created.
1. Post Table 
    * The post table represents posts created by users.
    * One user can be the author of many posts, a one-to-many relationship.
    * The timestamp that the post was created on and the title of the post are concatenated to form a unique slug.
    * Likes and users are related by a many-to-many relationship. A user can like many posts and a post can be liked by many users.
    * Useful information is stored in the post table and displayed to the user such as title, tagline, author, content, image and date published. 
1. Comments Table
    * The comment table enables users to comment on posts.
    * Many comments can be related to one post, a many-to-one relationship.
    * Useful information is stored in the comment table and displayed to the user such as body, author, date published.
1. Events Table
    * The event table is a custom model that represents events created by users (admin-only).
    * One user can be the author of many posts, a one-to-many relationship.
    * Likes and users are related by a many-to-many relationship. A user can like many posts and a post can be liked by many users.
    * Useful information is stored in the event table and displayed to the user such as title, tagline, content, image, date, time and location.


---
### Agile Methodology
## Overview
Agile methodologies and principles were used when planning and creating The Groomer's Network. Development was organised by working in sprints, focussed on a specific user story or stories, which could then be marked as complete. The user stories are arranged on a KanBan board, which was continuously managed throughout development to enable prioritisation of the workload.

## EPICS
Epics were used to plan the high-level bodies of work that needed to be accomplished. Customised colour-coded labels were added to user stories to show which EPICS they belong to.

EPIC 1: New User Experience

EPIC 2: User Interaction With Posts and Comments

EPIC 3: Events

EPIC 4: User Profile

EPIC 5: Administration and Site Management

## User Stories as Issues
The EPICS are broken down into user stories which are further broken down into acceptance criteria and tasks. The full list of user stories can be found in the [User Experience](#user-experience) section.

![User story](documentation/user_story.jpg)

## MoSCoW Prioritisation
Labels were added to user stories to assist with prioritisation of tasks. The MoSCoW system involves adding labels for MUST HAVE, SHOULD HAVE, COULD HAVE and WON'T HAVE. By labelling issues in such a way, the developer can focus on completing all the MUST HAVE tasks before moving onto tasks of lower priority, this is critical when working to a tight deadline to ensure a minimum viable product is completed in time.

![issues list](documentation/issues_list.jpg)

## GitHub Projects
The project was organised using a KanBan board containing columns for TO DO, IN PROGRESS, DONE and BACKLOG. The board is considered a live document, and was continuously managed between sprints to organise and prioritise workload effectively. Backlog was used to list bugs that required fixing. In future,  backlog can be used as a broad list of all items to be done, including those that are not yet scheduled for immediate action. Once ready for action, the item is pulled into TO DO, then IN PROGRESS and finally DONE when all tasks have been completed.

A link to the GitHub project board can be found [here](https://github.com/users/helenmurugan/projects/8)

![KanBan Board](documentation/kanban.jpg)

---
## Features
### Landing Page
### Registration/Log in
### Navigation
### User Profile
### Posts/Home Page
### Events Page
### Log out
### Admin Panel
### Future Development
---
## Testing

The application has been thoroughly tested and code validated. All testing documentation can be found in the separate [TESTING.md](/TESTING.md) file.

---

## Bugs
### Fixed Bugs
- search field
- slug thing

### Unfixed Bugs

---
## Technologies Used
### Languages
### Frameworks
### Database
### Technologies and Programs
### Supporting Libraries and Packages
- widget_tweaks for modifying the allauth signup form - see blog link below
---
## Deployment
### ElephantSQL
An external database was created in ElephantSQL using the following steps
1. Log in to ElephantSQL and select 'Create New Instance'
2. Select a plan, input your details and review.
3. Once created, use the copy icon to copy the DATBASE_URL.


### Cloudinary
Cloudinary was used to store static and media files.
1. Log in to Cloudinary
2. Copy your CLOUDINARY_URL

### Before Deployment
Important points for before deployment
1. The requirements for the project were added to a requirements.txt file using the command 'pip3 freeze > requirements.txt' in the terminal.
2. In .gitignore, include env.py to ensure sensitive information is not pushed to GitHub. In settings.py, link SECRET_KEY to the env.py file where the secreat key variable is defined.
3. In settings.py, set 'DEBUG = False' to prevent verbose error pages and to prevent Django serving static files itself instead of relying on Cloudinary.
4. It is necessary to make migrations and migrate the models to the database before deployment.

### Deployment to Heroku
This app was deployed to Heroku using the following steps.
1. Log in to Heroku and from the Dashboard, select 'Create New App'
2. Create a unique name for your app, and select your location.
3. Open the settings tab, Click 'Reveal Config Vars', and set the Config Vars for production (values are sensitive and have been left out). 

Config Vars for development of this project:
- DATABASE_URL
- SECRET_KEY
- PORT = 8000
- DISABLE_COLLECTSTATIC = 1
- CLOUDINARY_URL

Config Vars for production:
- DATABASE_URL
- SECRET_KEY
- CLOUDINARY_URL

4. Click 'Add buildpack'. The buildpacks will install further dependencies that are not included in the requirements.txt. For this project, the buildpack required is Python.
5. Select the Deploy tab. You can select to view build log to watch the project being built.
6. When successfully built, a message appears in the build log showing the URL'https://the-groomers-network-96ece9118f5d.herokuapp.com/ deployed to Heroku'. 
7. Click 'Open App' or 'View' to open the deployed app.

### Forking
1. From the GitHub repository, click on 'Fork', 'Create a Fork'
2. Change the name and description of the fork as required.
3. Select to copy only the main branch or copy all branches.
4. Click 'Create a Fork'. A new repository will appear in your GitHub repositories if successful.

### Cloning
1. From the GitHub repository, click 'Code' and copy the link.
1. Open git bash and change the working directory to the desired location.
1. Enter 'git clone' and paste the link.
1. Press Enter to create your local clone.
---
## Credits
### Code
- Boilerplate code, navbar and footer code modified from Code Institute's walkthrough blog project.
- Signals code was taken and modified from Juliia Konovalova's [e-commerce project](https://github.com/IuliiaKonovalova/e-commerce).
- The code for 'get_success_url' function was taken and modified from Kim Bergstroem's [PP4 project](https://github.com/KimBergstroem/PP4).


### Media
- Favicon was created using [Favicon.io](https://favicon.io/favicon-generator/)
- Dog image was taken from [rawpixel](https://www.rawpixel.com/) (id-12054680)

### Content
- Event and Post details taken from:
    - [The SouthEast Grooming Show](#https://wildwash.co.uk/event/the-south-east-grooming-show-2024/)
    - [The Dog Grooming Academy](#https://allevents.in/org/the-dog-grooming-academy/23332180)
    - [GroomFest](#https://groomfest.co.uk/)
    - [Gov.uk](#https://www.gov.uk/government/news/new-legal-restrictions-on-xl-bully-dog-now-in-force)
    - [Groomer's Choice Blog](#https://blog.groomerschoice.com/5-tips-for-new-competitive-groomers)
    - [Groomers](#https://www.groomers-online.com/blog/2022/09/what-is-competitive-dog-grooming-all-about/)
    - [Total Grooming Magazine](#https://totalgroomingmagazine.co.uk/groomers-of-the-month-emma-darlington/)
    - [Care of Pet Professionals](#https://careofpetprofessionals.co.uk/)

### Documentation and Useful Blogs
The following documentation, blogs, tutorials and guides were used to aid development.
- [Bootstrap documentation](https://getbootstrap.com/docs/4.1/getting-started/introduction/)
- [Django documentation](https://docs.djangoproject.com/en/5.0/)
- [Built with Django Blog](https://builtwithdjango.com/blog/styling-authentication-pages)
- [Sentry](https://sentry.io/welcome/)
- [Stack Overflow - Bootstrap Nav](https://stackoverflow.com/questions/25044370/make-clicked-tab-active-in-bootstrap)
- [Stack Overflow - Crispy Forms](https://stackoverflow.com/questions/11472495/remove-labels-in-a-django-crispy-forms)
- [Stack Overflow - User Profile](https://stackoverflow.com/questions/33724344/how-can-i-display-a-user-profile-using-django)
- [Widget Tweaks Documentation](https://pypi.org/project/django-widget-tweaks/)

### Acknowledgments
- Excellent mentoring and expert guidance from Juliia Konovalova and Spencer Barriball
- Inspiration on structure and design of templates taken from Kim Bergstroem's PP4 Gamer's Insight blog project.






 


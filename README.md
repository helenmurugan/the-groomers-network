# The Groomer's Network

Developer: [Helen Murugan](https://github.com/helenmurugan)<br>
Deployed website: [Link to website](https://.com)<br>

![Main image](documentation/readme_landing_page.jpg)

The Groomer's Network is a professional networking site that allows pet grooming professionals to network and access information about upcoming events. It has a registration/login system and allows users to create, read and update a personalised profile. Users can create, read, update and delete thir own posts, comment on posts, delete their own comments and view upcoming events.

Currently, pet grooming professionals use private Facebook groups to network and promote events. There are many such groups covering a diverse range of themes, some of which are very active. Events such as grooming competitions, workshops and seminars are often promoted only on these private Facebook groups which can be restrictive. The Groomer's Network provides a dedicated setting that encourages a professional approach to networking. The majority of pet grooming professionals work alone, as small business owners, and therefore the need for this type of platform is real, to enhance professional standards through sharing of information and to avoid isolation in this profession.


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
- [Project Goals](#project-goals)
    + [User Goals](#user-goals)
    + [Site Owner Goals](#site-owner-goals)
    + [Target Audience](#target-audience)
    + [User Stories](#user-stories)
- [Planning](#planning)
    + [Agile methodology](#agile-methodology)
    + [Database](#database)
    + [Wireframes](#wireframes)
- [Design](#design)
    + [Colour](#colour)
    + [Fonts](#fonts)
    + [Structure](#structure)
- [Features](#features)
    + [Landing Page](#landing-page)
    + [Posts/Home Page](#postshome-page)
    + [Events Page](#events)
    + [User Profile](#user-profile)
    + [Registration/Log in](#registrationlog-in)
    + [Navigation](#navigation)
    + [Future Development](#future-development)
-[Testing](#testing)
-[Bugs](#bugs)
    + [Fixed Bugs](#fixed-bugs)
    + [Unfixed Bugs](#unfixed-bugs)
- [Technologies Used](#technologies-used)
    + [Languages](#languages)
    + [Frameworks](#frameworks)
    + [Database](#database)
    + [Technologies and Programs](#technologies-and-programs)
    + [Supporting Libraries and Packages](#supporting-libraries-and-packages)
- [Deployment](#deployment)
    + [Before Deployment](#before-deployment)
    + [Deployment on Heroku](#deployment-on-heroku)
    + [Forking](#Forking)
    + [Cloning](#cloning)
- [Credits](#credits)
    + [Code](#code)
    + [Media](#media)
    + [Content](#content)
    + [Documentation and Useful Blogs](#documentation-and-useful-blogs)
    + [Acknowledgements](#acknowledgents)


## Project Goals
### User Goals
### Site Owner Goals
### Target Audience

The target audience for this website is all pet grooming professionals.

### User Stories 

Epic 1: New User Experience
- [Visually Appealing Landing Page](https://github.com/helenmurugan/the-groomers-network/issues/27) - As a Site User, I am welcomed by a visually appealing landing page with intuitive navigation so that I can select to register or sign in to the site.
- [Account Registration](https://github.com/helenmurugan/the-groomers-network/issues/5) - As a Site User, I can register for an account so that I can sign in and have access to the complete functionality of the site.

Epic 2: User Interaction With Posts and Comments
- [Create and Manage Posts](https://github.com/helenmurugan/the-groomers-network/issues/8) - As a Site User, I can create and manage my own posts so that I can network with other users.
- [Images](https://github.com/helenmurugan/the-groomers-network/issues/30) - As a Site User, I can upload and view images so that posts are meaningful and engaging.
- [View Posts](https://github.com/helenmurugan/the-groomers-network/issues/1) - As a Site User, I can view a list of posts so that I can click on a post to view the full content
- [Site Pagination for Posts](https://github.com/helenmurugan/the-groomers-network/issues/17) - As a Site User, I can view several posts on each page so that I can easily navigate between pages.
- [Interact Using Comments](https://github.com/helenmurugan/the-groomers-network/issues/20) - As a Site User, I can manage my comments on posts so that I can be a part of the conversation.
- [Like/Unlike Posts](https://github.com/helenmurugan/the-groomers-network/issues/7) - As a Site User, I can like or unlike a post so that I can interact with the content.


Epic 3: Events
- [View Events](https://github.com/helenmurugan/the-groomers-network/issues/19) - As a Site User, I can view a list of events and click on an event so that I can read the full content.
- [Site Pagination for Events](https://github.com/helenmurugan/the-groomers-network/issues/37) - As a Site User, I can view several events on each page so that I can easily navigate between pages.
- [Like/Unlike Comments](https://github.com/helenmurugan/the-groomers-network/issues/3) - As a Site User, I can like or unlike an event so that I can interact with the content.
- [Create and Manage Events](https://github.com/helenmurugan/the-groomers-network/issues/35) - As a Site Admin, I can create and manage events so that they can be shared with the user.

Epic 4: User Profiles
- [User Profile](https://github.com/helenmurugan/the-groomers-network/issues/25) - As a Site User, I can manage my profile so that I can display and update my details as necessary.
- [View Other User's Profiles](https://github.com/helenmurugan/the-groomers-network/issues/36) - As a Site User, I can click on the username of another user so that I can view their profile.

Epic 5: Administration and Site Management
- [Site Management](https://github.com/helenmurugan/the-groomers-network/issues/16) - As a Site Admin, I can use a dedicated admin panel so that I can delete any inappropriate content and manage the content of the site.

## Planning

### Agile Methodology 

### Database
Profile Table
Post Table
Events Table
Comments Table

### Wireframes

## Design

### Colour
### Fonts
### Structure



## Features
### Landing Page
### Posts/Home Page
### Events Page
### User Profile
### Registration/Log in
### Navigation
### Future Development

## Testing
The application has been thoroughly tested and code validated. All testing documentation can be found in the separate [testing.md](testing.md) file.

## Bugs
### Fixed Bugs
### Unfixed Bugs

## Technologies Used
### Languages
### Frameworks
### Database
### Technologies and Programs
### Supporting Libraries and Packages
- widget_tweaks for modifying the allauth signup form - see blog link below

## Deployment
### Before Deployment
### Deployment on Heroku
### Forking
### Cloning

## Credits
### Code
- Boilerplate code, navbar and footer code modified from Code Institute's walkthrough blog project.
- Signals code taken modified from Juliia Konovalova's PP5 e-commerce project.
- 'get_success_url' taken from Kim Bergstroem's PP4 blog project.


### Media
- https://favicon.io/favicon-generator/
### Content
### Documentation and Useful Blogs
- Bootstrap
- Django
- https://builtwithdjango.com/blog/styling-authentication-pages
- https://sentry.io/answers/how-do-i-auto-resize-an-image-to-fit-a-div-container/#:~:text=To%20fix%20this%2C%20we%20can,contain%E2%80%9D%20and%20%E2%80%9Ccover%E2%80%9D.
- https://stackoverflow.com/questions/25044370/make-clicked-tab-active-in-bootstrap
- https://stackoverflow.com/questions/11472495/remove-labels-in-a-django-crispy-forms
- https://stackoverflow.com/questions/33724344/how-can-i-display-a-user-profile-using-django
### Acknowledgents
- Excellent mentoring and expert guidance from Juliia Konovalova
- Inspiration on structure and design of templates taken from Kim Bergstroem Gamer's Insight blog project.






 


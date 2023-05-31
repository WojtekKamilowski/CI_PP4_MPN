# My Pantry Note
(Developer: Kamil Wojciechowski)

![Mockup image](docs/responsive.png)

[Live webpage](https://mypantrynote.herokuapp.com/)

## About 

My Pantry Note - 4th Portfolio Project for Diploma in Full Stack Software Development with Code Institute. It is a full stack website built using Django to help users keep track of their food stock at home. The idea was inspired by the hardships of the cost of living crisis to provide for users a simple mean useful in avoiding spending money for food products that often may expire and be wasted before consumers want to eat them. 

## Table of Contents

- [My Pantry Note](#my-pantry-note)
  - [About](#about)
  - [Table of Contents](#table-of-contents)
  - [Project Goals](#project-goals)
    - [User Goals](#user-goals)
    - [Business Owner Goals](#business-owner-goals)
  - [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Requirements and Expectations](#user-requirements-and-expectations)
    - [User Stories](#user-stories)
      - [Users](#users)
      - [Site Owner](#site-owner)
    - [Agile Methodologies](#agile-methodologies)
  - [Design](#design)
    - [Colors](#colors)
    - [Fonts](#fonts)
    - [Structure](#structure)
    - [Wireframes](#wireframes)
  - [Database Diagram](#database-diagram)
  - [Messages and Interaction With Users](#messages-and-interaction-with-users)
  - [Admin Panel/Superuser](#admin-panelsuperuser)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Libraries & Frameworks](#libraries--frameworks)
    - [Django Packages](#django-packages)
  - [Features](#features)
  - [Validation](#validation)
  - [Accessibility](#accessibility)
  - [Performance](#performance)
  - [Device Testing](#device-testing)
  - [Browser compatibility](#browser-compatibility)
  - [Testing](#testing)
    - [Automated Testing](#automated-testing)
    - [Manual Testing](#manual-testing)
  - [Creating the app using Django](#creating-the-app-using-django)
  - [Bugs](#bugs)
  - [Deployment](#deployment)
  - [Credits](#credits)
    - [Media](#media)
  - [Further Development](#further-development)
  - [Acknowledgements](#acknowledgements)

## Project Goals

### User Goals
- Control stock levels of food at home.
- Reduce food waste.
- Reduce money waste.
- Avoid leaving expired food in storage areas.
- Better plan where to store food according to temperature requirements.
- Easy navigation through the website.
- Ask questions or provide feedback for the website owner by using the contact form.
- Find social media of the website to find more content about saving food and network with other users.

### Business Owner Goals
- Allow users to organize information about stored food in storagespaces.
- Provide users with a simple application helping to reduce food waste.
- Help users to better organize their food storage.
- Collect feedback or answer questions from the users by using the contact form.
- Allow users to easily visit social media pages of the owner.


[Back to Table Of Contents](#table-of-contents)

## User Experience

### Target Audience
- People who would like to reduce costs of living by avoiding buying groceries in excess.
- Users who would like to have better control where they store their food.
- People who like to plan their grocery shopping to easier buy what is needed.

[Back to Table Of Contents](#table-of-contents)

### User Requirements and Expectations
- Accessible and responsive website.
- Intuitive website with a layout allowing to easily navigate through it.
- Easy access to Create, Read, Update & Delete information.
- Links and features that function in accordance with their intended purpose.
- Connection with the community on the social media platforms.
- A contact form to contact the website owner.

[Back to Table Of Contents](#table-of-contents)

### User Stories

#### Users

As a User I want to:

1. Register an account.
2. Login.
3. View the food stock list.
4. Add a new storage space.
5. Add a new stock item.
6. Update a stock item.
7. Remove an item from the stock list.
8. Contact Site's Admin.
9. See items are expired.
10. See items that have different temperature range than in the storage.
11. Easily navigate on the website.

[Back to Table Of Contents](#table-of-contents)

#### Site Owner

As an Admin I want to:

12. Access admin panel.
13. Review messages sent by users.
14. Manage messages sent by users.
15. Deliver an intuitive website for the users.


[Back to Table Of Contents](#table-of-contents)

### Agile Methodologies

<a href="https://github.com/users/WojtekKamilowski/projects/2/views/1">Github Project</a>

<a href="https://github.com/WojtekKamilowski/CI_PP4_MPN/issues">User Stories</a>

<details>
    <summary>Kanban</summary>
    
![Kanban](docs/agile/kanban-1.png)
![Kanban](docs/agile/kanban-2.png)
![Kanban](docs/agile/kanban-3.png)
![Kanban](docs/agile/kanban-4.png)
![Kanban](docs/agile/kanban-5.png)
![Kanban](docs/agile/kanban-6.png)
![Kanban](docs/agile/kanban-7.png)
![Kanban](docs/agile/kanban-8.png)
![Kanban](docs/agile/kanban-9.png)


</details>

[Back to Table Of Contents](#table-of-contents)

## Design

### Design Choices

The main theme was to create a simple website to help users keep their food storage organized and under control. 
The users can organize their lists into different storage spaces that can be useful to find the items, for exmaple in the physical locations when cooking or check stock levels on mobile devices during shopping. The logo is a clipboard list which is to inform user of the main purpose of this website: list food items. The name: MyPantryNote relates to personalized service where users can keep record of their own food stock, the lst word note was chosen to highlight the simplicity of the idea. Design of all elements of the website represent a message for users that controlling stock levels can be easy using an intuitive website.

### Colors

The main color of the website is green #7EC63F that is to represent nature & organic harmony to relate reducing waste as a way into more sustainable way of living for an individual user.
There is also tone of yellow, kept in the natural/ organic food theme to differentiate certain elements of the website.
Error messages are in white with red background to break from the color theme and clearly inform the user that something went wrong .

- #7EC63F from <a href="https://coolors.co/contrast-checker/000000-7ec63f">Coolors</a>.
<details>
    <summary>Contrast</summary> 

![Colors](docs/colors/contrast-green-black.png)

</details>

- #C8D363 from <a href="https://coolors.co/contrast-checker/000000-defdc3">Coolors</a>.

<details>
    <summary>Contrast</summary> 

![Colors](docs/colors/contrast-lgreen-black.png)

</details>

- #55D54E from <a href="https://coolors.co/contrast-checker/000000-55d54e">Coolors</a>.

<details>
    <summary>Contrast</summary> 

![Colors](docs/colors/contrast-dgreen-black.png)

</details>

- #CCC731 from <a href="https://coolors.co/contrast-checker/000000-ccc731">Coolors</a>.

<details>
    <summary>Contrast</summary> 

![Colors](docs/colors/contrast-yellow-black.png)

</details>

- #CAF3C8 from <a href="https://coolors.co/contrast-checker/000000-caf3c8">Coolors</a>. 

<details>
    <summary>Contrast</summary> 

![Colors](docs/colors/contrast-llgreen-black.png)

</details>

- #9B0000 from <a href="https://coolors.co/contrast-checker/ffffff-9b0000">Coolors</a>.

<details>
    <summary>Contrast</summary> 

![Colors](docs/colors/contrast-red-white.png)

</details>

- #C3CFB2 from <a href="https://coolors.co/contrast-checker/000000-c3cfb2">Coolors</a>.

<details>
    <summary>Contrast</summary> 

![Colors](docs/colors/contrast-graygreen-black.png)

</details>

[Back to Table Of Contents](#table-of-contents)

### Fonts

_Fira Sans_ was chosen as the main font with _Sans-serif_ as the fallback font. For h1, h2 & .nav-item elements it was _PT Serif_ with _Serif_ as the fallback font.
Fonts found on Google Fonts.

[Back to Table Of Contents](#table-of-contents)


### Structure

The website consists of two django applications: stocklist & contact. The content of the website is placed in the center. The logo and the name of the website is placed on the top, the main container in the middle and the footer placed on the bottom. There are four icons in the footer: three with links to social media platforms and envelope linking to the contact page of the website.

There is base.html that contains main structure of the website, the navbar &  the footer.

Stocklist app has 13 pages:

- index.html - home page containing some info about the website.
- list.html - its main part with options to create(add_stocklist.html), edit(edit_stocklist.html) or delete(delete_list.html) user's stocklist and naviagate to spaces.html
- spaces.html - contains list of created storagespaces and a button to create a new storage space(add_storage.html). 
- items.html - this is where after clicking on a storagespace, users can view items in the chosen storagespace and click on edit(edit_storage.html, edit_item.html) or delete(delete_storage.html, delete_item.html) options for storagespace itself or its items or add a new item(add_item.html).

Contact app contains 2 pages:

- contact.html with contact form
- received.html with a short confirmation for users after submitting the contact form.

There are also a few customised pages related to user's authentication option with Alluath:

- login.html
- logout.html
- password_change.html
- password_reset.html
- password_reset_done.html
- signup.html

### Wireframes

<details>
    <summary>Desktop</summary> 

![Wireframes](docs/wireframes/1.a-home-notloggedin-desktop.png)
![Wireframes](docs/wireframes/2.b-register-desktop.png)
![Wireframes](docs/wireframes/3.c-login-desktop.png)
![Wireframes](docs/wireframes/3.cc-password-reset-desktop.png)
![Wireframes](docs/wireframes/3.ccc-password-reset-done-desktop.png)
![Wireframes](docs/wireframes/4.d-home-loggedin-desktop.png)
![Wireframes](docs/wireframes/4.dd-change-password-desktop.png)
![Wireframes](docs/wireframes/5.e-nostocklist-desktop.png)
![Wireframes](docs/wireframes/6.f-create-stocklist-desktop.png)
![Wireframes](docs/wireframes/6.f-spaces-desktop.png)
![Wireframes](docs/wireframes/7.g-create-storage-desktop.png)
![Wireframes](docs/wireframes/7.g-stocklist-desktop.png)
![Wireframes](docs/wireframes/7.gg-create-item-desktop.png)
![Wireframes](docs/wireframes/7.gg-edit-stocklist-desktop.png)
![Wireframes](docs/wireframes/7.ggg-delete-stocklist-desktop.png)
![Wireframes](docs/wireframes/8.h-items-desktop.png)
![Wireframes](docs/wireframes/8.hh-edit-storage-desktop.png)
![Wireframes](docs/wireframes/8.hhh-delete-storage-desktop.png)
![Wireframes](docs/wireframes/8.hhhh-edit-item-desktop.png)
![Wireframes](docs/wireframes/8.hhhhh-delete-item-desktop.png)
![Wireframes](docs/wireframes/9.i-contact-desktop.png)
![Wireframes](docs/wireframes/10.j-received-desktop.png)
![Wireframes](docs/wireframes/10.jj-logout-desktop.png)
![Wireframes](docs/wireframes/11.k-error-desktop.png)

</details>

[Back to Table Of Contents](#table-of-contents)

<details>
    <summary>Tablet</summary> 

![Wireframes](docs/wireframes/12.l-home-tablet.png)
![Wireframes](docs/wireframes/13.m-register-tablet.png)
![Wireframes](docs/wireframes/14.n-login-tablet.png)
![Wireframes](docs/wireframes/14.nn-reset-password-tablet.png)
![Wireframes](docs/wireframes/14.nnn-reset-password-done-tablet.png)
![Wireframes](docs/wireframes/15.o-home-loggedin-tablet.png)
![Wireframes](docs/wireframes/15.oo-change-password-tablet.png)
![Wireframes](docs/wireframes/16.p-nostocklist-tablet.png)
![Wireframes](docs/wireframes/17.r-create-stocklist-tablet.png)
![Wireframes](docs/wireframes/18.s-stocklist-tablet.png)
![Wireframes](docs/wireframes/18.ss-edit-stocklist-tablet.png)
![Wireframes](docs/wireframes/18.sss-delete-stocklist-tablet.png)
![Wireframes](docs/wireframes/19.t-spaces-tablet.png)
![Wireframes](docs/wireframes/20.u-create-storage-tablet.png)
![Wireframes](docs/wireframes/20.uu-create-item-tablet.png)
![Wireframes](docs/wireframes/21.v-items-tablet.png)
![Wireframes](docs/wireframes/21.vv-edit-storage-tablet.png)
![Wireframes](docs/wireframes/21.vvv-delete-storage-tablet.png)
![Wireframes](docs/wireframes/21.vvvv-edit-item-tablet.png)
![Wireframes](docs/wireframes/21.vvvvv-delete-item-tablet.png)
![Wireframes](docs/wireframes/22.w-contact-tablet.png)
![Wireframes](docs/wireframes/23.y-received-tablet.png)
![Wireframes](docs/wireframes/23.yy-logout-tablet.png)
![Wireframes](docs/wireframes/24.z-error-tablet.png)

</details>

[Back to Table Of Contents](#table-of-contents)

<details>
    <summary>Mobile</summary> 

![Wireframes](docs/wireframes/25.aa-home-mobile.png)
![Wireframes](docs/wireframes/26.bb-register-mobile.png)
![Wireframes](docs/wireframes/27.cc-login-mobile.png)
![Wireframes](docs/wireframes/27.ccc-reset-password-mobile.png)
![Wireframes](docs/wireframes/27.cccc-reset-password-done-mobile.png)
![Wireframes](docs/wireframes/28.dd-home-loggedin-mobile.png)
![Wireframes](docs/wireframes/28.ddd-change-password-mobile.png)
![Wireframes](docs/wireframes/29.ee-nostocklist-mobile.png)
![Wireframes](docs/wireframes/30.ff-create-stocklist-mobile.png)
![Wireframes](docs/wireframes/31.gg-stocklist-mobile.png)
![Wireframes](docs/wireframes/31.ggg-edit-stocklist-mobilepng)
![Wireframes](docs/wireframes/31.gggg-delete-stocklist-mobile.png)
![Wireframes](docs/wireframes/32.hh-spaces-mobile.png)
![Wireframes](docs/wireframes/33.ii-create-storage-mobile.png)
![Wireframes](docs/wireframes/33.iii-create-item-mobile.png)
![Wireframes](docs/wireframes/34.jj-items-mobile.png)
![Wireframes](docs/wireframes/34.jjj-edit-storage-mobile.png)
![Wireframes](docs/wireframes/34.jjjj-delete-storage-mobile.png)
![Wireframes](docs/wireframes/34.jjjjj-edit-item-mobile.png)
![Wireframes](docs/wireframes/34.jjjjjj-delete-item-mobile.png)
![Wireframes](docs/wireframes/35.kk-contact-mobile.png)
![Wireframes](docs/wireframes/36.ll-received-mobile.png)
![Wireframes](docs/wireframes/36.lll-logout-mobile.png)
![Wireframes](docs/wireframes/37.mm-error-mobile.png)

</details>

[Back to Table Of Contents](#table-of-contents)

## Database Diagram

- Stocklist:

![Database Diagram](docs/database/stocklist.png)

- Contact:

![Database Diagram](docs/database/contact.png)

[Back to Table Of Contents](#table-of-contents)

## Messages and Interaction With Users

<details>
    <summary>Messages updating the user on interactions status.</summary> 

- Login
![Messages and Interaction With Users](docs/messages/login.png)
- Stocklist added
![Messages and Interaction With Users](docs/messages/stocklist-added.png)
- Stocklist edit
![Messages and Interaction With Users](docs/messages/stocklist-edit.png)
- Stocklist delete
![Messages and Interaction With Users](docs/messages/stocklist-delete.png)
- Storage add
![Messages and Interaction With Users](docs/messages/storage-add.png)
- Storage edit
![Messages and Interaction With Users](docs/messages/storage-edit.png)
- Storage delete
![Messages and Interaction With Users](docs/messages/storage-delete.png)
- Item add
![Messages and Interaction With Users](docs/messages/item-add.png)
- Item edit
![Messages and Interaction With Users](docs/messages/item-edit.png)
- Item delete
![Messages and Interaction With Users](docs/messages/item-delete.png)
- Message sent
![Messages and Interaction With Users](docs/messages/message-sent.png)
- Password change
![Messages and Interaction With Users](docs/messages/password-change.png)
- Sign out
![Messages and Interaction With Users](docs/messages/sign-out.png)

</details>

[Back to Table Of Contents](#table-of-contents)

## Admin Panel/Superuser

On Admin Panel, admin/ superuser has full access to CRUD functionality to control users' stocklists, status or to address messages sent via the contact form.

![Admin Panel/Superuser](docs/admin/admin.png)
![Admin Panel/Superuser](docs/admin/user.png)
![Admin Panel/Superuser](docs/admin/contact.png)

[Back to Table Of Contents](#table-of-contents)

## Technologies Used

- [GitHub](https://github.com/)
- [Gitpod](https://gitpod.io/)
- [Codeanywhere](https://app.codeanywhere.com/)
- [Heroku](https://id.heroku.com/)
- [Lucidchart](https://lucid.app/)
- [Fontawesome](https://fontawesome.com/)
- [Google Fonts](https://fonts.google.com/?fbclid=IwAR0M5mybiiO6URy8GMzAKIYHRdX_lQHlJhwcmI6h-bNFuL90-osnCNZaC8Q)
- [Balsamiq](https://balsamiq.com/)
- [CI Python Linter](https://pep8ci.herokuapp.com/)
- [TinyPNG](https://tinypng.com/)
- [jQuery](https://jquery.com/)
- [WAVE](https://wave.webaim.org/)
- [amiresponsive?](https://ui.dev/amiresponsive?)

[Back to Table Of Contents](#table-of-contents)

### Languages

- HTML5
- CSS3
- JavaScript
- Python

[Back to Table Of Contents](#table-of-contents)

### Libraries & Frameworks

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)

[Back to Table Of Contents](#table-of-contents)

### Django Packages

- [Cloudinary](https://cloudinary.com/)
- [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
- [Summernote](https://summernote.org/)

[Back to Table Of Contents](#table-of-contents)

## Features

<details>

<summary>Logo and Website Name</summary>

It is included on all pages.
The logo includes an icon. The logo and the website name are clickable link to Home page which is a common feature on many websites so users expect it.
Logo and website name are responsive, the font size reduces for smaller screens.
User stories covered: 11, 15.

![Features](docs/features/logo-name.png)

</details>

<details>

<summary>Navigation Bar</summary>

Appears on all pages.
When user is not loggedin contains links to navigate to Home, Register or Login pages.
If the user is authenticated displays options to navigate to the home, main stocklist, password change or logout.
Reflects to the user about the current login state by displaying user's name.
User stories covered: 11, 15.

![Features](docs/features/nav-bar.png)
![Features](docs/features/nav-bar-loggedin.png)

</details>

<details>

<summary>Footer</summary>

Appears on all pages.
Contains icons with links to Facebook, Pinterest, Youtube & the contact page.
User stories covered: 8, 11, 15.

![Features](docs/features/footer.png)

</details>

<details>

<summary>Register</summary>

It is included on signup.html
Taken from Allauth & customised.
Allows user to register an account using own username & password with an optional input of user's email address.
Gives user an option to navigate to login page if the user already created own account.
User stories covered: 1, 11, 15.

![Features](docs/features/register.png)

</details>

<details>

<summary>Login</summary>

It is included on login.html
Taken from Allauth & customised.
Allows user to login to the earlier created account by giving the username & password with an option to remember username.
Gives user an option to navigate to the password reset page if the user forgot the password or to the register page if user has not created an account yet.
User stories covered: 2, 11, 15.

![Features](docs/features/login.png)

</details>

<details>

<summary>Password Reset</summary>

It is included on password_reset.html  

Taken from Allauth & customised.  
Requests user’s email address (if given during the registration) to send user an Allauth email with a link allowing password reset. It has a link to the contact page so the user can interact with the site’s admin in case Allauth’s solution fails or there are any problems.  
User stories covered: 2, 11, 15. 

![Features](docs/features/password-reset.png)

</details>

<details>

<summary>Password Change</summary>

It is included on password_change.html 
Taken from Allauth & customised. 
User can change the current password to a new password. 
User stories covered: 2, 11, 15. 

![Features](docs/features/password-change.png)

</details>

<details>

<summary>Our Mission Box</summary>

Appears in the center of the home page.
Displays info about the website, giving some background to the user what this application is for. 
Includes links to the signup & login pages when user is not authenticated or to the main stocklist page(list.html) when the user is logged-in. 
User stories covered: 3, 11, 15.

![Features](docs/features/mission.png)
![Features](docs/features/mission-loggedin.png)

</details>

<details>

<summary>Main Stocklist Page</summary>

Central element list.html
If there is no stocklist already created it displays an option to create a new stocklist.
In case the user already created own stocklist with a chosen stocklist name, it gives options to edit or delete the stocklist and displays the link to the storage spaces list.
User stories covered: 3, 11, 15.

![Features](docs/features/list.png)
![Features](docs/features/list-created.png)

</details>

<details>

<summary>Storage Spaces List</summary>

Main part of spaces.html
It shows list of all storage spaces in user's stocklist and displays an option to create a new storage space.
Storagespaces names contain links to view the details including items table.
User stories covered: 4, 11, 15.

![Features](docs/features/spaces.png)

</details>

<details>

<summary>Storagespace Details & Items Table</summary>

Appears in the center of items.html
Allows user to edit or delete the storagespace.
Informs the user about the temperature in the storagespace & when it was last time updated.
Allows user to read list of all items in the storagespace. Items on the list that are expired or will expire next day have highlited expiry date in orange.
Items requiring lower temperature have temp. range highlighted in red & items that can be in a warmer environment have highlighted temp. range in blue.
The items table includes options to edit or delete item of the selected row.
Below the items table there is element navigating to the create a new item form.
User stories covered: 3, 5, 6, 7, 9, 10, 11, 15.

![Features](docs/features/items.png)

</details>

<details>

<summary>Contact</summary>

Central part of the contact page.
Contains a contact form allowing user to submit a message to site's admins.
If user is authenticated it automatically takes user's name & e-mail(if given during the registration).
Informs the user about message receipt after submitting the message.
User stories covered: 8, 11, 15.

![Features](docs/features/contact.png)
![Features](docs/features/received.png)

</details>

<details>

<summary>Logout</summary>

Taken from Allauth & customised.
Positioned in the center of logout.html appears after clicking Logout in the navbar.
Asks the user to confirm the choice of logging out.
User stories covered: 11, 15. 


![Features](docs/features/logout.png)

</details>

<details>

<summary>Admin</summary>

From Django Admin, customised.
Included on admin page accessed on https://mypantrynote.herokuapp.com/admin
Contains following main optios for the superuser:

- review Users, 
- change user's password
- read user's messages sent via the contact feature
- manage stocklists, storagespaces & stockitems

User stories: 12, 13, 14.

![Features](docs/features/admin.png)

</details>

[Back to Table Of Contents](#table-of-contents)

## Validation

### HTML Validation

<details>
    <summary>To validate HTML of the website<a href="https://validator.w3.org/?fbclid=IwAR37NqVmxg37_tfuFOF4BJoyH8h_H-2n-Ed-64KJpoP1nEgLduNPO227mvE">the W3C Markup Validation Service</a> was used. The results have no errors.</summary>

- home
![HTML Validation](docs/validation/html/html-home.png)
- signup
![HTML Validation](docs/validation/html/html-signup.png)
- login
![HTML Validation](docs/validation/html/html-login.png)
- password_reset
![HTML Validation](docs/validation/html/html-password-reset.png)
- password_reset_done
![HTML Validation](docs/validation/html/html-password-reset-done.png)
- loggedin home
![HTML Validation](docs/validation/html/html-loggedin.png)
- password_change
![HTML Validation](docs/validation/html/html-password-change.png)
- list
![HTML Validation](docs/validation/html/html-list.png)
- add_stocklist
![HTML Validation](docs/validation/html/html-add-stocklist.png)
- added list 
![HTML Validation](docs/validation/html/html-list-added.png)
- edit_stocklist
![HTML Validation](docs/validation/html/html-edit-stocklist.png)
- delete_stocklist
![HTML Validation](docs/validation/html/html-delete-stocklist.png)
- spaces
![HTML Validation](docs/validation/html/html-spaces.png)
- items
Warning of possible misuse of aria-label: aria-label added to fix an accessibility error "Empty table header"
![HTML Validation](docs/validation/html/html-items.png)
![HTML Validation](docs/validation/html/html-items-accessibility.png)
- add_storage
![HTML Validation](docs/validation/html/html-add-storage.png)
- edit_storage
![HTML Validation](docs/validation/html/html-edit-storage.png)
- delete_storage
![HTML Validation](docs/validation/html/html-delete-storage.png)
- add_item
![HTML Validation](docs/validation/html/html-add-item.png)
- edit_item
![HTML Validation](docs/validation/html/html-edit-item.png)
- delete_item
![HTML Validation](docs/validation/html/html-delete-item.png)
- logout
![HTML Validation](docs/validation/html/html-logout.png)
- contact
![HTML Validation](docs/validation/html/html-contact.png)
- received
![HTML Validation](docs/validation/html/html-received.png)
- error
![HTML Validation](docs/validation/html/html-error.png)

</details>

[Back to Table Of Contents](#table-of-contents)

### CSS Validation

<details>
    <summary>To validate style.css <a href="https://jigsaw.w3.org/css-validator/?fbclid=IwAR2zBUIZHTXAGa9KEvR__gsTkB05ZifTcd-us-pR0Kud0bLVaIPET-V-Hi4#validate_by_upload">the W3C Jigsaw CSS Validation Service</a> was used. There were no errors found.</summary>

![CSS Validation](docs/validation/css/style.png)

</details>

[Back to Table Of Contents](#table-of-contents)

### JavaScript Validation

<a href="https://jshint.com/">JSHint</a> JS Validation Serviced was used to validate the Javascript code for the website with no major issues found.
Two undefined variables message appears for jQuery $ sign & bootstrap.

![JavaScript Validation](docs/validation/js/js.png)

### PEP8 Validation

<details>
    <summary><a href="https://pep8ci.herokuapp.com">CI Python Linter</a> was used to perform the check if the code meets PEP8 requirements. All clear, no errors found:</summary>

- urls.py
![PEP8 Validation](docs/validation/pep8/urls.png)
- stocklist: admin.py
![PEP8 Validation](docs/validation/pep8/stocklist-admin.png)
- stocklist: models.py
![PEP8 Validation](docs/validation/pep8/stocklist-models.png)
- stocklist: urls.py
![PEP8 Validation](docs/validation/pep8/stocklist-urls.png)
- stocklist: views.py
![PEP8 Validation](docs/validation/pep8/stocklist-views.png)
- stocklist: forms.py
![PEP8 Validation](docs/validation/pep8/stocklist-forms.png)
- stocklist: test_models.py
![PEP8 Validation](docs/validation/pep8/stocklist-test_models.png)
- contact: admin.py
![PEP8 Validation](docs/validation/pep8/contact-admin.png)
- contact: models.py
![PEP8 Validation](docs/validation/pep8/contact-models.png)
- contact: urls.py
![PEP8 Validation](docs/validation/pep8/contact-urls.png)
- contact: views.py
![PEP8 Validation](docs/validation/pep8/contact-views.png)
- contact: forms.py
![PEP8 Validation](docs/validation/pep8/contact-forms.png)

</details>

[Back to Table Of Contents](#table-of-contents)

## Accessibility

<details>
    <summary>WAVE</summary> 

![Accessibility](docs/accessibility/wave-404.png)
![Accessibility](docs/accessibility/wave-500.png)
![Accessibility](docs/accessibility/wave-add-item.png)
![Accessibility](docs/accessibility/wave-add-storage.png)
![Accessibility](docs/accessibility/wave-contact.png)
![Accessibility](docs/accessibility/wave-create-list.png)
![Accessibility](docs/accessibility/wave-delete-item.png)
![Accessibility](docs/accessibility/wave-delete-stocklist.png)
![Accessibility](docs/accessibility/wave-edit-item.png)
![Accessibility](docs/accessibility/wave-edit-stocklist.png)
![Accessibility](docs/accessibility/wave-highlights.png)
![Accessibility](docs/accessibility/wave-home-loggedin.png)
![Accessibility](docs/accessibility/wave-home.png)
![Accessibility](docs/accessibility/wave-items.png)
![Accessibility](docs/accessibility/wave-list-created.png)
![Accessibility](docs/accessibility/wave-list-mt.png)
![Accessibility](docs/accessibility/wave-login.png)
![Accessibility](docs/accessibility/wave-logout.png)
![Accessibility](docs/accessibility/wave-pass-reset.png)
![Accessibility](docs/accessibility/wave-pass-reset-sent.png)
![Accessibility](docs/accessibility/wave-received.png)
![Accessibility](docs/accessibility/wave-register.png)
![Accessibility](docs/accessibility/wave-spaces.png)

*There is an alert for a redundant link to the home page. It was purposely designed to be included both in the logo and in the navbar.

</details>

[Back to Table Of Contents](#table-of-contents)

## Performance

<details>
    <summary>Desktop</summary> 

- home
![Performance](docs/performance/desktop-home.png)
- signup
![Performance](docs/performance/desktop-signup.png)
- login
![Performance](docs/performance/desktop-login.png)
- password_reset
![Performance](docs/performance/desktop-password-reset.png)
- password_reset_done
![Performance](docs/performance/desktop-desktop-password-reset-done.png)
- loggedin home
![Performance](docs/performance/desktop-home-loggedin.png)
- password_change
![Performance](docs/performance/desktop-password-change.png)
- list
![Performance](docs/performance/desktop-list.png)
- add_stocklist
![Performance](docs/performance/desktop-add-stocklist.png)
- added list 
![Performance](docs/performance/desktop-list-added.png)
- edit_stocklist
![Performance](docs/performance/desktop-edit-stocklist.png)
- delete_stocklist
![Performance](docs/performance/desktop-delete-stocklist.png)
- spaces
![Performance](docs/performance/desktop-spaces.png)
- items
![Performance](docs/performance/desktop-items.png)
- add_storage
![Performance](docs/performance/desktop-add-storage.png)
- edit_storage
![Performance](docs/performance/desktop-edit-storage.png)
- delete_storage
![Performance](docs/performance/desktop-delete-storage.png)
- add_item
![Performance](docs/performance/desktop-add-item.png)
- edit_item
![Performance](docs/performance/desktop-edit-item.png)
- delete_item
![Performance](docs/performance/desktop-delete-item.png)
- logout
![Performance](docs/performance/desktop-logout.png)
- contact
![Performance](docs/performance/desktop-contact.png)

</details>

<details>
    <summary>Mobile</summary> 

- home
![Performance](docs/performance/mobile-home.png)
- signup
![Performance](docs/performance/mobile-signup.png)
- login
![Performance](docs/performance/mobile-login.png)
- password_reset
![Performance](docs/performance/mobile-password-reset.png)
- password_reset_done
![Performance](docs/performance/mobile-password-reset-done.png)
- loggedin home
![Performance](docs/performance/mobile-home-loggedin.png)
- password_change
![Performance](docs/performance/mobile-password-change.png)
- list
![Performance](docs/performance/mobile-list.png)
- add_stocklist
![Performance](docs/performance/mobile-add-stocklist.png)
- added list 
![Performance](docs/performance/mobile-list-added.png)
- edit_stocklist
![Performance](docs/performance/mobile-edit-stocklist.png)
- delete_stocklist
![Performance](docs/performance/mobile-delete-stocklist.png)
- spaces
![Performance](docs/performance/mobile-spaces.png)
- items
![Performance](docs/performance/mobile-items.png)
- add_storage
![Performance](docs/performance/mobile-add-storage.png)
- edit_storage
![Performance](docs/performance/mobile-edit-storage.png)
- delete_storage
![Performance](docs/performance/mobile-delete-storage.png)
- add_item
![Performance](docs/performance/mobile-add-item.png)
- edit_item
![Performance](docs/performance/mobile-edit-item.png)
- delete_item
![Performance](docs/performance/mobile-delete-item.png)
- logout
![Performance](docs/performance/mobile-logout.png)
- contact
![Performance](docs/performance/mobile-contact.png)

</details>

## Device Testing

List of devices used to test the website:

- HP Pavilion 14
- Acer Nitro 5 without and with an external monitor (HP V22)
- Sony Xperia L2
- Motorola Moto G20

The website was also tested using Google Chrome Developer Tools, Toggle Device Toolbar simulating view from twenty-five listed devices, including popular amongst users iPad and iPhone 5.

[Back to Table Of Contents](#table-of-contents)

## Browser compatibility

Following browsers were used to test the website:

- Google Chrome
- Mozilla Firefox
- Microsoft Edge

[Back to Table Of Contents](#table-of-contents)

## Testing

### Automated Testing

<details><summary>Automated Testing</summary>

- stocklist.test_models.py
![Automated Testing](docs/testing/auto/test_models.png)

</details>

### Manual Testing

<details><summary>Manual Testing</summary>

---------------------------------------------------------------

Testing user stories:

1. As a User I want to register an account.

| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| Register | From the navigation bar choose 'Register' fill-up the form and press Register button | User registers own account & is automatically logged in | Works as expected |

![Manual Testing](docs/testing/manual/1.png)

2. As a User I want to login.

| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| Login | | From the navigation bar choose 'Login' input registered Username & Password and press Login! button | Works as expected |
| Password Reset | Click on 'Forgot Password?' link on Login page then click 'Reset My Password', check your emails if you do not receive it for a longer time contact Site's Admin | Email from Allauth is received | Allauth feature does not work. Contacting Site's Admins alternative works as expected |

![Manual Testing](docs/testing/manual/2.png)
![Manual Testing](docs/testing/manual/2-a.png)
![Manual Testing](docs/testing/manual/2-b.png)
![Manual Testing](docs/testing/manual/2-c.png)
![Manual Testing](docs/testing/manual/2-d.png)
![Manual Testing](docs/testing/manual/2-e.png)
![Manual Testing](docs/testing/manual/2-f.png)
![Manual Testing](docs/testing/manual/2-g.png)
![Manual Testing](docs/testing/manual/2-h.png)
![Manual Testing](docs/testing/manual/2-i.png)
![Manual Testing](docs/testing/manual/2-j.png)

3. As a User I want to view the food stock list.

| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| Our Mission Box | After logging in on the home page click on 'Manage Your Pantry Now'  | Navigates to the Main Stocklist page | Works as expected |
| Main Stocklist Page | Click on User: Name or access it via Our Mission Box as per above, create stocklist if not created yet or navigate to storage spaces | Creates new stocklist | Works as expected |
| Storagespace Details & Items Table | From Main Stocklist Page, navigate to Storage Spaces using the option at the bottom of the box then click on one of the Storage Spaces created earlier an view the items displayed on the table that were earlier created and assigned to the given Storage Space | User sees stockitems in the table | Works as expected |

![Manual Testing](docs/testing/manual/3-a.png)
![Manual Testing](docs/testing/manual/3-b.png)
![Manual Testing](docs/testing/manual/3-c.png)
![Manual Testing](docs/testing/manual/3-d.png)
![Manual Testing](docs/testing/manual/3-e.png)
![Manual Testing](docs/testing/manual/3-f.png)

4. As a User I want to add a new storage space

| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| Storage Spaces List | From Home page proceed to Main Stocklist Page, then navigate to Storage Spaces using the option at the bottom of the box and click on 'Add a new Storage Space' option. Choose a unique name for your new storage space, instert its temperature and press 'Confirm' | Just created new Storage Space appears on the storage spaces list  | Works as expected |

![Manual Testing](docs/testing/manual/4-a.png)
![Manual Testing](docs/testing/manual/4-b.png)

5. As a User I want to add a new stock item.

| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| Storagespace Details & Items Table | From Storagespace Details & Items Table click on 'Add a new item' complete the form and click 'Confirm' | Creates a new item with the inserted details | Works as expected |

![Manual Testing](docs/testing/manual/5-a.png)
![Manual Testing](docs/testing/manual/5-b.png)

6. As a User I want to update a stock item.


| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| Storagespace Details & Items Table | From Storagespace Details & Items Table click on the pen to square icon in the row corresponding to item to be updated, edit detail on the form as required & click on 'Confirm & Return to Storagespaces List' then navigate back to the storagespace details of the storagespace relevant to the item as updated | Item's details are updated and is moved to a different storagespace if applicable | Works as expected  |

![Manual Testing](docs/testing/manual/6-a.png)
![Manual Testing](docs/testing/manual/6-b.png)
![Manual Testing](docs/testing/manual/6-c.png)

7. As a User I want to remove an item from the stock list.

| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| Storagespace Details & Items Table | From Storagespace Details & Items Table click on the trash can icon in the row for the item to be deleted then choose 'Confirm & Return to Storagespaces List'| Item removed from the storagespace | Works as expected |

![Manual Testing](docs/testing/manual/7-a.png)
![Manual Testing](docs/testing/manual/7-b.png)
![Manual Testing](docs/testing/manual/7-c.png)

8. As a User I want to contact Site's Admin.

| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| Contact | Go to the contact page by clicking on the envelope icon in the footer, complete the contact form and click on 'Submit your message' | User is informed that the message has been sent & the received message information is displayed | Works as expected |

![Manual Testing](docs/testing/manual/8-a.png)
![Manual Testing](docs/testing/manual/8-b.png)

9. As a User I want to see items are expired.

| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| Storagespace Details & Items Table | On the Items Table see items' expiry dates | expiry dates of expired items are highlited in orange | Works as expected |

![Manual Testing](docs/testing/manual/9.png)

10. As a User I want to see items that have different temperature range than in the storage.

| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| Storagespace Details & Items Table | On the Items Table see items' temp ranges | temp ranges of items that should be in a colder environment are highlited in red & items that can be stored in a warmer place in blue | Works as expected |

![Manual Testing](docs/testing/manual/10.png)

11. As a User I want to easily navigate on the website.

| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| Logo and Website Name | Click on the logo or website name | Home page is loaded | Works as expected  |
| Navigation Bar | Click on options: Home/Register/Login/ Change Password | Relevant pages open | Works as expected |
| Footer | Click on Facebook/ Pinterest/ YT/ envelope icons | Facebook/ Pinterest/ YT/ open in separate tabs. For envelope the contact page is open | Works as expected |
| Register | Click on Register in the navbar / Our Mission Box | Register page with the form opens | Works as expected |
| Login | Click on Login in the navbar / Our Mission Box | Login page with the form opens | Works as expected |
| Password Reset | Click on 'Forgot Password?' link on Login or Password Change pages | Password Reset page opens | Works as expected |
| Password Change | Click on the gear icon in the nav-bar, complete the form and click 'Change Password'| User can login using the update password | Works as expected |
| Our Mission Box | Open Home page | Links to Login/Reset/Stocklist open | Works as expected |
| Main Stocklist Page | Click on User: Name or access it via Our Mission Box, click on options(Create your stocklist now/edit stocklist/delete stocklist/ Storage Spaces) | Relevant pages open | Works as expected |
| Storage Spaces List | Access Storage Spaces List from Main Stocklist Page, click on 'Add a new Storage Space' or 'Return' | Relevant options open | Works as expected |
| Storagespace Details & Items Table | Access Storagespace Details & Items Table Storage Spaces List then click on options(edit storagespace/delete storagespace/ add a new item/ edit item/ delete item/return) | Relevant options open | Works as expected |
| Contact | Access Contact by clicking the envelope icon in the footer | Contact page opens with the form, username & email are filled-up automatically if user is logged-in and entered e-mail address during the registration | Works as expected |
| Logout | Click on Logout in the nav-bar and confirm by clicking Logout button | User is logged-out | Works as expected |
| Admin | Go to https://mypantrynote.herokuapp.com/admin & login using superuser's credentials | Admin panel opens | Works as expected |

12. As an Admin I want to access admin panel.

| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| Admin | Go to https://mypantrynote.herokuapp.com/admin & login using superuser's credentials | Admin panel opens | Works as expected |

13. As an Admin I want to review messages sent by users.

| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| Admin | Go to https://mypantrynote.herokuapp.com/admin & login using superuser's credentials, click on Contacts and on MESSAGE ID to view details | Message opens displaying received details | Works as expected |

![Manual Testing](docs/testing/manual/13.png)
![Manual Testing](docs/testing/manual/13-a.png)

14. As an Admin I want to manage messages sent by users.

| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| Admin | Go to https://mypantrynote.herokuapp.com/admin & login using superuser's credentials, click on Contacts | Delete read messages | Works as expected |

![Manual Testing](docs/testing/manual/14-a.png)
![Manual Testing](docs/testing/manual/14-b.png)

15. As an Admin I want to deliver an intuitive website for the users.

| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| Logo and Website Name | Click on the logo or website name | Home page is loaded | Works as expected  |
| Navigation Bar | Click on options: Home/Register/Login/ Change Password | Relevant pages open | Works as expected |
| Footer | Click on Facebook/ Pinterest/ YT/ envelope icons | Facebook/ Pinterest/ YT/ open in separate tabs. For envelope the contact page is open | Works as expected |
| Register | Click on Register in the navbar / Our Mission Box | Register page with the form opens | Works as expected |
| Login | Click on Login in the navbar / Our Mission Box | Login page with the form opens | Works as expected |
| Password Reset | Click on 'Forgot Password?' link on Login or Password Change pages | Password Reset page opens | Works as expected |
| Password Change | Click on the gear icon in the nav-bar, complete the form and click 'Change Password'| User can login using the update password | Works as expected |
| Our Mission Box | Open Home page | Links to Login/Reset/Stocklist open | Works as expected |
| Main Stocklist Page | Click on User: Name or access it via Our Mission Box, click on options(Create your stocklist now/edit stocklist/delete stocklist/ Storage Spaces) | Relevant pages open | Works as expected |
| Storage Spaces List | Access Storage Spaces List from Main Stocklist Page, click on 'Add a new Storage Space' or 'Return' | Relevant options open | Works as expected |
| Storagespace Details & Items Table | Access Storagespace Details & Items Table Storage Spaces List then click on options(edit storagespace/delete storagespace/ add a new item/ edit item/ delete item/return) | Relevant options open | Works as expected |
| Contact | Access Contact by clicking the envelope icon in the footer | Contact page opens with the form, username & email are filled-up automatically if user is logged-in and entered e-mail address during the registration | Works as expected |
| Logout | Click on Logout in the nav-bar and confirm by clicking Logout button | User is logged-out | Works as expected |
| Admin | Go to https://mypantrynote.herokuapp.com/admin & login using superuser's credentials | Admin panel opens | Works as expected |

</details>

[Back to Table Of Contents](#table-of-contents)

## Bugs

| Bug  | Fix  |
| ------- | ------- |
| Heroku error during the early deployment: "Failed building wheel for backports.zoneinfo" | Edit requirements.txt file* |
| Continuation line under-indented for visual indent (E128) | Check best practice on Flake8 Rules |
| Accessibility error: Empty table header | Add aria-label "Settings column" to th element |

* update backports from backports.zoneinfo==0.2.1 to backports zoneinfo==0.2.1;python_version<"3.9"

[Back to Table Of Contents](#table-of-contents)

## Deployment

- This site was deployed using Heroku in following steps: 

Before deployment remember to set DEBUG = False & ensure requirements.txt is updated using terminal command: pip3 freeze --local requirements.txt

1. Log in to Heroku or create an account
2. On the main page click the button labelled New in the top right corner and from the drop-down menu select Create new app
3. You must enter a unique app name
4. Next select your region
5. Click on the Create App button
6. Click Reveal Config Vars and add a new record with the SECRET_KEY
7. Add another record to Config Vars with the CLOUDINARY_URL
8. Add another record to Config Vars with the DATABASE_URL
9. Add another record to Config Vars with DISABLE_COLLECTSTATIC = 1
10. Add another record to Config Vars with PORT = 8000
11. Below Config Vars in Buildpacks select heroku/python
12. Go to the Deploy Tab
13. Choose Deployment method GitHub and click Save Changes
14. Confirm you want to connect to GitHub
15. Search for the repository name and click the connect button
16. Scroll to the bottom of the deploy page and select the preferred deployment type ( Automatic deploys or Manual deploy)
17. Choose a branch to deploy: main
18. Click on Deploy Branch button
19. For Automatic deploys click on Enable Automatic Deploys button

[Back to Table Of Contents](#table-of-contents)

## Credits 

- Information regarding food waste found on <a href="https://www.epa.ie/our-services/monitoring--assessment/waste/national-waste-statistics/food/">the Environmental Protection Agency (EPA) website</a>.

- Website's background based on <a href="https://css-tricks.com/snippets/css/transparent-background-images">CSS Tricks</a>.

- Some of the styles inspired by the knowledge from my Project Portfolio 2:<a href="https://github.com/WojtekKamilowski/CI_PP2_WOTM">what'sOnTheMenu</a>.

- Placeholder color from <a href="https://www.w3schools.com/howto/howto_css_placeholder.asp">W3Schools</a> 

- Some of code based on <a href="https://github.com/Code-Institute-Solutions/Django3blog">Code Institue's "I Think Therefore I Blog" Walkthrough project</a>

- Some of code based on <a href="https://github.com/Code-Institute-Solutions/HelloDjango">Code Institue's "HelloDjango" Walkthrough project</a>

- get_queryset(self) function in PantryStocklist class view based on <a href="https://github.com/4n4ru/CI-PP4-Meal-Planner">CI-PP4-Meal-Planner</a>

- add_stocklist(request) and other view functions inspired by <a href="https://github.com/ArronBeale/CI_PP4_the_diplomat">CI_PP4_the_diplomat</a>

- JavaScript code for close messages after 3 seconds from <a href="https://github.com/ArronBeale/CI_PP4_the_diplomat">CI_PP4_the_diplomat</a>

- Contact app with some adjustments from <a href="https://github.com/ArronBeale/CI_PP4_the_diplomat/tree/main/contact">CI_PP4_the_diplomat</a>

- Unique slug fields found on: <a href="https://stackoverflow.com/questions/3816307/how-to-create-a-unique-slug-in-django">Stackoverflow</a>

- Unique together found on: <a href="https://stackoverflow.com/questions/66142733/how-do-i-go-about-making-a-django-model-field-unique-but-only-for-individual-use">Stackoverflow</a>

- Capitalize field on form found on: <a href="https://stackoverflow.com/questions/11996963/how-to-automatically-capitalize-field-on-form-submission-in-django">Stackoverflow</a>

- Storage spaces selection for 'Add a new item' associated with user found on: <a href="https://stackoverflow.com/questions/53478438/django-forms-how-to-show-only-objects-associated-with-user-in-dropdown">Stackoverflow</a>

- Datepicker for Expiry Date in ItemForm found on <a href="https://stackoverflow.com/questions/3367091/whats-the-cleanest-simplest-to-get-running-datepicker-in-django">Stackoverflow</a>

- Delete from <a href="https://stackoverflow.com/questions/19754103/django-how-to-delete-an-object-using-a-view">Stackoverflow</a>

- Delete confirmation inspired by <a href="https://stackoverflow.com/questions/31843145/deleteview-with-confirmation-template-and-post-method">Stackoverflow</a>

- Fix deployment issue from <a href="https://stackoverflow.com/questions/71712258/error-could-not-build-wheels-for-backports-zoneinfo-which-is-required-to-insta">Stackoverflow</a>

- Fix Django allauth OSError: [Errno 99] Address not available error <a href="https://stackoverflow.com/questions/69544594/django-allauth-oserror-errno-99-address-not-available">Stackoverflow</a>

- Code inserted at the beginning of the testcase in test_models.py creates a user, logs them in, and allows the rest of the test to contiue from: <a href="https://stackoverflow.com/questions/36940384/how-do-i-setup-a-unit-test-user-for-django-app-the-unit-test-cant-login">Stackoverflow</a>

- Django's built-in MinValueValidator & MaxValueValidator validators from <a href="https://stackoverflow.com/questions/849142/how-to-limit-the-maximum-value-of-a-numeric-field-in-a-django-model">Stackoverflow</a>

- Validation of min. & max. temp. for ItemForm from <a href="https://stackoverflow.com/questions/58068844/django-how-to-validate-validator-a-greater-then-between-two-formfields">Stackoverflow</a>

- Continuation line under-indented for visual indent (E128) PEP8 validation errors fix from <a href="https://www.flake8rules.com/rules/E128.html">Flake8 Rules</a>

### Media

- All icons found on <a href="https://fontawesome.com/">Fontawesome</a>.

- Font Fira Sans found on <a href="https://fonts.google.com/specimen/Fira+Sans?fbclid=IwAR0M5mybiiO6URy8GMzAKIYHRdX_lQHlJhwcmI6h-bNFuL90-osnCNZaC8Q">Google Fonts</a>.

- Font PT Serif found on <a href="https://fonts.google.com/specimen/PT+Serif?fbclid=IwAR0M5mybiiO6URy8GMzAKIYHRdX_lQHlJhwcmI6h-bNFuL90-osnCNZaC8Q&query=PT+Serif">Google Fonts</a>.

- Colors from <a href="https://coolors.co/">Coolors</a>.

- Background image from <a href="https://www.freepik.com/free-vector/flat-design-pantry_10892283.htm#query=food%20shelf&position=37&from_view=search&track=ais">Freepik</a>.

- Image replacing default Cloudinary placeholder for list_image from <a href="https://pixabay.com/photos/zero-waste-plastic-free-3749854/">Pixabay</a>.

- Image replacing default Cloudinary placeholder for create stocklist image from <a href="https://console.cloudinary.com/console/c-7d0dc1f07855d3688919c6f201a8dd/media_library/search/asset/4f3bf051866c4e34e1f31c72fe08ade6/manage?q=&context=manage">Freepik</a>.
  
- Image of a broken jar with pasta for error messages from <a href="https://pixabay.com/photos/jar-broken-pasta-pasta-scattered-4258747/">Pixabay</a>.

[Back to Table Of Contents](#table-of-contents)

## Further Development

1. Add extra functionality to the storagespace form to prevent Error 500 appearing when user attempts to add a storagespace with an existing name.

![Further Development](docs/storage-development.png)
![Further Development](docs/storage-development-error.png)

2. Automatic Password Reset funtionality.

[Back to Table Of Contents](#table-of-contents)

## Acknowledgements
I would like to thank those who were a great support and inspiration during writing this project:
- My wife, who supported me during the process of creating this project.
- My mentor Mo Shami.
- Code Institute for preparing the materials and providing a wide range of available means of learning for the students.
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
  - [Creating the app using Django](#creating-the-app-using-django)
  - [Bugs](#bugs)
  - [Deployment](#deployment)
  - [Credits](#credits)
    - [Media](#media)
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

### User Requirements and Expectations
- Accessible and responsive website.
- Intuitive website with a layout allowing to easily navigate through it.
- Easy access to Create, Read, Update & Delete information.
- Links and features that function in accordance with their intended purpose.
- Connection with the community on the social media platforms.
- A contact form to contact the website owner.

### User Stories

#### Users

As a User I want to:
- Register an account.
- Login.
- View the food stock list 
- Add a new storage space
- Add a new stock item.
- Update a stock item.
- Remove an item from the stock list.
- Contact Site's Admin
- See items are expired
- See items that have different temperature range than in the storage

#### Site Owner

As an Admin I want to:
- Access admin panel.
- Review messages sent by users .

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
![HTML Validation](docs/validation/html/html-items.png)
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

</details>

[Back to Table Of Contents](#table-of-contents)

## Performance

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

<details><summary>Click to see user stories testing</summary>

---------------------------------------------------------------

| Feature | Action  | Expected Result | Actual Result |
| ------- | ------- | --------------- | ------------- |
| | |  |  |

</details>


[Back to Table Of Contents](#table-of-contents)


## Creating the app using Django

## Bugs

| Bug  | Fix  |
| ------- | ------- |
| Heroku error during the early deployment: "Failed building wheel for backports.zoneinfo" |  Edit requirements.txt file. update backports from backports.zoneinfo==0.2.1 to
backports.zoneinfo==0.2.1;python_version<"3.9" |
| Continuation line under-indented for visual indent (E128) | Check best practice on Flake8 Rules |

[Back to Table Of Contents](#table-of-contents)

## Deployment


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

- based on <a href=""></a>

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

## Acknowledgements
I would like to thank those who were a great support and inspiration during writing this project:
- My wife, who supported me during the process of creating this project.
- My mentor Mo Shami.
- Code Institute for preparing the materials and providing a wide range of available means of learning for the students.
![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# The Otter Mill


## Project Purpose
'The Otter Mill' is a full-stack web application for a hypothetical restaurant built with the Django framework. The application includes a comprehensive booking system allowing prospective guests to create, view, update and delete multiple bookings, and specify key details such as the intended reservation date and time. Account authentication is used to facilitate the booking process and ensure security of users' details. 

The application provides a clean, appropriately styled interface where users can learn about the restaurant and see an image of the restaurant on the homepage, as well as being able to view the restaurant's current menu on a separate page.

## Link to application
The application can be accessed directly at this dedicated link: https://the-otter-mill-8571f3abe621.herokuapp.com/

## GitHub Repository
The GitHub repository for the project can be accssed at: https://github.com/DTT2411/the-otter-mill

## Project Methodology
An AGILE methodology was used to develop the project and was strictly adhered to at all stages of development. A GitHub project was utilised to track progress made on User Stories. 

User Stories were categorised into "must-have", "should-have", and "could-have" status, depending on the importance of the described features for establishing a minimum viable product. During development, the stories were separated into "To-Do", "In Progress", and "Done" streams to track development progress for each story.

Each user story was subdivided into individual acceptance criteria - stories were only moved into the "Done" stream once all criteria had been met.


## User Stories

### Implemented User Stories

#### Must Have
As a guest, I can...
- ...create a booking online so that I can have dinner at the restaurant.
- ...view my existing booking(s) so that I can remind myself of the details I submitted.
- ...update my booking so that I can make changes in case we are running late, or want to add another guest.
- ...delete my booking so that I can cancel at any time.
- ...view information about the restaurant so that I can learn about its history, cuisine, location and opening hours.
- ...register and log into a site account so that I can make a booking.

#### Should Have
As a guest, I can...
- ...view information about the restaurant’s menu so that I can decide if the restaurant would be suitable for my party.
- ...make multiple bookings so that I can schedule several upcoming dinners I want to have with friends.
- ...automatically be assigned a table when booking so that my dinner party is given the best sized available table.

As a restaurant manager, I can...
- ...create, read, update and delete menu items from the current menu so that we can accommodate for seasonal changes to the menu.
- ...make users login in order to make a booking so that the appropriate details for the user can be stored.

#### Could Have
As a guest I can...
- ...see a table listing existing bookings with columns for date, time and number of guests so that I can quickly review and understand my bookings at a glance.

### User Stories for future implementation
As a restaurant manager, I can...
- ...create, view and update content from the About Us section so that I can update this as and when needed.
- ...see an admin-only page listing all bookings in a sensible format so that I can get an overview of existing bookings and apply changes as required.
- ...have bookings which are in the past automatically deleted from the booking system so that only a list of valid upcoming bookings is retained.


## Design

### Design Methodology
A mobile-first design methodology was employed to ensure a responsive and organised appearance on all website pages. A combination of Bootstrap classes and custom CSS media queries was utilised to ensure elements and text appear at an appropriate size on all screen sizes. 

### Wireframes
Balsamiq wireframes were developed at the outset of the project as a visual guide to the structure and key features of the website.

### Colour Scheme
Coolors was used to identify suitably contrasting primary, secondary and tertiary colours for use across the site. A contrast checker was also utilised to ensure sufficient contrast between the primary colour and secondary & tertiary colours.
- **Primary colour - #30011E, Dark Purple**: Used as the main background colour for large html elements. Also used for fonts on some elements with inverse colouring.
- **Secondary colour - #D7FCD4, Tea Green**: Used as the main colour for text across the site. Also used as background colour on some elements with inverse colouring.
- **Tertiary colour - #B6CCA1, Celadon**: Intentionally low-contrast colour relative to secondary colour, primarily used to make navigation links and buttons with the secondary colour on top of a primary colour backgroun reactive on mouse hover.

![Coolors color scheme](readme_assets/img/colour-scheme.jpg) 

### Fonts
Google Fonts was used to identify suitable primary and secondary fonts for use throughout the site.

**Headings font - Eagle Lake**: "Fancy", attractive cursive font which looks good for large heading elements.<br>
![Headings font](readme_assets/img/heading-font-example.jpg) 

**Main font - Gudea**: Highly readable, clear and functional typeface for main/body text.<br>
![Main font](readme_assets/img/main-font-example.jpg) 


## Features

The main features of the application include:
1. Navigation Bar
2. Sign-in status notification
3. System Messages
4. Hero Image
5. Footer
6. Homepage
7. Reservation form
8. My Bookings page
9. Menu page
10. Registration page
11. Login page
12. Logout page

### 1. Navigation Bar
A simple Bootstrap navigation bar was used for site navigation, including the restaurant name, links to the "Home", "Menu" and "My Bookings" pages as well as authentication pages depending on the user's sign-in status. The navigation bar also contains the "Book Now" call to action (CTA) button.

Signed in users have access to the reservation form via the CTA button as well as the "My Bookings" page, and can opt to logout.

Signed out users have access to registration and login pages and are redirected to login when they click the CTA button.

The navigation bar is present on all pages of the site as it forms part of the base.html template which every other page/template extends. This ensures that users can enjoy a consistent look and level of navigation across the site.

On smaller screens, the navigation bar is collapsed into a buger icon, which expands into a vertical list in order to better utilise space. 

**Navigation bar when signed in** <br>
![Navbar signed in](readme_assets/img/navbar-signed-in.jpg) 

**Navigation bar when signed out** <br>
![Navbar signed out](readme_assets/img/navbar-signed-out.jpg) 

**Collapsed navigation bar with "burger" icon for smaller screens** <br>
![Navbar collapsed](readme_assets/img/navbar-collapsed.jpg) 

### 2. Sign-in status notification
All pages of the site contain a signin status notification for the user nested in the top right corner of the screen below the navigation bar. The notification advises whether the user is logged in or logged out and updates dynamically depending on sign-in status. 

**Status notification when signed in** <br>
![Status notification signed in](readme_assets/img/signed-in-status-notification.jpg) 

**Status notification when signed out** <br>
![Status notification signed out](readme_assets/img/signed-out-status-notification.jpg) 

### 3. System Messages
Django's messaging system was utilised to provide updates to the user when their sign-in status changes (i.e. if they sign in or out) and when they create, delete or edit a reservation. The messages appear in an alert bar below the navbar, above other page elements, in a green or red theme (depending on success vs error/failure) on the next page after a relevant event occurs.

**Example success message** - sign in <br>
![System succcess message](readme_assets/img/success-message.jpg) 

**Example error message** - invalid booking <br>
![System error message](readme_assets/img/error-message.jpg) 

### 4. Hero Image
A high-resolution, royalty-free hero image relevant to the restaurant theme was sourced from Pixabay. Using custom styling and application of `{% block main_class %}` on templates, this image serves as the background for all pages.

**Full hero image**<br>
![Hero Image](readme_assets/img/hero-image.jpg) 

### 5. Footer
The footer contains key information about the restaurant including address, contact number, email address, opening times, and social media links. Fontawesome Icons are used in this section for visual guidance and intuitive identification of contact details. 

Similar to the navigation bar, the footer is a component of the base.html template and is applied consistently across all pages on the website.

The footer is responsive, dividing into two rows on larger screens and collapsing & centering on smaller screens. <br>

**Footer - large screen**<br>
![Footer large](readme_assets/img/footer-large.jpg) 

**Footer - small screen**<br>
![Footer small](readme_assets/img/footer-small.jpg) 

### 6. Homepage
The default homepage for the website contains a short description of the restaurant's history and location, and the type of cuisine served. 

**Homepage**<br>
![Homepage](readme_assets/img/homepage.jpg) 

### 7. Reservation form
Users can access the reservation form by being logged in and clicking the "Book Now" CTA button from any page on the site. A simple booking form was developed to apprehend key details for the reservation including the number of guests, date & time of booking, and expected duration. An optional "Special Requirements" field also allows prospective guests to inform the restaurant about any allergies, conditions, etc. prior for anyone in their party.

The same form is used when a user edits an existing booking via the My Bookings page. In this case, after clicking the "Edit" button, a form prepopulated with the user's existing details will be displayed. Please see the "My Bookings page" subsection for further context.

**Reservation Form**<br>
![Reservation form](readme_assets/img/reservation-form.jpg) 

#### **Form Fields**
- **Number of guests**: Simple positive integer field with accepted minimum of 1 and maximum of 6 (largest table size at thos restaurant).
- **Date**: Datepicker field which opens into a calendar view when the calendar icon is clicked. Only accepts dates from today onwards. <br>
![Datepicker](readme_assets/img/reservation-form-date.jpg) 
- **Time**: Timepicker field which opens into a scrollable time selector when the clock icon is clicked. Only accepts times within the restaurant's opening hours (12:00 to 22:00).<br>
![Timepicker](readme_assets/img/reservation-form-time.jpg) 
- **Duration**: Simple positive integer field requesting user to define expected length of stay in hours, with accepted minimum of 1 and maximum of 3. Tracking reservation durations is important for the table allocation functionality, as the system needs to know which tables are booked and for how long.
- **Special Requirements**: Simple text area field for users to advise of any allergies, conditions or other requirements. Limited to 300 characters.

### 8. My Bookings list
The "My Bookings" page is accessible to all logged in users. If the user has any existing bookings, they will be displayed in a simple table with columns for key booking details. Additionally, users can manage (edit or delete) their booking via the respective buttons on the right side of the table in the Manage column.

If the user does not have any existing bookings, a simple alert message is displayed instead of the table.

**My Bookings - large screen**<br>
![My Bookings Large](readme_assets/img/my-bookings-large.jpg) 

**My Bookings - small screen**<br>
![My Bookings Small](readme_assets/img/my-bookings-small.jpg) 

**My Bookings - Manage buttons**<br>
The "Edit" and "Delete" buttons become appropriately coloured upon mouse hover or focus for visual guidance.<br>
![My Bookings Manage Buttons](readme_assets/img/my-bookings-manage-buttons.jpg) 

**My Bookings - no bookings**<br>
![No Bookings](readme_assets/img/no-bookings.jpg) 

### 9. Menu page
The "Menu" page is accessible to all users regardless of sign-in status. The page displays tabulated lists of menu items separated depending on course/type, e.g. Starters, Mains. Key information including the dish name and price are included on the menu sections.

The page is responsive, collapsing the size of the divisions for each course at smaller screen sizes.

Element padding and row dividers are used to ensure the tables of dishes are clean, well deliniated and readable.

**Menu - large screen**<br>
![Menu Large](readme_assets/img/menu-large.jpg) 

**Menu - small screen**<br>
![Menu Small](readme_assets/img/menu-small.jpg) 

### 10. Registration page
The default All Auth registration page has been custom styled for thematic consistency, but otherwise the content of this page is identical to the default. This page is accessible for users who are not already logged in, and allows them to register a guest account on the website. They are encouraged to specify a username and password (with confirmation), an email (optional), and upon valid form submission they will be signed in and redirected to the homepage with an alert to confirm they have successfully signed in. The page also has a link `sign in` which redirects the user to the login page if they already have an account.<br>

![Registration Page](readme_assets/img/registration-page.jpg) 

### 11. Login page
Similar to the registration page, the login page is similar to the All Auth default with the exception of custom styling for consistent appearance. This page is accessible for users who are not already logged in, and allows them to enter their username and password in order to access the site's booking functionality. The page also has a link `sign up` which redirects the user to the registration page if they do not already have an account.<br>

![Login Page](readme_assets/img/login-page.jpg) 

### 12. Logout page
Similar to the registration page, the logout page is similar to the All Auth default with the exception of custom styling for consistent appearance. This page is accessible for users who are logged in, and requests their confirmation in order to sign out from their site account.<br>
![Logout Page](readme_assets/img/logout-page.jpg) 


## Models
Dbdiagram was used at the outset of the project to sketch out the models and relationships which would be required for the database used to hold data for reservations, tables, and the menu. This tool allows the development of linked Entity-Relationship Diagrams to help enivision the structure and interactions between the required models.<br>

**Database Structure**<br>
![Dbdiagram ERDs](readme_assets/img/dbdiagram-ERDs.jpg) 


## Features for future development
The following features for future implementation are inspired by the "could have" user stories which are yet to be accomplished by the current version of the application. I have focussed on the following 3 improvements as I believe these would be the most immediately impactful for the functionality and user experience.

### Automatic removal of reservations after date has passed
The current booking system and user experience would be significantly improved if past bookings were automatically removed from the database after the specified date has passed. Currently, past reservations are retained on the system and therefore stay present on the "My Bookings" page. 

### Additional front-end admin functionality
The current site permits guests to create and manage bookings, however it would also be helpful to restuarant managers and administrators to have additional administrative features. Logged in administrators/superusers could have an admin-only page where they can view, organise (filter, sort, search) and manage all existing bookings from the front end, rather than having to use the default Django administration panel.

### Develop model for restaurant information
A new model could be created for `RestaurantInformation` and used to feed details such as opening times, contact info, etc. into templates with DTL where they are currently held as static text. Additionally, this could be fed into the bboking views and forms, where the restaurant opening times could be read as the limits for booking time inputs, rather than being static values added to widget attributes as they are currently.


## Testing

### Manual Testing
All manual testing detailed here was conducted both on a local server, as well as the main deployed version after development.

#### **Booking System**
Exhaustive testing was conducted on all aspects of the booking system, including the reservation form and "My Bookings" page. 
- **Reservation form**: All fields in the booking form (both for create and edit views) were manually tested to ensure an invalid booking could not be submitted. Testing was conducted in a structured approach using normal, extreme, and invalid data (e.g. time added as 19:00, 22:00, and 04:00; number of guests added as 3, 6, and 30). Values were entered both manually via text entry as well as using the date and time widgets to select from calendar/time scroller.
- **My Bookings page**: Testing was conducted to ensure that the page was responsive and produced the correct data for the logged-in user. Tested with users with no associated bookings, as well as users with a large number of existing bookings to ensure integrity of the table. The "Edit" and "Delete" buttons were also tested to ensure that each provided the expected behaviour when updating or deleting a booking, and that the page correctly refreshed and updated the list of bookings. The deletion confirmation check modal was also tested to ensure it correctly pops up whenever a user requests deletion.
- **Testing during development of create & edit reservation views**: During development, due to the complexity of the Python code required in the views for creating and editing reservations - in particular, the logic for table assignment - it was necessary to conduct manual testing using print statements in the terminal to track the status of booking variables. 

#### **Admin panel**
Admin panel functionality was tested for all models used within the application. Ensured that full expected CRUD functionality was available to logged in superusers for Users, Reservations, Tables and MenuItems, and that inputting normal, extreme, and invalid data in various fields resulted in the expected outcome when attempting to create or update model instances.

#### **Styling**
Manual testing was used to tidy up styling applied by Bootstrap classes on html elements and custom style rules in the stylesheet. The application was run on a local server while making amends, allowing live identification of redundancies and opportunities for refactoring. 

#### **Responsiveness**
The responsiveness of all pages on the site was tested by accessing the deployed version of the website via smartphone, as well as using Chome Developer Tools to limit screen size according to industry-standard breakpoints for phones, tablets, laptops and above. 

#### **Fixes & Improvements from manual testing**
- Noticed that all icons in the footer were being targeted with a 200% size rule which had only been intended for the social media icons. Resolved by adding more specificity to the existing rule.
- Identified a missing minimum value on the "number of guests" widget on the booking form, resolved by setting `'min': '1'` in the widget's attributes in `booking/forms.py`.
- Identified a missing minimum value validation on the "duration" field of the Reservation model, resolved by adding `validators=[MinValueValidator(1)]` to the duration field and migrating the changes.
- Multiple instances of redundancy within style rules e.g. applying color/background style to elements which have already inherited this from a lower specificity rule; applying styles already managed by Bootstrap class.
- Resolved an issue causing the table assignment functionality to break using manual testing with terminal print statements added to the `create_reservation` view. 


### Automated Testing

#### **Mock data testing**
Django's built-in testing functionality was used for testing key components of the booking system, including tests for the reservation form and functional views related to bookings.

The tests in `booking/test_forms` provides test cases for the functionality of the booking form, ensuring form validity and testing the constraints for each field.

The tests in `booking/test_views` verifies the functionality of the `create_reservation`, `edit_reservation` and `delete_reservation` views.

#### **Lighthouse testing**
The Lighthouse testing functionality within Google Chrome Developer Tools was used to assess the performace and accessibility of each site page on the deployed version of the application. The results for each page are summarised below:<br>
![Lighthouse testing](readme_assets/img/lighthouse-testing.jpg)<br>
The main deficit in Performance rating, relative to the other metrics, was the use of a high resolution hero image for the background on all pages of the site. Initially, an even higher resolution image was being used and resulted in significantly lower Performance scores (mid 60s for most pages). Lower resolution images were tested until sufficient compromise between image quality and page load was found.

#### **HTML Validation**
W3C HTML Validation Service was used to validate all templates used throughout the site, including:
- base.html
- homepage.html
- reservation_form.html
- reservation_list.html
- menu_list.html

All major issues and errors reported by W3C were due to the use of Django Templating Language (DTL) within the html documents (e.g. `{% for message in messages %}`, `{% message %}`) and could safely be ignored. 

**Examples of errors thrown due to W3C not recognising DTL**<br>
![DTL error examples 1](readme_assets/img/DTL-error-examples1.jpg)<br>
![DTL error examples 2](readme_assets/img/DTL-error-examples2.jpg) 

One minor issue was detected on login.html, logout.html and signup.html authentication pages where a trailing slash had been left on an input element, which was resolved immediately.<br>

**Trailing slash issue**<br>
![Trailing Slash Fix](readme_assets/img/trailing-slash-fix.jpg) 

#### **CSS Validation**
W3C CSS Validation Service was used to validate the static stylesheet after tidy up had been conducted. No errors were found.<br>
![CSS Validation](readme_assets/img/CSS-validation.jpg) 

#### **JS Validation**
The online JSHint validation tool was used to check the static javascript file. No errors were found.<br>
![JS Validation](readme_assets/img/JS-validation.jpg) 

#### **Python Validation**
Utilised [Code Institute's Python Linter](https://pep8ci.herokuapp.com/) for PEP8 adherence & validation. A python linter (Flake8) was also used within the IDE during development meaning that the majority of issues were fixed during development. 

I was unable to resolve one type of linter error reported on my `booking/views.py` file. Due to the level of indentation and length of variable names requried for the booking system logic, and the lack of a suitable place in these lines to add a linebreak, several lines in this file are longer than the 79 character limit. 

**Linter errors on booking/views.py**<br>
![Linter Errors](readme_assets/img/linter-errors.jpg) 

**Example of "line too long" error**<br>
![Line too long error](readme_assets/img/line-too-long-error.jpg) 

## Key packages
- **Django==4.2.23**: The framework used to build the application.
- **django-allauth==0.57.2**: Django application with pre-built templates for user registration and account management, including password protection.
- **django-crispy-forms==2.4**: Django application used for conveniently styling and structuring the reservation form.
- **django-summernote**: Django application for improving admin panel functionality for specific models and rich text editing.
- **gunicorn==20.1.0**: Python WSGI server for running the application.
- **psycopg2==2.9.10**: PostgreSQL database adaptor for python.
- **whitenoise==5.3.0**: Used to conveniently serve static files prior to deployment with `collectstatic` command.

## Django imports utilised
- **django.contrib**: messages
- **django.shortcuts**: render, redirect, get_object_or_404
- **django.test**: TestCase
- **django.urls**: path, reverse
- **django.utils**: timezone
- **django.views**: generic
- **django.contrib.auth.decorators**: login_required
- **django.contrib.auth.models**: User
- **django.core.validators**: MaxValueValidator, MinValueValidator

## Deployment

### Pre-deployment Requirements
- Ensure you have a GitHub repository set up for the project.
- Set `debug` to `False` in `settings.py`
- Ensure that `.herokuapp.com` is appended to the list of `ALLOWED_HOSTS` in `settings.py`
- Ensure `whitenoise` is correctly installed use `python manage.py collectstatic` to update any changes to static files, then commit and push these files to the project repository before deployment.
- Ensure `SECRET_KEY` is correctly set up as an environment variable and has been added as a config var to the Heroku app via Settings tab.
- Create a "Procfile" with `web: gunicorn the_otter_mill.wsgi` to link the WSGI server for running the application.
- Push any updated requirements to `requirements.txt`.

### Steps to deploy (via Heroku)
Please note that these steps assume you have a verified Heroku account and an eco dynos subscription.
- Log into Heroku dashboard.
- Create a new app with a unique name for the project.
- On the "Deploy" tab, enable GitHub integration by clicking "Connect to GitHub".
- Type in the name of your project repository you want the app to link to.
- On the "Resources" tab, select the "Eco Dyno" container to run the project.
- At the bottom of the deployment page, select the `main` branch and manually deploy.
- Open the deployed application.


## Credits

### Concept
Project Example Idea 1 recommended within Code Institute's Portfolio Project 4 Assessment Guide was the main inspiration for this project.

### AGILE Project Management
Github project dashboard and issues were used for AGILE development, including: development of User Story templates; labels for prioritisation (must-have, should-have, could-have); and a dashboard for tracking User Story progress (to-do, in progress, done).

### Code
- **Stack Overflow** was used extensively for general troubleshooting, and for specific fix with enforcing a positive number on Django model via `minValuValidator`: https://stackoverflow.com/questions/54858123/how-do-i-enforce-a-positive-number-on-my-python-django-model-field
- **Bootstrap Documentation** for general troubleshooting on styling and classes, and a specific fix for right-aligning table items with the `flowreverse` class: https://getbootstrap.com/docs/4.0/utilities/flex/
- **Django documentation** for general guidance on built-in Django functions and imports used extensively throughout the project: https://docs.djangoproject.com/en/5.2/.
- Reutilisation of navbar and footer elements from previous Ski Trossachs project (my CI Portfolio Project 1): https://github.com/DTT2411/CI-Portfolio-Project-1.


### Deployment
- **Heroku** - Cloud application platform used to host the project. Link to Heroku: https://www.heroku.com/.

### Data Modelling
- **Dbdiagram** (https://dbdiagram.io/) was used to help plan and visualise the models required for the booking and menu apps within the project. 

### Content
- **Bootstrap** classes were used extensively throughout the templates to improve responsiveness of html elements and reduce the need for additional custom CSS styling. https://getbootstrap.com/docs/5.3/getting-started/introduction/.
- **Google Fonts** for custom fonts used throughout site. Link to embed code used: https://fonts.googleapis.com/css2?family=Eagle+Lake&family=Gudea:ital,wght@0,400;0,700;1,400&display=swap.
- **Coolors** (https://coolors.co/) was used to identify a suitable colour scheme for the site.
- **Pixabay** was used to identify a suitable hero-image for use as the background image for all site pages. Direct link to image: https://pixabay.com/photos/landscape-building-architecture-1303550/
- **Amiresponsive** (https://ui.dev/amiresponsive) was used to generate the mock-up image for the readme.
- **Balsamiq Wireframes** (https://balsamiq.com/) was used extensively during planning to guide the structure and layout of the website.
- **WebAim Contrast checker** (https://webaim.org/resources/contrastchecker/) was used to check the viability of the colour scheme.
- **Flaticon** was used to source the icon for the tab in browser. Attribution link: https://www.flaticon.com/free-icons/water-mill
- **Font Awesome** for iconography, link to personal kit: https://kit.fontawesome.com/3af9805755.js

### Testing
- **W3C HTML Validator** (https://validator.w3.org/) was used for testing HTML.
- **W3C CSS Validator** (https://jigsaw.w3.org/css-validator/) was used for testing CSS.
- **JSHint Validator** (https://jshint.com/) was used for testing JavaScript.
- **Autoprefixer** (https://autoprefixer.github.io/) was used to ensure portability of stylesheet across different browsers.

### Special Thanks
Special thanks to my mentor Cans and all of the amazing CI tutors for their unwavering support, quick responses, and kind encouragement. 
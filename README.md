# PLANNR
#### Video Demo:  <(https://youtu.be/oQ93m1MQVco)>
#### Description:
PLLANR is an innovative productivity application designed to help users manage their tasks efficiently through various features, including template creation, a Pomodoro timer, and a task timer. The application provides an intuitive interface with a sleek design, enhancing the user experience while ensuring effective time management. The core functionality revolves around creating and managing templates, each consisting of different tasks with specified time intervals. Additionally, the Pomodoro timer supports users in implementing the Pomodoro technique to improve focus and productivity.

So this application lets you create your own templates and edit and delete them.
ALso it lets you use a pomodoro timer
Then you can go to the letsdothis and do your tasks the way it was meant to be

Now lets go ahead and explain this project and every file in it.

Well the structure source has 4 directories and the app.py.actually 3

first up /instance contains the database.db which helps with the functionality of saving the templates and pulling them back when needed.

next up static itself has 3 directories:
1.Css: It has the styles.css:
        Which makes sure with the color scheme and all the other design stuff along with some minimal animations.
2.images:Even though it is named images all it really has is a image and 1 video. 

Project Structure
base.html
This is the main HTML template for the application, providing the foundational structure and layout. It includes:

A responsive navigation bar with an off-canvas sidebar for easy navigation.

A video background (video2.mp4) that creates a visually appealing and dynamic backdrop for the content.

Basic page setup, including linking to custom CSS and Bootstrap for styling.

template_creator.html
This file serves as the interface for creating and managing task templates. It features:

A form for adding new templates, including task names and their respective time intervals.

A dynamic table that allows users to add or remove tasks interactively.

A list of existing templates with options to view details and delete templates.

Integration with Bootstrap for a polished look and feel.

pomodoro.html
This file implements the Pomodoro timer, which helps users apply the Pomodoro technique for better time management. It includes:

A user-friendly interface to set the timer duration.

Buttons to start, pause, and reset the timer.

Real-time updating of the timer display.

Utilizes Bootstrap for consistent styling across the application.

styles.css
This CSS file contains custom styles for the application, ensuring a cohesive dark theme. Key features include:

Basic reset and dark theme settings.

Styles for the navigation bar and off-canvas sidebar.

Smooth transitions and hover effects for interactive elements.

Responsive design adjustments for mobile and smaller screens.

app.py
This is the main backend script for the application, built using Flask and SQLAlchemy. It handles routing, database operations, and rendering of HTML templates. Key components include:

Database Configuration: Sets up an SQLite database and initializes SQLAlchemy.

Models: Defines Template and Task models to store templates and their associated tasks.

Routes:

/: Renders the home page (base.html).

/templates: Handles template creation and rendering of the template_creator.html.

/templates/delete/<int:template_id>: Deletes a specified template.

/pomodoro: Renders the pomodoro.html page.

/letsdothis: Renders the letsdothis.html page and handles form submission.

/get_templates: Returns a list of all templates in JSON format.

/get_tasks/<int:template_id>: Returns tasks associated with a specified template in JSON format.

Database Initialization: Ensures tables are created during startup.

letsdothis.html
This file provides the interface for managing and timing tasks using templates. It includes:

A form to select a template and task.

A task timer that updates in real-time with start, pause, and reset functionalities.

Integration with the backend to fetch templates and tasks dynamically.

Utilizes Bootstrap for consistent and responsive styling.

Design Choices
Video Background
The use of a video background in base.html was chosen to create an engaging and modern user experience. This dynamic element helps maintain user interest and provides a visually appealing interface.

Off-Canvas Sidebar
An off-canvas sidebar was implemented to ensure easy navigation without cluttering the main interface. This design choice aligns with modern web design practices and improves the overall user experience.

Dark Theme
A dark theme was selected to reduce eye strain, especially for users working long hours. The consistent dark theme across all pages, controlled by styles.css, ensures a uniform and professional appearance.

Real-Time Timer Updates
Implementing real-time timer updates in pomodoro.html and letsdothis.html ensures that users can monitor their progress accurately. This functionality is crucial for time management applications, where precision is paramount.

Future Improvements
User Authentication: Implement user authentication to allow personalized experiences and save user preferences.

Analytics: Add features to track and analyze user productivity over time.

Notifications: Integrate notifications to alert users when timers end or tasks are due.

Conclusion
PLLANR is a comprehensive productivity tool designed to enhance time management through its intuitive interfaces and dynamic features. The careful design choices and thorough documentation reflect a commitment to creating a user-friendly and efficient application. With further improvements, PLLANR has the potential to become an indispensable tool for productivity enthusiasts.

# TaskZap

#### A Task Management Application
![taskzap logo](./static/images/taskzap-logo.png)


## Description
TaskZap is a task management and tracking application designed to help users stay organized, focused, and productive. The app allows users to create, update, and manage tasks efficiently, keeping everything centralized in a clean and intuitive interface. TaskZap was built to provide a practical solution for organizing daily responsibilities while reinforcing core CRUD functionality within a full-stack web application.

This project was also an opportunity to further expand my experience with Python and Django. I intentionally challenged myself to implement new Django features, strengthen my understanding of models, views, templates, and relational data, and improve overall backend structure. On the frontend, I pushed my CSS skills further by integrating Bootstrap to create a responsive, polished UI while still applying custom styling to refine the user experience. TaskZap reflects both my technical growth and my commitment to building clean, functional applications.

The app is built using Python and the Django web framework, leveraging Django’s built-in ORM, authentication system, and form handling to manage data and user interactions efficiently. For the frontend, I used HTML, CSS, and Bootstrap 5 to create a responsive and visually appealing interface. The project also makes use of the Django messages framework for user feedback and utilizes static file management to serve assets like images and custom stylesheets.

## Table of Contents
* [Technologies Used](#technologiesused)
* [Features](#features)
* [Design](#design)
* [Project Next Steps](#nextsteps)
* [Deployed App](#deployment)
* [About the Author](#Author)

## <a name="technologiesused"></a>Technologies Used 
* Python
* Django
* PostgreSQL
* CSS3
* HTML5
* Boostrap 5
* JavaScript
* Django Templates
* Django ORM
* Django Admin
* Django Authentication
* SQL



## Features
* User Authentication and account-based task management
* Full CRUD functionality 
* Relational database structure using PostgreSQL
* Responsive Boostrap Styling
* Secure, protected routes for authenticated users
* REST Routes
* Confirmation Pages for destructive actions
* Intuitive navigation system
* Streamlined form handling with Django forms



## Wireframe Link
* https://lucid.app/lucidspark/b0aa772d-6560-4e3c-a853-599184b61813/edit?page=0_0#
## Trello Planning
* https://trello.com/b/GFecE0qq/taskzap-plan-board

## <a name="design"></a>Design
TaskZap was designed around a bold thunder and lightning theme to reflect energy, momentum, and productivity. I wanted the visual identity of the application to feel powerful and dynamic — aligning with the idea that completing tasks should feel impactful. Dark gradient backgrounds, high-contrast typography, and sharp accent colors were intentionally chosen to create a modern interface that feels focused while minimizing distractions. The overall aesthetic reinforces the idea of “striking down” tasks efficiently.

From a layout perspective, I implemented a card-based design using Bootstrap to clearly separate each task into its own visual container. This approach improves readability, creates strong visual hierarchy, and allows users to quickly scan their task list without feeling overwhelmed. The spacing, alignment, and consistent structure help maintain clarity while supporting responsive behavior across different screen sizes.




## <a name="nextsteps"></a>Project Next Steps
#### List of Future Features
* Allow users to filter tasks by status (completed/incomplete), due date, or priority to improve organization and workflow efficiency
* Introduce user roles such as “Admin” or “Manager” with the ability to assign tasks to other users, enabling collaborative task management.
* Expand the data models to support multi-user task ownership and team-based workflows.
* Implement automated reminders via email or SMS to help users stay on track with deadlines.
* Add additional lightning-inspired themes and customizable visual modes (e.g., light mode, high-contrast mode)
* Add multiple lighting modes (light/dark etc.)
* Create a productivity dashboard with task completion statistics and visual insights.


## Github repository
* You can view the repository:
[Github.com](https://github.com/Zebyrod/todo-django-crud-app)
* If unable to view please go live locally through VS Code

## Live link
* You can view the deployed site here:
[Taskzap](https://taskzap-218aece0a6e2.herokuapp.com/)
* If unable to view please go live locally through VS Code 

## <a name="Zebastian Rodriguez"></a>The Developer
* Zebastian [GitHub](https://github.com/Zebyrod) [LinkedIn](https://www.linkedin.com/in/zebastian-rodriguez-480191309/)

I started learning to code on my own, just out of curiosity. What began as a personal interest quickly turned into a real passion. Wanting to take it further, I decided to take a risk and enroll in the General Assembly Software Engineering Bootcamp.

The course was challenging — there were definitely moments where I was pushed outside my comfort zone — but that’s exactly what made it so valuable. It gave me the tools, structure, and support I needed to grow. One of the biggest takeaways was realizing how much I’m actually capable of when I commit to something.

TaskZap represents that growth. This project allowed me to apply everything I’ve learned while continuing to challenge myself beyond the curriculum. From strengthening my understanding of Python and Django to refining my frontend design skills with Bootstrap and custom CSS, I intentionally used this application as a way to push my technical abilities further. More than just a task manager, TaskZap reflects my progression from curiosity-driven learner to confident full-stack developer focused on building clean, functional, and scalable applications.

I’m now seeking an opportunity as a junior developer where I can contribute to a collaborative team, continue expanding my technical skill set, and bring the same level of dedication and growth mindset that fueled the creation of this project.

    
## Works Cited:
* Bootstrap 

Bootstrap is an open-source CSS framework used to build responsive, mobile-first websites quickly and efficiently. It provides prebuilt components like grids, buttons, navigation bars, forms, and more — helping developers save time while maintaining consistent design.

I used Bootstrap to style Taskzap, including layout structure, form styling, buttons, and navigation bar
- https://getbootstrap.com/docs/5.3/getting-started/introduction/
- https://www.w3schools.com/bootstrap5/

* Custom CSS Static Files

Custom CSS was integrated into this project using Django's static file config to ensure proper asset loading across the production environment. By extending the Bootstrap's default classes and overriding specific styles, I was able to maintain responsiveness while achieving the theme I was aiming for. This helped to reinforce my understanding of not only how Django manages static files, but how to layer styling with a template using Bootstrap. As a developer I always felt like CSS and styling was was weakest area, and I can say I am pretty proud of some of the cool and complex styling I was able to incorporate into this project.


- https://getbootstrap.com/docs/5.3/getting-started/introduction/
- https://docs.djangoproject.com/en/6.0/howto/static-files/
- https://www.youtube.com/watch?v=z2LQYsZhsFw
- https://www.youtube.com/watch?v=u_GIT5MJAtc&t=257s


* DateTime Fields

I leveraged Django's built-in DateTimeField functionality to automatically track important metadata such as time of creation, due dates, time of completion etc. By incorporating these fields into my models, the application maintains accurate time-based records without requiring manual input from the users. This made entering the data feel great, while also allowing the opportunity for further expansion with future features like sorting or deadline based reminders.


- https://www.geeksforgeeks.org/python/datetimefield-django-models/
- https://docs.djangoproject.com/en/6.0/ref/models/fields/
- https://www.youtube.com/watch?v=3Csl3PcWU8I
- https://www.youtube.com/watch?v=y3XT3L66Z_Q


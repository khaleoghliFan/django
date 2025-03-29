This project is a To-Do List with AI web application built using Django with a Perceptron-based priority system. 
### The main features include:
- ask Management – Users can add, complete, and delete tasks.
- Priority Calculation – Each task is assigned a priority based on urgency and importance using a Perceptron algorithm.
- Sorting Mechanism – Tasks are automatically sorted, with high-priority tasks appearing at the top.
- Responsive UI – The interface is designed with HTML, CSS, and Django templates to enhance user experience.( i have just upload files that has been changed in django project for some resoan other files didn't attach to this repository.
- Success Message Page – After marking a task as completed, the user is redirected to a page displaying a success message
### How It Works:
 - 1- The user submits a task title, an urgency score (0-1), and an importance score (0-1).
 - 2- The Perceptron function calculates whether the task is high-priority (🔴) or normal (🟢).
 - 3- The tasks are sorted based on priority and displayed in a structured table.
 - 4- Users can complete or delete tasks, and completed tasks redirect to a success message page.

The project follows Django best practices, including template inheritance, static files management, and database-driven task storage using Django’s ORM and models.

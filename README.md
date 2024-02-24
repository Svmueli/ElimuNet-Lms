
# Learning Management System (LMS)

## Overview
This is a Learning Management System (LMS) built using Python and Django framework. The system aims to provide an online platform for managing courses, assignments, resources, and user profiles for administrators, teachers, and students. Additionally, it includes an AI assistant powered by Google's Gemini API for enhanced user interactions.

## Features
- **Signup:** Administrators, teachers, and students can sign up for accounts.
- **Login:** Users can log in to their accounts.
- **Logout:** Users can log out of their accounts.
- **Course Management:**
  - Creation and deletion of courses.
- **Assignment Management:**
  - Creation, submission, and deletion of assignments.
  - Grade submission for assignments.
- **Resource Management:**
  - Creation and deletion of resources related to courses.
- **Reports Generation:**
  - Generation of downloadable reports based on various parameters.
- **User Profile:**
  - Users can view and update their profiles.
- **AI Assistant:**
  - Integration of Google's Gemini API for AI-powered interactions.

## Tech Stack
- Python
- Django
- HTML
- CSS
- Bootstrap
- SQLite (database)
- Google's Gemini API

## Setup
1. Clone the repository:
   ```
   git clone <repository_url>
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up the database:
   ```
   python manage.py migrate
   ```
4. Create a superuser for admin access:
   ```
   python manage.py createsuperuser
   ```
5. Run the development server:
   ```
   python manage.py runserver
   ```
6. Access the application at `http://localhost:8000`.

## Usage
- Navigate to the signup page to create an account.
- Log in with your credentials.
- Explore different functionalities based on your role (admin, teacher, or student).
- Interact with the AI assistant for assistance or guidance.

## Contributing


## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgements
- [Django Documentation](https://docs.djangoproject.com/en/stable/)
- [Google's Gemini API Documentation](https://developers.google.com/gemini)
```


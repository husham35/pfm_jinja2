# Personal Finance Manager

The Personal Finance Manager is a Flask-based web application that allows registered users to manage their personal finances. Users can create budgets, track expenses, and categorize their spending. The app provides a structured way to manage expenses under different categories, ensuring users can maintain a clear view of their financial activities.

## Features

- User registration and authentication
- Create, read, update, and delete (CRUD) operations on budgets
- Track expenses and categorize them
- Predefined expense categories (Needs, Wants, Bills) and the ability for users to create their own categories
- Detailed overview of expenses and budgets

## Technologies Used

- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Login
- SQLite (can be replaced with PostgreSQL or any other SQL database)

### Prerequisites

- Python 3.x
- Flask

### Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/husham35/pfm_jinja2.git
   cd pfm_jinja2
   ```

2. **Create a virtual environment**:

   ```
   python3 -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```
   pip install -r requirements.txt
   ```

4. **Set up the database**:

   ```
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

5. **Set up the database**:

   ```
   flask run
   ```

6. **Contact**:

   ```
   For any inquiries or feedback, please contact [husham35@gmail.com].
   ```

### Explanation:

1. **Introduction**: Brief overview of what the app does.
2. **Features**: Key functionalities of the app.
3. **Technologies Used**: List of technologies used in the app.
4. **Clone the repository**: Clone the repository for your use
5. **Create a virtual environment**: Create the virtual environment for the app
6. **Install dependencies**: Install the required depencies to run the app
7. **Set up the database**: Set up the database
8. **Contact**: Contact the repo owner

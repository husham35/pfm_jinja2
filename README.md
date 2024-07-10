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

## Installation

### Prerequisites

- Python 3.x
- Flask

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/personal-finance-manager.git
   cd personal-finance-manager
   ```

python3 -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`

pip install -r requirements.txt

flask db init
flask db migrate -m "Initial migration"
flask db upgrade

flask run

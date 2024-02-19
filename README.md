# Dynamic Delivery Time Calculator

## Overview
This Django project is a web application that calculates the estimated delivery time for orders dynamically based on the distance between the customer's location and the restaurant. It utilizes the OpenRouteService API to calculate the travel time and provides users with accurate delivery time estimates.

## Requirements
- Python 3.x
- Django 5.0.2
- Django Rest Framework (DRF) 3.14.0
- Geopy 2.4.1
- OpenRouteService 2.3.3
- Psycopg2 2.9.9 (for PostgreSQL database)
- Requests 2.31.0

## Installation
1. **Clone this repository to your local machine:**
    ```bash
    git clone https://github.com/your_username/your_project.git
    ```
2. **Navigate to the project directory:**
    ```bash
    cd your_project
    ```
3. **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Configuration
1. **Rename the `.env.example` file to `.env`:**
    ```bash
    mv .env.example .env
    ```
2. **Update the `.env` file with your configuration settings, including the OpenRouteService API key.**
3. **Set up the PostgreSQL database:**
    - Install PostgreSQL if not already installed.
    - Create a new database for the project.
    - Update the `DATABASES` setting in the `settings.py` file with the database name, user, password, and host.

## Database Setup
1. **Run migrations to create the database schema:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

## Running the Application
1. **Start the Django development server:**
    ```bash
    python manage.py runserver
    ```
2. **Open a web browser and navigate to `http://127.0.0.1:8000` to access the application.**

## Usage
- **Create customers, food menus, and restaurants via the provided APIs or Django admin interface.**
- **Place orders by specifying the customer, food, and restaurant.**
- **The estimated delivery time for orders will be automatically calculated based on real-time traffic conditions using the OpenRouteService API.**

## API Endpoints
- **`/customers/`: CRUD endpoints for managing customers.**
- **`/foodmenus/`: CRUD endpoints for managing food menus.**
- **`/restaurants/`: CRUD endpoints for managing restaurants.**
- **`/orders/`: CRUD endpoints for managing orders.**

.



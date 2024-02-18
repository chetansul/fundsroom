# Dynamic Delivery Time Calculator

## Overview
This Django project is a web application that calculates the estimated delivery time for orders dynamically based on the distance between the customer's location and the restaurant. It utilizes the OpenRouteService API to calculate the travel time and provides users with accurate delivery time estimates.

## Requirements
- Python 3.x
- Django 3.x
- Geopy
- OpenRouteService

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

## Running the Application
1. **Apply migrations to create the database schema:**
    ```bash
    python manage.py migrate
    ```
2. **Start the Django development server:**
    ```bash
    python manage.py runserver
    ```
3. **Open a web browser and navigate to `http://127.0.0.1:8000` to access the application.**

## Usage
- **Create customers, food menus, and restaurants via the provided APIs or Django admin interface.**
- **Place orders by specifying the customer, food, and restaurant.**
- **The estimated delivery time for orders will be automatically calculated based on real-time traffic conditions using the OpenRouteService API.**

## API Endpoints
- **`/customers/`: CRUD endpoints for managing customers.**
- **`/foodmenus/`: CRUD endpoints for managing food menus.**
- **`/restaurants/`: CRUD endpoints for managing restaurants.**
- **`/orders/`: CRUD endpoints for managing orders.**

## Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

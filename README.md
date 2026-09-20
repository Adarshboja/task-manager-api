# task-manager-api

A robust and scalable Django REST Framework application providing comprehensive endpoints for managing tasks, complete with user authentication and authorization features.

## Table of Contents

-   [Overview](#overview)
-   [Problem Statement](#problem-statement)
-   [Features](#features)
-   [Tech Stack](#tech-stack)
-   [Architecture](#architecture)
-   [Structure](#structure)
-   [Installation](#installation)
-   [Configuration](#configuration)
-   [Usage](#usage)
-   [Testing](#testing)
-   [CI/CD](#cicd)
-   [Future Improvements](#future-improvements)
-   [License](#license)

---

## Overview

`task-manager-api` is a backend service built using Python and Django REST Framework, designed to power task management applications. It offers a secure and efficient way to create, retrieve, update, and delete tasks, ensuring that users can only interact with tasks they own. The API provides a clear, consistent interface, making it suitable for integration with various frontend clients (web, mobile, desktop).

## Problem Statement

In today's fast-paced environments, effective task management is crucial for productivity. Existing solutions often lack programmatic interfaces, robust security, or the flexibility required for custom application development. This project addresses the need for a modern, extensible, and secure API backend that provides core task management functionalities alongside user authentication and authorization, enabling developers to build sophisticated task-centric applications with ease.

## Features

*   **User Authentication & Authorization:** Secure user registration, login, and token-based authentication (e.g., JWT or Token Authentication) to protect API endpoints. Users can only access their own tasks.
*   **Task CRUD Operations:**
    *   **Create:** Create new tasks with details like title, description, and status.
    *   **Retrieve:** Fetch a list of all tasks for the authenticated user, or retrieve a specific task by ID.
    *   **Update:** Modify existing task details (e.g., title, description, status).
    *   **Delete:** Remove tasks that are no longer needed.
*   **RESTful API Design:** Adherence to REST principles for intuitive and predictable API interactions.
*   **Database Integration:** Seamless data persistence with a relational database.
*   **Scalability:** Built on Django, ensuring a solid foundation for future scaling and feature additions.

## Tech Stack

*   **Language:** Python 3.x
*   **Web Framework:** Django 3.x / 4.x
*   **API Framework:** Django REST Framework
*   **Database:** PostgreSQL (recommended for production), SQLite (default for development)
*   **Dependency Management:** `pip`
*   **Authentication:** Django's built-in User model, DRF's authentication classes (e.g., `rest_framework.authtoken` or `djangorestframework-simplejwt`)

## Architecture

The `task-manager-api` follows a typical N-tier (or 3-tier) client-server architecture:

1.  **Client Layer:** Any frontend application (web, mobile, desktop) that consumes the API.
2.  **API Layer (Application/Logic Layer):**
    *   **Django REST Framework:** Handles API requests, routing, serialization/deserialization of data, view logic, and permission checks.
    *   **Django Core:** Manages URLs, settings, and serves as the underlying web framework.
    *   **Business Logic:** Custom code for task and user management, ensuring data integrity and application-specific rules.
3.  **Data Layer:**
    *   **Database:** Stores all user and task-related information. Leverages Django's ORM for database interactions.

Authentication and Authorization are handled within the API layer, leveraging DRF's robust permission and authentication systems to secure access to resources.

## Structure

The project adheres to a standard Django project layout, organized into distinct applications for modularity:

```
task-manager-api/
├── .env.example                # Example environment variables
├── .gitignore                  # Files/directories to ignore in Git
├── README.md                   # Project documentation
├── manage.py                   # Django's command-line utility
├── requirements.txt            # Python dependencies
├── core/                       # Main Django project settings (e.g., task_manager_api/ in default setup)
│   ├── settings.py             # Project settings
│   ├── urls.py                 # Main URL routing
│   ├── wsgi.py                 # WSGI configuration
│   └── asgi.py                 # ASGI configuration (if async features)
├── tasks/                      # Django app for task management
│   ├── admin.py                # Admin interface customization
│   ├── apps.py                 # App configuration
│   ├── migrations/             # Database migrations
│   ├── models.py               # Task data models
│   ├── serializers.py          # DRF serializers for tasks
│   ├── urls.py                 # Task-specific URL routing
│   └── views.py                # DRF viewsets/views for tasks
└── users/                      # Django app for user management and authentication
    ├── admin.py
    ├── apps.py
    ├── migrations/
    ├── models.py               # User models (if custom user model is used)
    ├── serializers.py          # DRF serializers for users
    ├── urls.py                 # User-specific URL routing (e.g., registration, login)
    └── views.py                # DRF viewsets/views for users
```

## Installation

Follow these steps to set up and run the `task-manager-api` locally:

1.  **Prerequisites:**
    *   Python 3.8+
    *   `pip` (Python package installer)
    *   `git`

2.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/task-manager-api.git
    cd task-manager-api
    ```

3.  **Create and activate a virtual environment:**
    It's recommended to use a virtual environment to manage project dependencies.
    ```bash
    python -m venv venv
    # On macOS/Linux:
    source venv/bin/activate
    # On Windows:
    venv\Scripts\activate
    ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Environment Configuration:**
    Create a `.env` file in the project root based on `.env.example`.
    ```
    # .env
    DEBUG=True
    SECRET_KEY='your_super_secret_key_here'
    DATABASE_URL='sqlite:///db.sqlite3' # For PostgreSQL: postgresql://user:password@host:port/dbname
    # Additional settings like EMAIL_HOST, etc., if applicable
    ```
    Ensure `SECRET_KEY` is a strong, unique, and confidential value in production.

6.  **Database Migrations:**
    Apply the necessary database migrations to create tables for users and tasks.
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

7.  **Create a Superuser (Optional, for Django Admin access):**
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to set up username, email, and password.

8.  **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```
    The API will now be running at `http://127.0.0.1:8000/`.

## Configuration

Key configuration aspects are managed through `core/settings.py` and environment variables defined in your `.env` file.

*   **`DEBUG`**: Controls debugging mode. Set to `False` in production.
*   **`SECRET_KEY`**: A unique secret key used for security purposes. **Crucial for production.**
*   **`DATABASE_URL`**: Specifies the database connection string. Uses `dj-database-url` to parse the URL.
    *   Example for SQLite: `DATABASE_URL=sqlite:///db.sqlite3`
    *   Example for PostgreSQL: `DATABASE_URL=postgresql://user:password@host:5432/db_name`
*   **`ALLOWED_HOSTS`**: A list of domain names that this Django site can serve. Must be configured for production.
*   **REST Framework Settings**: Configured in `core/settings.py` under `REST_FRAMEWORK` for authentication classes, permission classes, etc.
    ```python
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_simplejwt.authentication.JWTAuthentication', # Or 'rest_framework.authentication.TokenAuthentication'
        ),
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.IsAuthenticated',
        ),
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 10,
    }
    ```

## Usage

The API provides several endpoints for user authentication and task management.

**Base URL:** `http://127.0.0.1:8000/api/v1/` (assuming versioning and an `api` prefix in `core/urls.py`)

### Authentication Endpoints

Before accessing task endpoints, users need to register and log in to obtain an authentication token.

*   **User Registration:**
    *   **Endpoint:** `POST /api/v1/users/register/`
    *   **Body:**
        ```json
        {
            "username": "newuser",
            "email": "user@example.com",
            "password": "strongpassword123"
        }
        ```
    *   **Response (example with JWT):**
        ```json
        {
            "username": "newuser",
            "email": "user@example.com"
        }
        ```

*   **User Login (Get Token):**
    *   **Endpoint:** `POST /api/v1/token/` (if using `djangorestframework-simplejwt`)
    *   **Body:**
        ```json
        {
            "username": "newuser",
            "password": "strongpassword123"
        }
        ```
    *   **Response (example with JWT):**
        ```json
        {
            "refresh": "eyJ...",
            "access": "eyJ..."
        }
        ```
    *   *Note:* The `access` token is used for subsequent authenticated requests. Include it in the `Authorization` header as `Bearer <access_token>`.

### Task Endpoints (Requires Authentication)

All task endpoints require an `Authorization: Bearer <access_token>` header.

*   **List Tasks / Create Task:**
    *   **Endpoint:** `GET /api/v1/tasks/`
    *   **Method:** `GET` (List tasks) / `POST` (Create task)
    *   **`GET` Response:**
        ```json
        [
            {
                "id": 1,
                "title": "Buy groceries",
                "description": "Milk, eggs, bread",
                "status": "pending",
                "owner": "newuser",
                "created_at": "2023-10-27T10:00:00Z",
                "updated_at": "2023-10-27T10:00:00Z"
            }
        ]
        ```
    *   **`POST` Body:**
        ```json
        {
            "title": "Learn Django REST Framework",
            "description": "Read documentation and build an API",
            "status": "in_progress"
        }
        ```
    *   **`POST` Response:** (Task object with generated `id`, `owner`, `created_at`, `updated_at`)

*   **Retrieve / Update / Delete Task:**
    *   **Endpoint:** `GET /api/v1/tasks/<id>/`
    *   **Methods:** `GET` (Retrieve), `PUT` (Full Update), `PATCH` (Partial Update), `DELETE` (Delete)
    *   **`GET` Response:** (A single task object similar to the list item)
    *   **`PUT` / `PATCH` Body:**
        ```json
        {
            "title": "Learn Django REST Framework (Completed)",
            "status": "completed"
        }
        ```
    *   **`DELETE` Response:** `204 No Content`

## Testing

The project includes unit and integration tests to ensure the reliability and correctness of the API endpoints and business logic.

To run the tests:
```bash
python manage.py test
```

This command will discover and execute all tests within your Django apps (e.g., `tasks/tests/`, `users/tests/`).

## CI/CD

For continuous integration and continuous deployment, it is recommended to set up pipelines using tools like GitHub Actions, GitLab CI/CD, or Jenkins.

A typical CI/CD pipeline for this project would include the following stages:

1.  **Linting:** Run code linters (e.g., Flake8, Black, Isort) to enforce code style and catch errors.
2.  **Testing:** Execute all project tests (`python manage.py test`).
3.  **Security Scan:** Scan for known vulnerabilities in dependencies (e.g., Bandit).
4.  **Building (Optional):** If packaging the application (e.g., Docker image).
5.  **Deployment:** Deploy the application to a staging or production environment upon successful completion of previous stages.

## Future Improvements

*   **Filtering, Sorting, and Pagination:** Enhance task listing with advanced query capabilities.
*   **Due Dates & Priorities:** Add fields for task due dates and priority levels.
*   **Task Tags/Categories:** Implement a tagging system for better task organization.
*   **Search Functionality:** Allow users to search tasks by title or description.
*   **Dockerization:** Provide a `Dockerfile` and `docker-compose.yml` for easier deployment and environment setup.
*   **API Documentation:** Integrate with tools like `drf-yasg` or `Django REST Swagger` to generate interactive API documentation (OpenAPI/Swagger UI).
*   **Rate Limiting:** Implement safeguards against abusive usage of the API.
*   **Email Notifications:** Add functionality for sending email notifications (e.g., for upcoming task due dates).
*   **User Profile Management:** Allow users to update their email, password, or other profile details.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
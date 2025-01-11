# Event Management API

This is a backend project that implements an **Event Management API** using **Django** and **Django REST Framework** (DRF). The API allows users to manage events, including creating, updating, deleting, and viewing upcoming events. It also includes user authentication, event capacity management, and several filtering options.

## Project Overview

The goal of this project is to build a fully functional API for managing events. This API supports the following key features:

- Event CRUD (Create, Read, Update, Delete) operations
- User management with authentication and permissions
- Event filtering by title, location, and date range
- Capacity management to prevent overselling events

## Functional Requirements

### Event Management (CRUD)
- Implement the ability to Create, Read, Update, and Delete (CRUD) events.
- Each event has the following attributes:
  - Title
  - Description
  - Date and Time
  - Location
  - Organizer
  - Capacity (maximum number of attendees)
  - Created Date
- Prevent creating events with past dates.

### User Management (CRUD)
- Implement CRUD operations for users (Username, Email, Password).
- Users can only manage their own events, ensuring that they can update or delete events they created.

### View Upcoming Events
- An endpoint to list all upcoming events with the option to filter by:
  - Title
  - Location
  - Date Range

### Event Capacity Management
- Ensure each event has a maximum capacity and prevent new registrations once it's full.
- Optionally, implement a waitlist feature when an event is fully booked.

### Authentication and Permissions
- Use Django’s built-in authentication system to secure the API.
- Implement permissions to ensure that users can only interact with their own events.

### Deployment
- The API is deployed on a cloud platform such as **Heroku** or **PythonAnywhere** for production use.

## Technical Requirements

- Use **Django ORM** to interact with the database.
- Define models for **Events** and **Users** with appropriate relationships.
- Implement authentication using **Django REST Framework**.
- Ensure proper error handling and use HTTP status codes (e.g., 404 for not found, 400 for bad request).
- Use **JWT (JSON Web Tokens)** for secure API authentication.
- Ensure that the API is fully functional, including pagination for event lists and proper filtering.

## Setup and Installation

### Prerequisites

Before starting, ensure you have the following installed:

- Python 3.8 or later
- MySQL (or any database of your choice)
- Virtualenv or `venv`

### Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/event-management-api.git
cd event-management-api
```

### Set Up Virtual Environment

Create a virtual environment for the project:

```bash
python -m venv env
```

Activate the virtual environment:

- For Windows:

```bash
env\Scripts\activate
```

- For macOS/Linux:

```bash
source env/bin/activate
```

### Install Dependencies

Install the required packages using `pip`:

```bash
pip install -r requirements.txt
```

### Set Up Database

1. Configure the database in `settings.py` for MySQL:
   - Update the `DATABASES` setting in `settings.py` with your MySQL credentials.

2. Run migrations to set up the database:

```bash
python manage.py migrate
```

### Create Superuser

To create an admin user:

```bash
python manage.py createsuperuser
```

Follow the prompts to create the superuser account.

### Collect Static Files

Run the following command to collect static files for the project:

```bash
python manage.py collectstatic
```

### Running the Server

Start the development server:

```bash
python manage.py runserver
```

You can now access the API locally at `http://127.0.0.1:8000/`.

## API Endpoints

Here are the key API endpoints for managing events:

1. **Create an Event:**
   - **POST** `/api/events/`
   - Requires authentication (JWT).
   - Request body:
     ```json
     {
       "title": "Event Title",
       "description": "Event Description",
       "date_time": "2025-01-12T14:00:00Z",
       "location": "Event Location",
       "capacity": 100
     }
     ```

2. **Get All Upcoming Events:**
   - **GET** `/api/events/`
   - Filters for title, location, and date range are available.

3. **Get Event Details:**
   - **GET** `/api/events/{id}/`
   - Requires event ID.

4. **Update an Event:**
   - **PUT** `/api/events/{id}/`
   - Requires authentication and permission to update the event.

5. **Delete an Event:**
   - **DELETE** `/api/events/{id}/`
   - Requires authentication and permission to delete the event.

6. **User Authentication:**
   - **POST** `/api/token/` to obtain a JWT token.

7. **Refresh JWT Token:**
   - **POST** `/api/token/refresh/` to refresh your JWT token.

## Deployment

To deploy your API, follow the steps for deploying a Django application to platforms like **Heroku** or **PythonAnywhere**. 

1. **Heroku Deployment:**
   - Install the Heroku CLI and log in.
   - Create a Heroku app using `heroku create`.
   - Push the code to Heroku using `git push heroku main`.
   - Set up environment variables for your database and secret key in Heroku.

2. **PythonAnywhere Deployment:**
   - Create a PythonAnywhere account.
   - Set up a new web app and select **Django** as the framework.
   - Configure the database settings and environment variables in the PythonAnywhere dashboard.
   - Push the code to PythonAnywhere or clone it from GitHub.

## Future Improvements

- Implement a waitlist feature for fully booked events.
- Add email notifications for event registration and updates.
- Improve filtering by adding more criteria such as event type or tags.

## License

This project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for more information.

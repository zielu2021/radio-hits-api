# Radio Hits API

A Django REST API with Frontend for managing songs (hits) and artists for a hypothetical radio station.

## Overview

This project provides a complete solution for managing radio hits and artists with:

- RESTful API endpoints for data management
- Modern frontend interface built with Bootstrap
- Automatic URL slug generation
- Database models with proper relationships
- Unit tests
- Data population command
- Docker containerization
- Cloud deployment with HTTPS

## Live Demo

The application is deployed and available at: https://radio-hits-api.onrender.com/

![radio-hits-api-up-and-running](screenshots/13.png)

## Technical Stack

- Python 3.10+
- Django 5.2+
- Django REST Framework
- PostgreSQL 14+
- Bootstrap 5
- JavaScript (Fetch API)
- HTML/CSS
- Docker & Docker Compose
- CI/CD via Render

## Database Schema

### Artist
- id (PK)
- first_name (CharField)
- last_name (CharField)
- created_at (DateTimeField)
- full_name (property)

### Hit
- id (PK)
- title (CharField)
- artist (FK to Artist)
- title_url (SlugField, unique, auto-generated)
- created_at (DateTimeField)
- updated_at (DateTimeField)

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/hits/` | List all hits (limited to 20, sorted by creation date) |
| GET | `/api/v1/hits/{title_url}/` | Get details of a specific hit |
| POST | `/api/v1/hits/` | Create a new hit |
| PUT | `/api/v1/hits/{title_url}/` | Update an existing hit |
| DELETE | `/api/v1/hits/{title_url}/` | Delete a hit |
| GET | `/api/v1/artists/` | List all artists |
| GET | `/api/v1/artists/{id}/` | Get details of a specific artist |

## Response Codes

- 200: Successful GET or PUT request
- 201: Successful POST request (resource created)
- 204: Successful DELETE request (no content)
- 400: Bad request (invalid data)
- 404: Resource not found
- 500: Server error

## Local Development Setup

### Option 1: Traditional Setup

1. Clone the repository
```bash
git clone https://github.com/zielu2021/radio-hits-api.git
cd radio_hits_api
```

2. Set up a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up the database
```bash
python manage.py migrate
```

5. Populate database with initial data
```bash
python manage.py populate_data
```

6. Run the development server
```bash
python manage.py runserver
```

7. Access the application
   - Frontend: http://localhost:8000/
   - API: http://localhost:8000/api/v1/

### Option 2: Docker Setup

1. Clone the repository
```bash
git clone https://github.com/zielu2021/radio-hits-api.git
cd radio_hits_api
```

2. Build and start the Docker containers
```bash
docker-compose build
docker-compose up
```

3. Access the application
   - Frontend: http://localhost:80/
   - API: http://localhost:80/api/v1/

## Running Tests

```bash
python manage.py test
```

## Deployment

The application is deployed using Docker containers on Render.com with the following setup:

1. Web Service: Containerized Django application
2. Database: PostgreSQL 14
3. HTTPS: Automatically provided by Render

To deploy your own instance:

1. Fork this repository
2. Create an account on [Render](https://render.com/)
3. Create a new Blueprint and connect your repository
4. Render will automatically detect the `render.yaml` file and deploy the services


## API Usage Examples

### Create a new hit (POST)

```
POST /api/v1/hits/

{
  "title": "New Hit",
  "artist_id": 1
}
```

Response:
```json
{
  "id": 54,
  "title": "New Hit",
  "artist": {
    "id": 7,
    "first_name": "John",
    "last_name": "Doe",
    "created_at": "2025-04-16T09:30:30.755012Z",
    "full_name": "John Doe"
  },
  "title_url": "new-hit",
  "created_at": "2025-04-16T09:54:57.765240Z",
  "updated_at": "2025-04-16T09:54:57.765257Z"
}
```

Note: The `title_url` is automatically generated from the title.

### Get hit details (GET)

```
GET /api/v1/hits/new-hit/
```

### Update a hit (PUT)

```
PUT /api/v1/hits/new-hit/

{
  "title": "Changed Title Hit",
  "artist_id": 7
}
```

Response:
```json
{
  "id": 55,
  "title": "Changed Title Hit",
  "artist": {
    "id": 7,
    "first_name": "John",
    "last_name": "Doe",
    "created_at": "2025-04-16T09:30:30.755012Z",
    "full_name": "John Doe"
  },
  "title_url": "changed-title-hit",
  "created_at": "2025-04-16T10:09:05.479459Z",
  "updated_at": "2025-04-16T10:10:02.622033Z"
}
```

Note: The `title_url` is automatically updated when the title changes.

### Delete a hit (DELETE)

```
DELETE /api/v1/hits/changed-title-hit/
```

Returns a 204 No Content response if successful.

## Frontend Features

The frontend provides a user-friendly interface for managing hits and artists:

- Home page with overview and latest hits
- Complete hits management (listing, viewing, creating, editing, deleting)
- Artists management
- Responsive design with Bootstrap 5
- Interactive modals for adding and editing
- Client-side form validation

## Screenshots

![Radio Hits Home Page](screenshots/6.png)
*Radio Hits Home Page*

![Hits List Page](screenshots/7.png)
*Hits List Page with Management Options*

![Artists List Page](screenshots/8.png)
*Artists List Page*

![Add New Artist Modal](screenshots/9.png)
*Adding a New Artist via Modal*

![Add New Hit Modal](screenshots/10.png)
*Adding a New Hit via Modal*

![Hit Detail Page](screenshots/11.png)
*Hit Detail Page with Full Information*

![Delete Confirmation Modal](screenshots/12.png)
*Delete Confirmation Modal*

![Postman_GET](screenshots/1.png)
*Postman GET API*

![Postman_GET](screenshots/1b.png)
*Postman GET API DETAILS*

![Postman_PUT](screenshots/2.png)
*Postman PUT API*

![Postman_POST](screenshots/3.png)
*Postman POST API*

![Postman_DELETE](screenshots/4.png)
*Postman DELETE API*

![Postman_GET_DELETE](screenshots/5.png)
*Postman GET AFTER DELETE API*

## Project Structure

```
radio_hits_api/
├── api/                        # API app
│   ├── management/
│   │   └── commands/
│   │       └── populate_data.py  # Data population command
│   ├── migrations/
│   ├── models.py               # Database models
│   ├── serializers.py          # API serializers
│   ├── tests.py                # API unit tests
│   ├── urls.py                 # API URL routing
│   └── views.py                # API views
├── frontend/                   # Frontend app
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css      # Custom CSS
│   │   └── js/
│   │       └── scripts.js      # Shared JavaScript
│   ├── templates/
│   │   ├── base.html           # Base template
│   │   ├── index.html          # Homepage
│   │   ├── hits/
│   │   │   ├── list.html       # Hits list view
│   │   │   └── detail.html     # Hit detail view
│   │   └── artists/
│   │       └── list.html       # Artists list view
│   ├── urls.py                 # Frontend URL routing
│   └── views.py                # Frontend views
├── resthits/                   # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── docker/                     # Docker configuration
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── entrypoint.sh
├── staticfiles/                # Collected static files
├── requirements.txt            # Project dependencies
├── render.yaml                 # Render deployment configuration
└── manage.py                   # Django management script
```

## Features

- Automatic slug generation for hit URLs
- Slug updates when title changes
- Full CRUD operations for hits and artists
- Comprehensive test suite
- Proper validation and error handling
- Database population command for easy setup
- Responsive frontend with Bootstrap
- Interactive user interface
- Client-side form validation
- CSRF protection for secure requests
- Containerized with Docker for easy deployment
- Cloud deployment with automatic HTTPS

## Future Improvements

- User authentication and access control
- Search functionality
- Advanced filtering options
- Pagination controls
- Upload artist images
- Charts for track popularity
- Dark mode theme option
- Admin dashboard for analytics
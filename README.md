# Radio Hits API

A Django REST API for managing songs (hits) and artists for a hypothetical radio station.

## Overview

This API provides endpoints to create, read, update, and delete information about radio hits and their artists. The project includes:

- RESTful API endpoints
- Automatic URL slug generation
- Database models with proper relationships
- Unit tests
- Data population command

## Technical Stack

- Python 3.6+
- Django 3.0+
- Django REST Framework
- PostgreSQL 13+
- Unit tests (Django TestCase)

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

## Installation and Setup

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

## Running Tests

```bash
python manage.py test
```

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

## Screenshots

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
├── api/
│   ├── management/
│   │   └── commands/
│   │       └── populate_data.py  # Data population command
│   ├── migrations/
│   ├── models.py                 # Database models
│   ├── serializers.py            # API serializers
│   ├── tests.py                  # Unit tests
│   ├── urls.py                   # API URL routing
│   └── views.py                  # API views
├── resthits/                     # Project settings
└── manage.py
```

## Features

- Automatic slug generation for hit URLs
- Slug updates when title changes
- Full CRUD operations for hits
- Comprehensive test suite
- Proper validation and error handling
- Database population command for easy setup

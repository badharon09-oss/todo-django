# API Endpoints — To-Do List Web App

## Authentication
- `POST /api/auth/signup/`
  - Create a new user.
  - Body (JSON): `{ "username": "ronald", "email": "r@example.com", "password": "secret123" }`
  - Response: `201 Created` with user info (no password).

- `POST /api/auth/login/`
  - Authenticate user and return token (if using token auth) or session cookie.
  - Body (JSON): `{ "username": "ronald", "password": "secret123" }`
  - Response: `200 OK` with token or session details.

- `POST /api/auth/logout/`
  - Invalidate the current token / session.
  - Auth required.

## Tasks (Require Authentication)
- `GET /api/tasks/`
  - List tasks belonging to authenticated user.
  - Response: `200 OK`, JSON array of tasks.

- `POST /api/tasks/`
  - Create a new task.
  - Body: `{ "title": "Buy milk", "description": "2L", "due_date": "2025-12-10T10:00:00Z" }`
  - Response: `201 Created` with created task.

- `GET /api/tasks/<id>/`
  - Retrieve a task by ID (must belong to user).
  - Response: `200 OK` with task object.

- `PUT /api/tasks/<id>/` or `PATCH /api/tasks/<id>/`
  - Update task fields.
  - Body example (PATCH): `{ "completed": true }`
  - Response: `200 OK` with updated task.

- `DELETE /api/tasks/<id>/`
  - Delete a task.
  - Response: `204 No Content` on success.

- `POST /api/tasks/<id>/complete/`
  - Shortcut to mark a task completed.
  - Body: none or `{ "completed": true }`
  - Response: `200 OK` with updated task.

## Notes
- All task endpoints require authentication.
- Use standard HTTP status codes.
- Response bodies follow JSON format:
  ```json
  {
    "id": 1,
    "title": "Buy milk",
    "description": "2L",
    "due_date": "2025-12-10T10:00:00Z",
    "completed": false,
    "created_at": "2025-11-01T12:00:00Z",
    "updated_at": "2025-11-01T12:00:00Z"
  }

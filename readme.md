# Library Task - Django REST Framework

## Overview

This is a Library Management System built using Django REST Framework. The system allows users to manage books, authors, and library operations efficiently through a RESTful API.

## Prerequisites

Make sure you have the following installed before setting up the project:

- Python 3.x
- Django
- Django REST Framework
- django-cors-headers

## Installation

1. Clone the repository:

```bash
git clone https://github.com/rajatrawal/library-task.git
cd library-task
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
```

3. Activate the virtual environment:

   - On Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - On Unix or MacOS:

     ```bash
     source venv/bin/activate
     ```

4. Install dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Database Setup

1. Apply database migrations:

```bash
python manage.py migrate
```

2. Create a superuser for admin access:

```bash
python manage.py createsuperuser
```

Follow the prompts to create a superuser account.

## Running the Server

Start the Django development server:

```bash
python manage.py runserver
```

Your application should now be accessible at [http://localhost:8000/](http://localhost:8000/).

## API


## Author Account Creation

### URL

`POST http://127.0.0.1:8000/api/author/create`

### Request Body

| Field          | Type   | Description                 |
| -------------- | ------ | --------------------------- |
| username       | string | Author's username           |
| password       | string | Author's password           |
| phone          | string | Author's phone number       |
| city           | string | Author's city               |
| profile_image  | string | URL or path to profile image |

### Example Request

```json
{
  "username": "example_author",
  "password": "securepassword",
  "phone": "123-456-7890",
  "city": "Example City",
  "profile_image": "https://example.com/profile.jpg"
}
```

### Success Response

```json
{
  "id": 1,
  "auth_id": "Generated_Auth_ID",
  "books": [],
  "username": "example_author",
  "password": "securepassword",
  "phone": "123-456-7890",
  "city": "Example City",
  "profile_image": "https://example.com/profile.jpg"
}
```



## Login

### URL

`POST http://127.0.0.1:8000/api/login`

### Request Body

| Field     | Type   | Description            |
| --------- | ------ | ---------------------- |
| username  | string | Author's username      |
| password  | string | Author's password      |

### Example Request

```json
{
  "username": "example_author",
  "password": "securepassword"
}
```

### Success Response

```json
{
  "refresh": "Generated_Refresh_Token",
  "access": "Generated_Access_Token"
}
```



## Get All Authors (Admin Only)

### URL

`GET http://127.0.0.1:8000/api/authors/`

### Authentication

- **Type:** Bearer Token
- **Token:** `Your_Admin_Access_Token`

To acess token use admin following auth  - 
- **username :** admin
- **password :** admin

### Success Response

```json
[
  {
    "id": 1,
    "auth_id": "Generated_Auth_ID_1",
    "books": [],
    "username": "author_1",
    "phone": "123-456-7890",
    "city": "City 1",
    "profile_image": "https://example.com/profile_1.jpg"
  },
  {
    "id": 2,
    "auth_id": "Generated_Auth_ID_2",
    "books": [],
    "username": "author_2",
    "phone": "987-654-3210",
    "city": "City 2",
    "profile_image": "https://example.com/profile_2.jpg"
  },
  // ... other authors
]
```

## Get Single Author Details

### URL

`GET http://127.0.0.1:8000/api/author/14`

### Authentication

- **Type:** Bearer Token
- **Token:** `Your_Access_Token`

### Success Response

```json
{
  "id": 14,
  "auth_id": "Generated_Auth_ID_14",
  "books": [
    {
      "id": 1,
      "title": "Book Title 1",
      "genre": "Fiction",
      "publication_date": "2022-02-01"
    },
    {
      "id": 2,
      "title": "Book Title 2",
      "genre": "Non-Fiction",
      "publication_date": "2022-03-15"
    }
    // ... other books by the author
  ],
  "username": "author_14",
  "phone": "987-654-3210",
  "city": "City 14",
  "profile_image": "https://example.com/profile_14.jpg"
}
```

## Genre API

### URL

`GET http://127.0.0.1:8000/api/genre/`

### Authentication

- **Type:** Bearer Token
- **Token:** `Your_Access_Token`

### Success Response

```json
[
  {
    "id": 1,
    "name": "Fiction"
  },
  {
    "id": 2,
    "name": "Non-Fiction"
  },
  // ... other genres
]
```

### Error Responses

- **401 Unauthorized:** If the provided access token is not valid or the user does not have the required privileges.

---

### URL

`GET http://127.0.0.1:8000/api/genre/1/`

### Authentication

- **Type:** Bearer Token
- **Token:** `Your_Access_Token`

### Success Response

```json
{
  "id": 1,
  "name": "Fiction"
}
```

### Error Responses

- **401 Unauthorized:** If the provided access token is not valid or the user does not have the required privileges.
- **404 Not Found:** If the requested genre with ID 1 does not exist.

---

### URL

`POST http://127.0.0.1:8000/api/genre/`

### Authentication

- **Type:** Bearer Token
- **Token:** `Your_Access_Token`

### Request Body

```json
{
  "name": "Science Fiction"
}
```

### Success Response

```json
{
  "id": 3,
  "name": "Science Fiction"
}
```

### Error Responses

- **401 Unauthorized:** If the provided access token is not valid or the user does not have the required privileges.
- **400 Bad Request:** If the request body is invalid or incomplete.

---

### URL

`PUT http://127.0.0.1:8000/api/genre/1/`

### Authentication

- **Type:** Bearer Token
- **Token:** `Your_Access_Token`

### Request Body

```json
{
  "name": "Updated Fiction"
}
```

### Success Response

```json
{
  "id": 1,
  "name": "Updated Fiction"
}
```

### Error Responses

- **401 Unauthorized:** If the provided access token is not valid or the user does not have the required privileges.
- **404 Not Found:** If the requested genre with ID 1 does not exist.
- **400 Bad Request:** If the request body is invalid or incomplete.

---

### URL

`DELETE http://127.0.0.1:8000/api/genre/1/`

### Authentication

- **Type:** Bearer Token
- **Token:** `Your_Access_Token`

### Success Response

```json
{
  "detail": "Genre with ID 1 has been deleted successfully."
}
```

### Error Responses

- **401 Unauthorized:** If the provided access token is not valid or the user does not have the required privileges.
- **404 Not Found:** If the requested genre with ID 1 does not exist.

## Book API

### URL

`GET http://127.0.0.1:8000/api/book/`

### Authentication

- **Type:** Bearer Token
- **Token:** `Your_Access_Token`

### Success Response

```json
[
  {
    "id": 1,
    "name": "Book Title 1",
    "genre": {
      "id": 1,
      "name": "Fiction"
    },
    "pages": 300,
    "cover_image": "https://example.com/cover_1.jpg",
    "authors": [
      {
        "id": 1,
        "auth_id": "Generated_Auth_ID_1",
        "username": "author_1",
        "phone": "123-456-7890",
        "city": "City 1",
        "profile_image": "https://example.com/profile_1.jpg"
      },
      // ... other authors
    ]
  },
  {
    "id": 2,
    "name": "Book Title 2",
    "genre": {
      "id": 2,
      "name": "Non-Fiction"
    },
    "pages": 250,
    "cover_image": "https://example.com/cover_2.jpg",
    "authors": [
      {
        "id": 2,
        "auth_id": "Generated_Auth_ID_2",
        "username": "author_2",
        "phone": "987-654-3210",
        "city": "City 2",
        "profile_image": "https://example.com/profile_2.jpg"
      },
      // ... other authors
    ]
  },
  // ... other books
]
```

### Error Responses

- **401 Unauthorized:** If the provided access token is not valid or the user does not have the required privileges.

---

### URL

`GET http://127.0.0.1:8000/api/book/1/`

### Authentication

- **Type:** Bearer Token
- **Token:** `Your_Access_Token`

### Success Response

```json
{
  "id": 1,
  "name": "Book Title 1",
  "genre": {
    "id": 1,
    "name": "Fiction"
  },
  "pages": 300,
  "cover_image": "https://example.com/cover_1.jpg",
  "authors": [
    {
      "id": 1,
      "auth_id": "Generated_Auth_ID_1",
      "username": "author_1",
      "phone": "123-456-7890",
      "city": "City 1",
      "profile_image": "https://example.com/profile_1.jpg"
    },
    // ... other authors
  ]
}
```

### Error Responses

- **401 Unauthorized:** If the provided access token is not valid or the user does not have the required privileges.
- **404 Not Found:** If the requested book with ID 1 does not exist.

---

### URL

`POST http://127.0.0.1:8000/api/book/`

### Authentication

- **Type:** Bearer Token
- **Token:** `Your_Access_Token`

### Request Body

```json
{
  "name": "New Book Title",
  "genre": 1,
  "pages": 200,
  "cover_image": "https://example.com/new_cover.jpg",
  "authors": [1, 2]
}
```

### Success Response

```json
{
  "id": 3,
  "name": "New Book Title",
  "genre": {
    "id": 1,
    "name": "Fiction"
  },
  "pages": 200,
  "cover_image": "https://example.com/new_cover.jpg",
  "authors": [
    {
      "id": 1,
      "auth_id": "Generated_Auth_ID_1",
      "username": "author_1",
      "phone": "123-456-7890",
      "city": "City 1",
      "profile_image": "https://example.com/profile_1.jpg"
    },
    {
      "id": 2,
      "auth_id": "Generated_Auth_ID_2",
      "username": "author_2",
      "phone": "987-654-3210",
      "city": "City 2",
      "profile_image": "https://example.com/profile_2.jpg"
    }
  ]
}
```

### Error Responses

- **401 Unauthorized:** If the provided access token is not valid or the user does not have the required privileges.
- **400 Bad Request:** If the request body is invalid or incomplete.

---

### URL

`PUT http://127.0.0.1:8000/api/book/1/`

### Authentication

- **Type:** Bearer Token
- **Token:** `Your_Access_Token`

### Request Body

```json
{
  "name": "Updated Book Title",
  "genre": 2,
  "pages": 220,
  "cover_image": "https://example.com/updated_cover.jpg",
  "authors": [2]
}
```

### Success Response

```json
{
  "id": 1,
  "name": "Updated Book Title",
  "genre": {
    "id": 2,
    "name": "Non-Fiction"
  },
  "pages": 220,
  "cover_image": "https://example.com/updated_cover.jpg",
  "authors": [
    {
      "id": 2,
      "auth_id": "Generated_Auth_ID_2",
      "username": "author_2",
      "phone": "987-654-3210",
      "city": "City 2",
      "profile_image": "https://example.com/profile_2.jpg"
    }
  ]
}
```

### Error Responses

- **401 Unauthorized:** If the provided access token is not valid or the user does not have the required privileges.
- **404 Not Found:** If the requested book with ID 1 does not exist.
- **400 Bad Request:** If the request body is invalid or incomplete.

---

### URL

`DELETE http://127.0.0.1:8000/api/book/1/`

### Authentication

- **Type:** Bearer Token
- **Token:** `Your_Access_Token`

### Success Response

```json
{
  "detail": "Book with ID 1 has been deleted successfully."
}
```
  
### Error Responses

- **401 Unauthorized:** If the provided access token is not valid or the user does not have the required privileges.
- **404 Not Found:** If the requested book with ID 1 does not exist.



## Export Book Data (Admin Only)

### URL

`GET http://127.0.0.1:8000/api/export/{genre}`


### URL Parameters

| Parameter | Type   | Description                  |
| --------- | ------ | ---------------------------- |
| genre     | string | The genre to export data for |

### Success Response

A CSV file containing book data for the specified genre will be downloaded.



## Acknowledgments

- Thanks to the Django and Django REST Framework communities for their excellent documentation and support.


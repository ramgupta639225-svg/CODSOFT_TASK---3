# Library Management System API

A RESTful Library Management System API built using Django and Django REST Framework (DRF).

This project was developed as part of a backend development internship task. The API manages books, authors, members, and issued books with CRUD operations, validation, searching, filtering, sorting, pagination, and book issuing and returning functionality.

## 📌 Task Overview

The objective of this task is to build a backend system that manages:

- Books
- Authors
- Library Members
- Issued Books

The API provides complete CRUD functionality along with data validation, search, filtering, sorting, pagination, book availability management, borrowing records, and appropriate HTTP responses.

## 🚀 Features

### Author Management

- Create a new author
- Retrieve all authors
- Retrieve a single author
- Update author information
- Partially update author information
- Delete an author
- Author name validation
- Email uniqueness validation

### Book Management

- Create a new book
- Retrieve all books
- Retrieve a single book
- Update book information
- Partially update book information
- Delete a book
- ISBN uniqueness validation
- Book title validation
- Author relationship management
- Total copies and available copies management
- Book availability tracking
- Search books
- Filter books by category and author
- Sort books
- Pagination

### Member Management

- Create a new member
- Retrieve all members
- Retrieve a single member
- Update member information
- Partially update member information
- Delete a member
- Email uniqueness validation
- Phone number uniqueness validation
- Member active status management
- Search members
- Filter members
- Sort members
- Pagination

### Issued Book Management

- Issue a book to a member
- Retrieve all issued book records
- Retrieve a single issued book record
- Update issued book information
- Partially update issued book information
- Delete an issued book record
- Return a book
- Track issue dates and due dates
- Maintain return dates and issue status
- Update book availability during issuing and returning
- Prevent duplicate active book issues
- Prevent inactive members from borrowing books
- Validate book availability
- Maintain borrowing records
- Return meaningful success and error responses

## 🛠️ Technologies Used

- Python
- Django
- Django REST Framework
- django-filter
- SQLite
- Git
- GitHub
- Postman for API testing

## 🔗 API Endpoint Summary

| Resource | Method | Endpoint |
|---|---|---|
| Authors | GET | `/api/authors/` |
| Authors | POST | `/api/authors/` |
| Author Detail | GET | `/api/authors/{id}/` |
| Author Detail | PUT | `/api/authors/{id}/` |
| Author Detail | PATCH | `/api/authors/{id}/` |
| Author Detail | DELETE | `/api/authors/{id}/` |
| Books | GET | `/api/books/` |
| Books | POST | `/api/books/` |
| Book Detail | GET | `/api/books/{id}/` |
| Book Detail | PUT | `/api/books/{id}/` |
| Book Detail | PATCH | `/api/books/{id}/` |
| Book Detail | DELETE | `/api/books/{id}/` |
| Members | GET | `/api/members/` |
| Members | POST | `/api/members/` |
| Member Detail | GET | `/api/members/{id}/` |
| Member Detail | PUT | `/api/members/{id}/` |
| Member Detail | PATCH | `/api/members/{id}/` |
| Member Detail | DELETE | `/api/members/{id}/` |
| Issued Books | GET | `/api/issuedbooks/` |
| Issued Books | POST | `/api/issuedbooks/` |
| Issued Book Detail | GET | `/api/issuedbooks/{id}/` |
| Issued Book Detail | PUT | `/api/issuedbooks/{id}/` |
| Issued Book Detail | PATCH | `/api/issuedbooks/{id}/` |
| Issued Book Detail | DELETE | `/api/issuedbooks/{id}/` |
| Return Book | POST | `/api/issuedbooks/{id}/return/` |

## 🔍 Search, Filtering, Sorting & Pagination

### Books

- Search books by title, ISBN, or author name
- Filter books by category and author
- Sort books using supported ordering fields
- Retrieve paginated results

Example requests:

- `/api/books/?search=Python`
- `/api/books/?category=Programming`
- `/api/books/?author=1`
- `/api/books/?ordering=title`
- `/api/books/?page=2`

### Members

- Search members using supported search fields
- Filter members by active status
- Sort members using supported ordering fields
- Retrieve paginated results

Example requests:

- `/api/members/?search=Rahul`
- `/api/members/?is_active=true`
- `/api/members/?ordering=name`
- `/api/members/?page=2`

## 📁 Project Structure


LibraryManagementSystem/
│
├── authors/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── books/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── pagination.py
│   └── urls.py
│
├── members/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── pagination.py
│   └── urls.py
│
├── issuedbooks/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── LibraryManagementSystem/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── .env
├── .gitignore
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md


## ⚙️ How to Run the Project

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install the required dependencies:

   `pip install -r requirements.txt`

4. Apply database migrations:

   `python manage.py migrate`

5. Start the development server:

   `python manage.py runserver`

6. Open the API endpoints in your browser or test them using Postman.

## 🧪 API Testing

The API can be tested using Django REST Framework's Browsable API and Postman.

The following functionalities can be tested:

- CRUD operations for authors, books, members, and issued books
- Input validation
- Search, filtering, sorting, and pagination
- Book issuing and returning
- Book availability management
- Borrowing record management
- Error handling and HTTP status codes

## About

Library Management System API built with Django REST Framework, featuring CRUD operations, validation, book availability tracking, book issuing and returning, search, filtering, sorting, and pagination.

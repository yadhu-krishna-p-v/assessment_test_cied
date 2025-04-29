# **MEDICAL SHOP BILLING APP**

This is a RESTful API built with Django and Django REST Framework. It includes features like stock tracking, sales reporting, and Swagger documentation using `drf-yasg`.

## Installation


1. Clone the repository:

```bash
git clone https://github.com/yadhu-krishna-p-v/assessment_test_cied.git
git checkout master
cd cied_project
```

2. Create and activate a virtual environment:

   ```
   bash
   python -m venv env
   path/acivate.bat
   ```
3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```
4. Apply migrations:

   ```bash
   python manage.py migrate
   ```
5. Run server:

   ```
   bash
   python manage.py runserver
   ```


## Running the Project with Docker Compose

This project includes a `docker-compose.yml` for easy setup using Docker.

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed
- [Docker Compose](https://docs.docker.com/compose/) installed (comes with Docker Desktop)

### Steps to Run

1. Build and start the containers:
   ```bash
   docker-compose up --build
   ```

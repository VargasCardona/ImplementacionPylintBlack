# CRUD Exercise: FastAPI with Docker (Person and Cat Management)

This repository contains a simple CRUD (Create, Read, Update, Delete) exercise built using FastAPI for managing two independent entities: Person and Cat. The project is containerized using Docker for easy database setup and management, allowing seamless interaction with both entities.
Features:

## Person Management:
- Add, view, update, and delete person records.
- Attributes include name, age, gender, and email.

## Cat Management:
- Add, view, update, and delete cat records.
- Attributes include name, breed, age, and color.

## Independence:
Person and Cat are two separate, unrelated classes.

## Technologies Used:
- FastAPI: For building RESTful APIs.
- Docker: To manage the database container.
- [Database]: Managed through Docker, used for persistent data storage.

## How to Run:

- Clone the repository.
- Use Docker to set up the database by running: `docker-compose up`

## Install dependencies:

`pip install -r requirements.txt`

Start the FastAPI application: `uvicorn main:app --reload`

Access the API at `http://localhost:8000/docs` to interact with the CRUD operations.

## Contributors
- Nicolás Vargas Cardona
- Mateo Loaiza García

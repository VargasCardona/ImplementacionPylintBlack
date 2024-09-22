![logo](https://github.com/user-attachments/assets/6a948440-925d-4334-8e17-7cf2351d4108)
# CRUD Exercise: FastAPI with Docker (Class management)

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
- Build and start the Docker containers by running: `docker-compose up --build`

Access the API at `http://localhost:8000/docs` to interact with the CRUD operations.
The ApiKey is: 4d631589-409c-4c7f-8729-c21064c4f242

Access the Adminer at `http://localhost:8080` to interact with the data base.

## Contributors
- Nicolás Vargas Cardona
- Mateo Loaiza García

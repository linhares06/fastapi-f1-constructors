# F1 constructors API Project
This project is a Python-based RESTful API with FastAPI that provides information about Formula 1 constructors.
It uses FastAPI and pymongo for integration with a noSQL database(MongoDB).

## Running 
1. Clone repository.
2. pip install requirements.txt
3. Import formulaone.constructors.json with database name: formulaone and collection name constructors
4. Start server by running python main.py

## API Documentation
Swagger UI documentation at [http://localhost:8000/docs/](http://localhost:8000/docs/) to interactively explore and test the API endpoints.

## Endpoints
- **GET /api/v1/constructors/:** Retrieve a list of all F1 constructors.
- **POST /api/v1/constructors/:** Add a new F1 constructor to the database.
- **GET /api/v1/constructors/{constructor_id}:** Get details of a specific F1 constructor.
- **PUT /api/v1/constructors/{constructor_id}:** Update details of a specific F1 constructor.
- **DELETE /api/v1/constructors/{constructor_id}:** Delete a specific F1 constructor.

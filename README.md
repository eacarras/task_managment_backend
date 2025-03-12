# Task Managment API

I write this API for handle a small UI that needs to handle states in a board of tasks

I decide to use the following libraries:

fastapi: Framework para construir APIs.
uvicorn: Servidor ASGI para ejecutar FastAPI.
pymongo: Cliente oficial de MongoDB.
motor: Cliente asincrónico para MongoDB.
boto3: SDK de AWS para Python (para interactuar con Lambda y API Gateway).
pydantic: Validación de datos y modelos.
python-dotenv: Manejo de variables de entorno.
pytest: Framework de testing.

python-jose[cryptography]: Para manejar tokens JWT.
passlib[bcrypt]: Para encriptar contraseñas de usuarios.
fastapi-users: Facilita la implementación de autenticación con JWT.

For DB I decided to use MongoDB as is simple to configure and hanlde in a free trial

## Run the app locally

First of all fill your `.env` with the data put it in the .env.example

The just run the following command
```
uvicorn app.main:app --reload
```

If you want to test I recommend use POSTMAN and I left a file here that you can use it to import the endpoints that we have

## Run test
For run the test we will use the next command
```
export PYTHONPATH=$(pwd) && pytest
```

## TODO && Stuff to improve
- [ ] Add more test related with auth like an endpoint needs to be auth
- [ ] Dockerize the app 
- [ ] Mock responses and calls in the tests
- [ ] Create documentation
- [ ] Deploy to lambdas as serverless
- [ ] Improve and clean more the code adding the best practices and focus on functional programming

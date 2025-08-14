# Minimal REST API Microservice

This repository contains a simple minimal REST microservice boilerplate written in python using Flask. 
It is meant to be a boilerplate/template to clone and quickly start a scalable microservice application.

Project Organization
------------

    |
    ├── /account-microservice
    │   ├── /api       
    |   |   ├── __init__.py                         <- Python init file
    |   |   └── accounts.py                         <- Python file where methods are injected in the API
    │   ├── /providers       
    |   |   └── MongoProvider.py                    <- Python file where methods are implemented
    │   ├── /swagger       
    |   |   └── accounts-service-docs.yaml          <- API Swagger file
    │   ├── app.py                                  <- Main python file to run the app
    │   ├── Dockerfile                              <- Dockerfile used to build the image of the microservice
    │   └── requirements.txt                        <- Requirements file with the list of the libraries needed
    │
    ├── /img                                        <- Folder containing the images for this README file
    ├── LICENSE                                     <- License file
    ├── README.md                                   <- This Readme file
    └── docker-compose.yml                          <- Docker compose file, used to run the microservice
     



|Method|URI|Description|
|------|---|-----------|
| GET | /accounts/{user_id} | Retrieve data from the DB given an id |
| POST | /accounts/createUser | Insert data into the DB (Any JSON file, id mandatory)|
| PUT | /accounts/updateUser | Update data in the DB |
| DELETE | /accounts/{user_id} | Delete data from the DB | 

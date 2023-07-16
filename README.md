# fastapi-client-server-app

Dockerized fastapi client-server application (no db yet)

## Description
This service is designed to receive a request with a cadastral number, latitude and longitude. It emulates sending the request to an external server. Once processed, it returns the result of the request. The external server is expected to respond with either "true" or "false".
Both client and server sides are deployed in the separate Docker containers.


## Endpoints

The service provides the following endpoints:

#### /query

This endpoint is used to submit a request. It accepts a POST request with the following parameters:

- **number (string)**: the cadastral number associated with the request;
- **latitude (string)**: the latitude value for the request;
- **longitude (string)**: the longitude value for the request.

```
POST /query
Content-Type: application/x-www-form-urlencoded

number=1234567890&latitude=40.7128&longitude=-74.0060
```

#### /result
This endpoint is used to send the previously processed request data to the emulated server. It accepts a POST request and returns the result of the request as a JSON object. The result can be either "true" or "false".
At this moment this endpoint is being used within the service, after the conversion of the *query* data into the dictionary.
Separate usage:

```
POST /result
Content-Type: application/json

{
  "number": "1234567890",
  "latitude": "40.7128",
  "longitude": "-74.0060"
}
```

#### /ping
This endpoint is used to check if the server is running. It accepts a GET request and returns a simple "pong" response.

Example Response:

```
GET /ping

"pong"
```

### To run the project, follow these steps:

1. Clone the project from the GitHub repository. You can use the ```git clone``` command and provide the repository URL.

2. Navigate to the project directory using the ```cd``` command.

3. Make sure you have Docker and Docker Compose installed on your machine. If not, follow the instructions to install [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/).

Run the command ```docker-compose up --build``` to start the project. This command will build the Docker containers and launch them.

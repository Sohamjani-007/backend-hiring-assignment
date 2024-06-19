# TASK-MANAGEMENT-SYSTEM

##  Testing in Local on Postman (CURL COMMAND GIVEN BELOW TO DIRECTLY COPY PASTE IN POSTMAN):::
### NOTE : Project is running on ::: python manage.py runserver 8010

POST API - Create a new project
```commandline
curl --location 'http://127.0.0.1:8010/api/projects/' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Pixel Project 2",
    "description": "Pixel Description 2",
    "client": "PixelDust2",
    "end_date": "2024-06-18"
}'
```
GET --> Fetch all projects (with pagination)
```commandline
curl --location 'http://127.0.0.1:8010/api/projects/' \
--header 'Accept: application/json'

```
GET --> View a project (including tasks for the project)
```commandline
curl --location 'http://127.0.0.1:8010/api/projects/3/' \
--header 'Accept: application/json'
```
DELETE --> Delete a project
```commandline
curl --location --request DELETE 'http://127.0.0.1:8010/api/projects/1/'
```
POST --> Create a new task.
```commandline
curl --location 'http://127.0.0.1:8010/api/tasks/' \
--header 'Content-Type: application/json' \
--data '{
    "name": "First Task",
    "description": "Task Description",
    "project": 2,
    "status": "To Do"
}'
```
PUT --> Edit the status of a task
```commandline
curl --location --request PUT 'http://127.0.0.1:8010/api/tasks/1/' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Updated Task",
    "description": "Updated Description",
    "project": 2,
    "status": "Done"
}'
```
GET --> View a task
```commandline
curl --location 'http://127.0.0.1:8010/api/tasks/1/' \
--header 'Accept: application/json'
```
GET --> Fetch all tasks (with pagination)
```commandline
curl --location 'http://127.0.0.1:8010/api/tasks/' \
--header 'Accept: application/json'
```
DELETE --> Delete a task
```commandline
curl -X DELETE "http://127.0.0.1:8010/api/tasks/1/"
```

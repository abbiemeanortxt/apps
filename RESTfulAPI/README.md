# RESTful API example in Flask
This example demonstrates how to create a simple RESTful API using the Flask framework in Python.

## Installing dependencies
To run this example, make sure you have the Flask framework installed.  
If it is not there, install it using the following command:
```bash
pip install Flask
```

## Launching the application
Open a terminal and go to the directory containing the `app.py` file.

Launch the application using the following command:
```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000/`.

## API Resources
### Getting a list of tasks
```bash
curl http://127.0.0.1:5000/tasks
```
### Getting a task by ID (replace <task_id> with the actual ID)
```bash
curl http://127.0.0.1:5000/tasks/<task_id>
```
### Create a new task
```bash
curl -X POST -H "Content-Type: application/json" -d '{"title":"New Task"}' http://127.0.0.1:5000/tasks
```

## Project structure
`app.py`: The main application file describing the endpoints and API functionality.  
`README.md`: This file contains project information and instructions.

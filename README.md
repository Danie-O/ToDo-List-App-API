# ToDo-List-App-API

This is a RESTful API for a to-do list app, with CRUD, authentication and filtering functionalities.

The todo-list database consists of two Models(tables):

## Users

This contains information about registered users, and has the following fields:
    - id
    - name
    - email
    - password

## Tasks

This contains the details about tasks that been added to the TODO list. It consists of the following fields:
    - id
    - title
    - description
    - status
    - due_date

### Set environment variables

- Enviroment
- JWT Token
- SQLAlchemy database URI

To enable migrations, run:

- First set the FLASK_APP environment variable to the app runner by running the following command:

```shell
SET FLASK_APP=./run.py:create_app('development')
```

- Create database migration repository: Run the command below to add a migrations directory in the root of your project.
  
```shell
flask db init
```

Then, add the 'migrations' directory that would be created, and all of its contents to source control. ( git add .)

- Create initial migration
  
```shell
flask db migrate
```

- After making any changes to database schemas, run the following command to update the database.
  
```shell
flask db upgrade
```

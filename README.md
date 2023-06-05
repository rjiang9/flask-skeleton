# flaskskeleton

# From Flask-Complete-Tutorial

https://dev.to/nagatodev/adding-authentication-to-a-flask-application-53ep

This is the completed and styled Todolist application built in the Flask Tutorial. See the tutorial for instructions on how to build this.

## Code Usage
- Clone the repository
- Create your environment 
 ```shell
       python3 -m venv env
 ```
 - Activate your environment 
 ```shell
       source env/bin/activate
 ```
 - Install all requirements
 ```shell
       pip install -r requirements.txt
 ```
 - Run the following command to run the code in development mode
 
 If there are mgirations/todo.db alreaady, remove them!!!
``` re-create db
    rm -r migrations
    rm todo.db
```

then: 


```shell
    flask db init
    flask db migrate
    flask db upgrade
    flask run
 ```
If have like flask does have db command error, run
```
flaks --help
``` 
to see whether 'db' on the command list. If not, 
run:

```shell
    flask --app Todolist db init
    flask --app Todolist db migrate
    flask --app Todolist db upgrade
    flask --app Todolist run
 ```



 
 - Enjoy!!!!

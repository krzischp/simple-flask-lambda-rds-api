# simple-flask-lambda-rds-api
Simple flask lambda rds api

Clone this repo to your local machine. In the top level directory, create a virtual environment:
```
virtualenv venv
.\venv\Scripts\activate
```
Now install the required modules:
```
.\venv\Scripts\python.exe -m pip install --upgrade pip setuptools
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```


To play with the app right away, you can use a local database. Edit ```config.py``` by commenting out the AWS URL and uncomment this line:
```
SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
```

Run migrations initialization, using the db init command as follows:
```
python migrate.py db init
```

Run the second script that populates the migration script with the detected changes in the models. 
In this case, it is the first time we populate the migration script, and therefore, the
migration script will generate the tables that will persist our model: **Data**:
```
python migrate.py db migrate 
```


Then apply the migration to the database. Run the upgrade command:
```
python migrate.py db upgrade
```

And the tables are created.  Now you can launch the app:
```
python app.py
```
And point your browser to http://0.0.0.0:5000

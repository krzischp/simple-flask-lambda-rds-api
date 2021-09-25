# simple-flask-lambda-rds-api
Simple flask lambda rds api

Clone this repo to your local machine. In the top level directory, create a virtual environment:
```
virtualenv venv
```
Activate it:
```
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
Create folder `migration` with `alembic.ini` file to edit before proceeding.  

Run the second script that populates the migration script with the detected changes in the models. 
In this case, it is the first time we populate the migration script, and therefore, the
migration script will generate the tables that will persist our model **Data**:
```
python migrate.py db migrate 
```

First generated log:
```
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'Data'
INFO  [alembic.autogenerate.compare] Detected added index 'ix_Data_notes' on '['notes']'
Generating C:\Users\Utilisateur\Pierre\Interviews\mercado_livre\simple-flask-lambda-rds-api\migrations\versions\8cbe97fbecd0_.py ...  done
```


Then apply the migration to the database. Run the upgrade command:
```
python migrate.py db upgrade
```

First generated log:
```
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 8cbe97fbecd0, empty message
```

And the tables are created.  Now you can launch the app:
```
python app.py
```
And point your browser to the link being displayed.

# AWS

## Zappa
Step by step:  
https://www.viget.com/articles/building-a-simple-api-with-amazon-lambda-and-zappa/

Allows users to deploy code to **Lambda** with minimal configuration with just one command from the CLI.

You can deploy your Zappa application by executing:
```
zappa deploy dev
```

After that, you can update your application code with:
```
zappa update dev
```

Your updated Zappa deployment is live!:  
https://rqefqjt8l4.execute-api.sa-east-1.amazonaws.com/dev


Check deployment logs:
```
zappa tail
```

Remove deployed resources
```
zappa undeploy dev
```

**Fix**  
venv/Lib/site-packages/zappa/core.py at line 2137  
change `add_description` by `set_description`
## RDS
Public Access: No
RDS will not assign a public IP address to the database. Only Amazon EC2 instances and devices inside the VPC can connect to your database.

https://sa-east-1.console.aws.amazon.com/rds/home?region=sa-east-1#databases:

You first need to create testdb database in your AWS RDS test-db instance.
```
CREATE DATABASE testdb;
```
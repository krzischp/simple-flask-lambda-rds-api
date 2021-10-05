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
https://**********.execute-api.sa-east-1.amazonaws.com/dev


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

# Requirements
- **SQLAlchemy** is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL
    - translates Python classes to tables on relational databases and automatically converts function calls to SQL statements.
    
- **Flask** is an API of Python that allows us to build up web-applications.
- **Flask-RESTful** is an extension for Flask that adds support for quickly building REST APIs
- **Flask-SQLAlchemy** is an extension for Flask that adds support for SQLAlchemy to your application
    - It aims to simplify using SQLAlchemy with Flask by providing useful defaults and extra helpers that make it easier to accomplish common tasks.
    
- **Flask-Migrate** is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic
- **Alembic** is a lightweight database migration tool for usage with the SQLAlchemy Database Toolkit for Python
    - Version control in database: Version Control protects production systems from uncontrolled change. The VCS acts as a guard against 'uncontrolled' database changes i.e. against direct changes to the code, structure, or configuration of a production database.
- **boto3**: You use the AWS SDK for Python (Boto3) to create, configure, and manage AWS services, such as Amazon Elastic Compute Cloud (Amazon EC2) and Amazon Simple Storage Service (Amazon S3). The SDK provides an object-oriented API as well as low-level access to AWS services.
- **botocore**: Boto3 is built atop of a library called Botocore, which is shared by the AWS CLI. Botocore provides the low level clients, session, and credential & configuration data.
- **marshmallow** is an ORM/ODM/framework-agnostic library for converting complex datatypes, such as objects, to and from native Python datatypes.  
  
**Ex** of object conversion to python dict native Python datatype:
  
```
from datetime import date
from pprint import pprint

from marshmallow import Schema, fields


class ArtistSchema(Schema):
    name = fields.Str()


class AlbumSchema(Schema):
    title = fields.Str()
    release_date = fields.Date()
    artist = fields.Nested(ArtistSchema())


bowie = dict(name="David Bowie")
album = dict(artist=bowie, title="Hunky Dory", release_date=date(1971, 12, 17))

schema = AlbumSchema()
result = schema.dump(album)
pprint(result, indent=2)
# { 'artist': {'name': 'David Bowie'},
#   'release_date': '1971-12-17',
#   'title': 'Hunky Dory'}
```

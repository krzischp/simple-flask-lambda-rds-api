import os

# You need to replace the next values with the appropriate values for your configuration

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
# SQLALCHEMY_DATABASE_URI = "mysql+pymysql://krzischp:Bernard1994@symphonymysql.cn5orfrkeinp.sa-east-1.rds.amazonaws.com/symphony"

# Uncomment the line below if you want to work with a local DB
SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

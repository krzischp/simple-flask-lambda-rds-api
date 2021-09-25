from run import api_bp
from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from model import db

# from run import create_app

# app = create_app('config')
app = Flask(__name__)

config_filename = "config"
app.config.from_object(config_filename)

app.register_blueprint(api_bp, url_prefix='/api')

db.init_app(app)


migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()

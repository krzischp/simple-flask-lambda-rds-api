from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from model import db
from flask import Flask

# from run import create_app

# app = create_app('config')
app = Flask(__name__)

config_filename = "config"
app.config.from_object(config_filename)

from app import api_bp
app.register_blueprint(api_bp, url_prefix='/api')

db.init_app(app)



migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
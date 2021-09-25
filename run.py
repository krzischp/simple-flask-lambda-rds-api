from model import db
from routes import api_bp
from flask import Flask
from flask_cors import CORS

# def create_app(config_filename):
app = Flask(__name__)
CORS(app)

config_filename = "config"
app.config.from_object(config_filename)

app.register_blueprint(api_bp, url_prefix='/api')

db.init_app(app)
# return app


if __name__ == "__main__":
    # app = create_app("config")
    app.run(debug=True)

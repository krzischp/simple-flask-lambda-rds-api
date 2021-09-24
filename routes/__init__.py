from flask import Blueprint
from flask_restful import Api

from resources.Data import DataResource

# api_bp = Blueprint('api', __name__) - creates a Blueprint which we'll register to the app later.
# api.add_resource(Hello, '/Hello') - creates a route - /Hello. add_resource accepts two parameter
# - Hello and /Hello, where Hello is the class we have imported and /Hello is the route we defined for that Resource.

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(DataResource, '/Data')

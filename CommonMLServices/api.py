# CommonMLServices entry point
# Import framework
from flask import Flask
from flask_restful import Resource, Api

# Instantiate the app
app = Flask(__name__)
api = Api(app)

class CommonMLServices(Resource):
    def get(self):
        return {
            'Shivam': ['2.3', '100', 
            '5']
        }

# Create routes
api.add_resource(CommonMLServices, '/')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

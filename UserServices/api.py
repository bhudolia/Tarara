# Usersevices entry point
# Import framework
from flask import Flask
from flask_restful import Resource, Api

# Instantiate the app
app = Flask(__name__)
api = Api(app)

class UserServices(Resource):
    def get(self):
        return {
            'Shivam': ['Guitarist', 'Chennai', 
            'Hindi,English,Tamil']
        }

# Create routes
api.add_resource(UserServices, '/')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

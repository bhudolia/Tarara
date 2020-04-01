# Vendorsevices entry point
# Import framework
from flask import Flask
from flask_restful import Resource, Api

# Instantiate the app
app = Flask(__name__)
api = Api(app)

class VendorServices(Resource):
    def get(self):
        return {
            'Local': ['Delhi', 'CP', 
            'Bar']
        }

# Create routes
api.add_resource(VendorServices, '/')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

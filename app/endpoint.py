from flask import Flask
from modules import rnmapi
from flask_restful import Api
app = Flask(__name__)
api = Api(app)

api.add_resource(rnmapi.Index,'/')
api.add_resource(rnmapi.GetCharacters,'/characters')
api.add_resource(rnmapi.HealthCheck, '/healthchack')
# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
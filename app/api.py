from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        response = app.make_response({'greetings': 'worldling'})
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        return response

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request
from flask_restful import Resource, Api
from skills import Skills
import json


app = Flask(__name__)
api = Api(app)

devs = [
    {   'id': '0',
        'name': 'Aragon',
        'skills': ['Python', 'Flask']
    },
    {   'id': '1',
        'name': 'Bilbo',
        'skills': ['Django', 'Docker']}
]

class Developer(Resource):
    def get(self, id):
        try:
            res = devs[id]
        except IndexError:
            message = "ID Developer {} not found".format(id)
            res = {"status": "error", "message": message}
        except Exception:
            message = "Unknow error, Find the administrator of API"
            res = {"status": "error", "message": message}
        return res



    def put(self, id):
        data = json.loads(request.data)
        devs[id] = data
        return data

    def delete(self, id):
        devs.pop(id)
        return {'status': 'success', 'message': 'Info deleted'}

class ListDevs(Resource):
    def get(self):
        return devs

    def post(self):
        data = json.loads(request.data)
        position = len(devs)
        data['id'] = position
        devs.append(data)
        return(devs[position]) 


api.add_resource(Developer, '/dev/<int:id>')
api.add_resource(ListDevs, '/dev/')
api.add_resource(Skills, '/skills/')




if __name__ == '__main__':
    app.run(debug=True)
    
from logging import debug
from flask import Flask, jsonify
from flask.globals import request
import json

app = Flask(__name__)

devs = [
    {   'id': '0',
        'name': 'Jose',
        'skills': ['Python', 'Flask']
    },
    {   'id': '1',
        'name': 'Bruce',
        'skills': ['Django', 'Java']}
]

#devolve, deleta e altera um desenvolvedor pelo id
@app.route('/dev/<int:id>/', methods=["GET", "PUT", "DELETE"])
def dev(id):
    if request.method == "GET":
        try:
            res = devs[id]
        except IndexError:
            message = "ID Developer {} not found".format(id)
            res = {"status": "error", "message": message}
        except Exception:
            message = "Unknow error, Find the administrator of API"
            res = {"status": "error", "message": message}
        return jsonify(res)
    elif request.method == "PUT":
        data = json.loads(request.data)
        devs[id] = data
        return jsonify(data)
    elif request.method == "DELETE":
        devs.pop(id)
        return jsonify({"status": "success", "message": "Info deleted"})

    #lista todos os desenvolvedores e permite registrar um novo
@app.route('/dev/', methods=["POST", "GET"])
def list_devs():
    if request.method == "POST":
        data = json.loads(request.data)
        position = len(devs)
        data['id'] = position
        devs.append(data)
        return jsonify(devs[position]) 
    elif request.method == "GET":
        return jsonify(devs)

if __name__ == '__main__':
    app.run(debug=True)
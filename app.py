from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from pymongo import MongoCLient
import json
from bson.objectid import ObjectId

app = Flask(__name__)

CORS(app, origins=["*"])

# client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://<sinis_gay>:<gato>@<34.42.241.216>:5000/')

db = client['Documentos']
mycol = db['docs']


@app.route('/documents', methods=['GET'])
def get():
    data = mycol.find({})
    a = []
    for d in data:
        b = {
            "id": str(d["_d"]),
        }
        a.append(b)
    return {'message': a}


@app.route('/documents', methods=['POST'])
def add_user():
    data = request.get_json()
    print(data)
    if data:
        d = mycol.insert_one(data)
        print(d)
        response = jsonify(
            {'message': "Documento agregado de forma exitosa", "id": str(d.inserted_id)})
    else:
        response = Response("Que sapo", status=400,
                            minetype='application/json')
    return Response


if __name__ == "__main__":

    app.run(host='0.0.0.0', port=8080, debug=True)

import pandas as pd
import numpy as np
from utils.get_consensus_similarity import get_consensus_similarity
from sprints.sprint_3 import sprint_3
from flask import Flask, json, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

data = pd.read_csv("./data/pizzas.csv")

@app.route("/", methods=["GET"])
def index():
    return json.dumps([
        {   
            "name": "Sprint #2",
            "endPoint DUMMY": "http://127.0.0.1:5000/sprint-2?nodeA=Natalia Betancourt&nodeB=Isabella Gallego",
            "description": "Provides the similarity between 2 given nodes"
        },
        {   
            "name": "Nodes",
            "endPoint DUMMY": "http://127.0.0.1:5000/nodes",
            "description": "Provides all the nodes from the database"
        },
    ])

@app.route("/nodes", methods=["GET"])
def get_nodes():
    nodes = [data.loc[x[0]].to_dict() for x in data.iterrows()]
    return json.dumps(nodes)

@app.route("/sprint-2", methods=["GET"])
def sprint_2_endpoint():
    args = request.args.to_dict()
    # print("args->", args.to_dict())
    row_frame_A = data[data["Nombre"] == args["nodeA"]]
    row_frame_B = data[data["Nombre"] == args["nodeB"]]
    similarity = get_consensus_similarity(row_frame_A, row_frame_B)
    return json.dumps({
        "nodeA": args["nodeA"],
        "nodeB": args["nodeB"],
        "similarity": similarity,
    })

    # print(similarity)
    # return json.dumps(sprint_3(row_frame_A, data, 4))


if __name__ == "__main__":
    app.run(debug=True)
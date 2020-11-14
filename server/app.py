from flask import Flask, jsonify, request
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# create simple array
todo_list = ["Item 1", "Item 2"]

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/todolist', methods=['GET'])
def get_todo_list():
    return jsonify(todo_list)

@app.route('/todolist', methods=['POST'])
def save_todo_list():
    item = request.json['item']
    todo_list.append(item)
    return jsonify(todo_list)

if __name__ == '__main__':
    app.run()
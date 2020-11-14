# https://gist.github.com/miguelgrinberg/5614326
from flask import Flask, request, url_for
from flask_cors import CORS
from ResponseHandler import ResponseHandler

# configuration
DEBUG = True
ROOT_PATH = "/todo/api/v1"

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# create dictionary list
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

# Routes
@app.route(f'{ROOT_PATH}/tasks', methods=['GET'])
def get_tasks():
    return ResponseHandler(tasks).toJSON()

@app.route(f'{ROOT_PATH}/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = list(filter(lambda t: t['id'] == task_id, tasks))
    if len(task) == 0:
        return ResponseHandler(errorMessage = "Record not found").toJSON()
    return ResponseHandler(payload=task[0]).toJSON()

@app.route(f'{ROOT_PATH}/tasks', methods=['POST'])
def save_task():
    if not request.json:
        return ResponseHandler(errorMessage = "Title cannot be empty").toJSON()
    if not request.json or not 'title' in request.json or not request.json['title']:
        return ResponseHandler(errorMessage = "Title cannot be empty").toJSON()
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': request.json.get('done', False)
    }
    tasks.append(task)
    return ResponseHandler(task).toJSON()

if __name__ == '__main__':
    app.run()
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample database (instead of a real database)
tasks = [
     {
         'id': 1,
         'title': 'Task 1',
         'done': False
     },
     {
         'id': 2,
         'title': 'Task 2',
         'done': False
     }
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
     return jsonify({'tasks': tasks})

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
     task = next((task for task in tasks if task['id'] == task_id), None)
     if task is None:
         return jsonify({'error': 'Task not found'}), 404
     return jsonify({'task': task})

@app.route('/tasks', methods=['POST'])
def create_task():
     if not request.json or 'title' not in request.json:
         return jsonify({'error': 'Task title is required'}), 400
     task = {
         'id': len(tasks) + 1,
         'title': request.json['title'],
         'done': False
     }
     tasks.append(task)
     return jsonify({'task': task}), 201

if __name__ == '__main__':
     app.run(debug=True)

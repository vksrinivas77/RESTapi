from flask import Flask, request, jsonify, render_template
from db_config import get_db_connection

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tasks', methods=['GET'])
def get_tasks():
    connection = get_db_connection()
    if connection is None:
        return jsonify({'error': 'Database connection failed'}), 500

    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM todos")
    tasks = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    task = request.json.get('task')
    if not task:
        return jsonify({'error': 'No task provided'}), 400

    connection = get_db_connection()
    if connection is None:
        return jsonify({'error': 'Database connection failed'}), 500

    cursor = connection.cursor()
    cursor.execute("INSERT INTO todos (task) VALUES (%s)", (task,))
    connection.commit()
    task_id = cursor.lastrowid
    cursor.close()
    connection.close()
    return jsonify({'id': task_id, 'task': task, 'status': 'pending'}), 201

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = request.json.get('task')
    if not task:
        return jsonify({'error': 'No task provided'}), 400

    connection = get_db_connection()
    if connection is None:
        return jsonify({'error': 'Database connection failed'}), 500

    cursor = connection.cursor()
    cursor.execute("UPDATE todos SET task = %s WHERE id = %s", (task, id))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({'id': id, 'task': task})

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    connection = get_db_connection()
    if connection is None:
        return jsonify({'error': 'Database connection failed'}), 500

    cursor = connection.cursor()
    cursor.execute("DELETE FROM todos WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]


@app.route('/')
def home():
    return 'Hello api'

@app.route('/todos', methods=['GET', 'POST'])
def todosfn():
    if request.method == 'GET':
        print(type(todos))
        return jsonify(todos)
    elif request.method == 'POST':
        request_body = request.json
        print(request_body)
        updated_list = todos + [request_body]
        print(updated_list)
        return jsonify(updated_list)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete(position):
    if request.method == 'DELETE':
        del todos[position]
        print(jsonify(todos))
        return jsonify(todos)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database (list)
items = []

# Create (POST)
@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.json
    items.append(new_item)
    return jsonify(new_item), 201

# Read (GET)
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items), 200

# Update (PUT)
@app.route('/items/<int:index>', methods=['PUT'])
def update_item(index):
    if index < len(items):
        items[index] = request.json
        return jsonify(items[index]), 200
    return jsonify({"error": "Item not found"}), 404

# Delete (DELETE)
@app.route('/items/<int:index>', methods=['DELETE'])
def delete_item(index):
    if index < len(items):
        deleted_item = items.pop(index)
        return jsonify(deleted_item), 200
    return jsonify({"error": "Item not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

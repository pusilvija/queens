from flask import Blueprint, jsonify, request, Flask
from flask_cors import CORS

from grid import Grid

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

grid = None


def get_coordinates_from_request(request):
    """Helper function to extract x and y from the request."""
    data = request.get_json()
    if not data:
        return None, None, "Invalid request: No JSON body found."
    
    x = data.get('x')
    y = data.get('y')

    if x is None or y is None:
        return None, None, "Missing x or y in the request."

    try:
        x = int(x)
        y = int(y)
    except ValueError:
        return None, None, "x and y must be integers."

    return x, y, None


@app.route('/put-queen', methods=['POST'])
def put_queen():
    x, y, error = get_coordinates_from_request(request)
    if error:
        return jsonify(message=error), 400

    message = grid.put_queen(x, y)
    grid.print_grid()
    return jsonify(message=message), 200


@app.route('/remove-queen', methods=['POST'])
def remove_queen():
    x, y, error = get_coordinates_from_request(request)
    if error:
        return jsonify(message=error), 400

    message = grid.remove_queen(x, y)
    return jsonify(message=message), 200

@app.route('/reset-grid', methods=['POST'])
def reset_grid():
    message = grid.reset_queens()
    return jsonify(message=message), 200

@app.route('/create-grid', methods=['GET'])
def create_grid():
    size = request.args.get('size', default=8, type=int)
    global grid
    grid = Grid(size)
    grid.print_grid()
    jsonify(message=f"Grid generated with size of {size}"), 200

if __name__ == '__main__':
    app.run(host='localhost', port=5174)

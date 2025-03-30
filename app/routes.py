from flask import Blueprint, jsonify, request, Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/queen', methods=['POST'])
def put_queen():
    x = request.args.get('x')
    y = request.args.get('y')
    
    return jsonify(message="")


if __name__ == '__main__':
    app.run()

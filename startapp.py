import logging
from flask import Flask, jsonify, request

from manager.app_manager import Manager
from manager.static import REDIRECT_TO_ADD_DATA_URL

data = []

app = Flask(__name__)


@app.route('/add_data', methods=['POST'])
def add_data():
    req = request.get_json()
    data.append({'data': Manager.reverse_line_by_fibonacci_id(req['strings_list'])})
    return {'info': Manager.reverse_line_by_fibonacci_id(req['strings_list'])}


@app.route('/get_data', methods=['GET'])
def get_added_data():
    logging.warning(f"Users data: {data}")
    return {'data': data,
            'p.s': f'{REDIRECT_TO_ADD_DATA_URL}'}


if __name__ == '__main__':
    app.run(debug=True, port=8080)

# project/api/main.py


from flask import Blueprint, jsonify


main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/ping', methods=['GET'])
def ping():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })

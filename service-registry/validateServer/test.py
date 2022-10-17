from flask import Flask, Blueprint, jsonify

sr_test = Blueprint('sr_test', '__name__', url_prefix='/test-server')

@sr_test.route('', methods=['GET'])
def test_server():
    return "SERVICE OK"
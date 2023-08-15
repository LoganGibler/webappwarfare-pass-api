from flask import Flask, jsonify, make_response
from flask_cors import CORS, cross_origin
from importlib import reload
from flask import request
import string
import random
import json
import re

from hashlib import md5, sha1, sha224, sha256, sha384, sha512

server = Flask(__name__)
cors = CORS(server)
server.config['CORS_HEADERS'] = 'Content-Type'


@server.route("/hash_pass", methods=['GET', 'POST'])
@cross_origin()
def hash_pass():
    data = request.get_json(force=True)
    print("This is main request to sent to flask api:", data)
    password = data['password']
    print("This is password: " + password)

    hashed_password = md5(password.encode())

    return {"hashed_pass": hashed_password.hexdigest()}


if __name__ == "__main__":
    server.run(host='0.0.0.0', port=5000, debug=True)

from flask import Flask, jsonify

server = Flask(__name__)


def get_relays(relays):
    return jsonify({"relays": relays}), 200


def get_relay(relays, relay_name):
    code = 200
    try:
        relay = relays[relay_name]
    except KeyError:
        code = 404
        return "", code

    return jsonify({"relay": relay}), code

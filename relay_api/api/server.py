from flask import Flask, jsonify, abort

server = Flask(__name__)


def get_relays(relays):
    return jsonify({"relays": relays})


def get_relay(relays, relay_id):
    relay = [relay for relay in relays if relay["id"] == relay_id]
    if len(relay) == 0:
        abort(404)
    return jsonify({"relay": relay[0]})

from flask import Flask, jsonify
# import json

server = Flask(__name__)


def __serialize_relay(relays):
    if type(relays).__name__ == "relay":
        return jsonify({"gpio": relays.gpio,
                           "NC": relays.nc,
                           "state": relays.state})
    di = {}
    for r in relays:
        di[r] = {"gpio": relays[r].gpio,
                 "NC": relays[r].nc,
                 "state": relays[r].state}
    return jsonify(di)


def get_relays(relays_dict):
    return __serialize_relay(relays_dict), 200


def get_relay(relay):
    code = 200
    if not relay:
        code = 404
        return "", code
    return __serialize_relay(relay), code

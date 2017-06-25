from flask import Flask, request
import relay_api.api.backend as backend


server = Flask(__name__)

backend.init_relays()


@server.route("/relay-api/relays/", methods=["GET"])
def get_all_relays():
    js = backend.get_all_relays()
    return js, 200


@server.route("/relay-api/relays/<relay_name>", methods=["GET"])
def get_relay(relay_name):
    js = backend.get_relay(relay_name)
    if not js:
        return "", 404
    return js, 200


@server.route("/relay-api/relays/<relay_name>/on", methods=["PUT"])
def set_relay_on(relay_name):
    js = backend.set_relay_on(relay_name)
    if not js:
        return "", 404
    return js, 200


@server.route("/relay-api/relays/<relay_name>/off", methods=["PUT"])
def set_relay_off(relay_name):
    js = backend.set_relay_off(relay_name)
    if not js:
        return "", 404
    return js, 200


@server.route("/relay-api/relays/<relay_name>/delete", methods=["DELETE"])
def delete_relay(relay_name):
    js = backend.delete_relay(relay_name)
    if not js:
        return "", 404
    return js, 200


@server.route("/relay-api/relays/create", methods=["POST"])
def create_relay():
    new_relay = request.get_json()
    js, error = backend.create_relay(new_relay)
    if error:
        return js, 404
    return js, 200

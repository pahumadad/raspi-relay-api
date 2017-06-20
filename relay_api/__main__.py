from relay_api.api.server import server
from relay_api.core.relay import relay
from relay_api.conf.config import relays
import relay_api.api.server as api


for r in relays:
    relays[r]["instance"] = relay(relays[r]["gpio"],
                                  relays[r]["NC"])


@server.route("/relay-api/relays", methods=["GET"])
def get_relays():
    return api.get_relays(relays)


@server.route("/relay-api/relays/<relay_name>", methods=["GET"])
def get_relay(relay_name):
    return api.get_relay(relays, relay_name)

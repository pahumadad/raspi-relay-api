from relay_api.api.server import server
from relay_api.core.relay import relay
from relay_api.conf.config import relays
import relay_api.api.server as api


relays_dict = {}
for r in relays:
    relays_dict[r] = relay(relays[r]["gpio"], relays[r]["NC"])


@server.route("/relay-api/relays", methods=["GET"])
def get_relays():
    return api.get_relays(relays_dict)


@server.route("/relay-api/relays/<relay_name>", methods=["GET"])
def get_relay(relay_name):
    return api.get_relay(relays_dict.get(relay_name, "None"))

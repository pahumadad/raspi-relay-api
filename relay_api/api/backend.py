import json
import copy
from relay_api.core.relay import relay
from relay_api.conf.config import relays


def init_relays():
    for r in relays:
        relays[r]["object"] = relay(relays[r]["gpio"])
        relays[r]["state"] = relays[r]["object"].get_state()


def get_all_relays():
    relays_dict = __get_relay_dict()
    return json.dumps(relays_dict, indent=4)


def get_relay(relay_name):
    if relay_name not in relays:
        return None
    relay_dict = __get_relay_dict(relay_name)
    return json.dumps(relay_dict, indent=4)


def set_relay_on(relay_name):
    if relay_name not in relays:
        return None
    relays[relay_name]["object"].on()
    relays[relay_name]["state"] = relays[relay_name]["object"].get_state()
    relay_dict = __get_relay_dict(relay_name)
    return json.dumps(relay_dict, indent=4)


def set_relay_off(relay_name):
    if relay_name not in relays:
        return None
    relays[relay_name]["object"].off()
    relays[relay_name]["state"] = relays[relay_name]["object"].get_state()
    relay_dict = __get_relay_dict(relay_name)
    return json.dumps(relay_dict, indent=4)


def delete_relay(relay_name):
    if relay_name not in relays:
        return None
    relays[relay_name]["object"].cleanup()
    del(relays[relay_name])
    return json.dumps({relay_name: "deleted!"}, indent=4)


def __get_relay_dict(relay_name=None):
    if relay_name:
        relay_dict = copy.deepcopy(relays[relay_name])
        del(relay_dict["object"])
        return relay_dict
    relays_dict = copy.deepcopy(relays)
    for r in relays_dict:
        del(relays_dict[r]["object"])
    return relays_dict

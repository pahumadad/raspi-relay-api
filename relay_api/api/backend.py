import json
import copy
from relay_api.core.relay import relay
from relay_api.core.relay import MAX_RELAY_GPIO
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


def create_relay(new_relay):
    try:
        r_name = new_relay["name"]
        r_gpio = new_relay["gpio"]
        r_type = new_relay["type"]
        r_desc = new_relay["desc"]
    except Exception:
        msg = {"name": "Must be unique",
               "gpio": "Must be an int between 0 - " + str(MAX_RELAY_GPIO),
               "type": "NO or NC",
               "desc": "Relay description"}
        return json.dumps(msg, indent=4), True

    if r_name in relays:
        msg = "Relay name is already in use!"
        return json.dumps({"error": msg}, indent=4), True

    try:
        r = relay(new_relay["gpio"])
        relays[r_name] = {"gpio": r_gpio,
                          "type": r_type,
                          "desc": r_desc}
        relays[r_name]["object"] = r
    except Exception as e:
        return json.dumps({"error": str(e)}, indent=4), True

    relays[r_name]["state"] = relays[r_name]["object"].get_state()
    relay_dict = __get_relay_dict(r_name)
    return json.dumps(relay_dict, indent=4), False


def __get_relay_dict(relay_name=None):
    if relay_name:
        relay_dict = copy.deepcopy(relays[relay_name])
        del(relay_dict["object"])
        return relay_dict
    relays_dict = copy.deepcopy(relays)
    for r in relays_dict:
        del(relays_dict[r]["object"])
    return relays_dict

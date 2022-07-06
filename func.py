import json

import requests
import constants


def send_message(message, to):
    response = requests.post(url=constants.WA_ENDPOINT, headers=constants.header, data=json.dumps(
        {
            "messaging_product": "whatsapp",
            "to": to,
            "type": "text",
            "text": {
                "body": message,
            }
        }
    ))
    return response.json()


def send_selection_msg(to):
    response = requests.post(url=constants.WA_ENDPOINT, headers=constants.header, data=json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": to,
        "type": "interactive",
        "interactive": constants.interactive_msg_body
    }))
    return response.json()


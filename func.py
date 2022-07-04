import requests
import constants


def send_message(template, to):
    response = requests.post(url=constants.WA_ENDPOINT, headers=constants.header, data={
        "messaging_product": "whatsapp",
        "to": to,
        "type": "template",
        "template": {
            "name": template,
            "language": {
                "code": "en_US"
            }
        }
    })
    return response.json()


def send_selection_msg(to):
    response = requests.post(url=constants.WA_ENDPOINT, headers=constants.header, data={
        "recipient_type": "individual",
        "to": to,
        "type": "interactive",
        "interactive": constants.interactive_msg_body
    })
    return response.json()

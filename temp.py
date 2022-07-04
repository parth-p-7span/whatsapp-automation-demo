import requests
import constants
import json

response = requests.post(url=constants.WA_ENDPOINT,
                         headers=constants.header,
                         data=json.dumps({
                            "messaging_product": "whatsapp",
                            "recipient_type": "individual",
                            "to": "918780495804",
                            "type": "interactive",
                            "interactive": constants.interactive_msg_body
                            })
                         )

print(response.json())
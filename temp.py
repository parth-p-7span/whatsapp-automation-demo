import requests
import constants
import json
import func

# response = requests.post(url=constants.WA_ENDPOINT,
#                          headers=constants.header,
#                          data=json.dumps({
#                             "messaging_product": "whatsapp",
#                             "recipient_type": "individual",
#                             "to": "918780495804",
#                             "type": "interactive",
#                             "interactive": constants.interactive_msg_body
#                             })
#                          )

# print(func.send_message("hi there", "917227856454"))

#!/usr/bin/python
# -*- coding: utf-8 -*-
# a = {
#     "object": "whatsapp_business_account",
#     "entry": [
#         {
#             "id": "104861202286839",
#             "changes": [
#                 {
#                     "value": {
#                         "messaging_product": "whatsapp",
#                         "metadata": {
#                             "display_phone_number": "15550054716",
#                             "phone_number_id": "106519662119427",
#                         },
#                         "contacts": [
#                             {
#                                 "profile": {"name": "Parth Panchal"},
#                                 "wa_id": "918780495804",
#                             }
#                         ],
#                         "messages": [
#                             {
#                                 "context": {
#                                     "from": "15550054716",
#                                     "id": "wamid.HBgMOTE4NzgwNDk1ODA0FQIAERgSN0IxREZBN0QyMDhENUM1ODExAA==",
#                                 },
#                                 "from": "918780495804",
#                                 "id": "wamid.HBgMOTE4NzgwNDk1ODA0FQIAEhggRkNDRjQxRTBGREU5RUU0MDdGMURBMzZFQzRCQkJBM0IA",
#                                 "timestamp": "1657025134",
#                                 "type": "interactive",
#                                 "interactive": {
#                                     "type": "button_reply",
#                                     "button_reply": {
#                                         "id": "1",
#                                         "title": "Referred by Friend",
#                                     },
#                                 },
#                             }
#                         ],
#                     },
#                     "field": "messages",
#                 }
#             ],
#         }
#     ],
# }
#
#
# b = {
#     "object": "whatsapp_business_account",
#     "entry": [
#         {
#             "id": "104861202286839",
#             "changes": [
#                 {
#                     "value": {
#                         "messaging_product": "whatsapp",
#                         "metadata": {
#                             "display_phone_number": "15550054716",
#                             "phone_number_id": "106519662119427",
#                         },
#                         "contacts": [
#                             {"profile": {"name": "Parth"}, "wa_id": "917227856454"}
#                         ],
#                         "messages": [
#                             {
#                                 "from": "917227856454",
#                                 "id": "wamid.HBgMOTE3MjI3ODU2NDU0FQIAEhggNTg3NDJDQTZFQzM2MDQxQ0U5NzVGMDE1RDUzRTk0RjkA",
#                                 "timestamp": "1657026173",
#                                 "type": "document",
#                                 "document": {
#                                     "caption": "certificate.pdf",
#                                     "filename": "certificate.pdf",
#                                     "mime_type": "application/pdf",
#                                     "sha256": "D/oNA1RlM9Zm9oAAPvkE5y/Z9LftB98Kdou fRuPAnI=",
#                                     "id": "1159973034927406",
#                                 },
#                             }
#                         ],
#                     },
#                     "field": "messages",
#                 }
#             ],
#         }
#     ],
# }
a = {"name": "parth"}
print(a)
a["name"] = "hitchhicker"
print(a)
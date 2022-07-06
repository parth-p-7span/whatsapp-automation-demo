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


b = {
    "object": "whatsapp_business_account",
    "entry": [
        {
            "id": "104861202286839",
            "changes": [
                {
                    "value": {
                        "messaging_product": "whatsapp",
                        "metadata": {
                            "display_phone_number": "15550054716",
                            "phone_number_id": "106519662119427",
                        },
                        "contacts": [
                            {"profile": {"name": "Parth"}, "wa_id": "917227856454"}
                        ],
                        "messages": [
                            {
                                "from": "917227856454",
                                "id": "wamid.HBgMOTE3MjI3ODU2NDU0FQIAEhggNTg3NDJDQTZFQzM2MDQxQ0U5NzVGMDE1RDUzRTk0RjkA",
                                "timestamp": "1657026173",
                                "type": "document",
                                "document": {
                                    "caption": "certificate.pdf",
                                    "filename": "certificate.pdf",
                                    "mime_type": "application/pdf",
                                    "sha256": "D/oNA1RlM9Zm9oAAPvkE5y/Z9LftB98Kdou fRuPAnI=",
                                    "id": "1159973034927406",
                                },
                            }
                        ],
                    },
                    "field": "messages",
                }
            ],
        }
    ],
}

res = requests.put(
    url='https://graph.facebook.com/v13.0/messages/wamid.HBgMOTE4NzgwNDk1ODA0FQIAEhggQkU2OURGQUYyMzdCNDlBRkQ1QUI4RERBNDdENDBBOEIA',
    headers=constants.header,
    data=json.dumps({"status": "read"})
)

print(res.json())

a = {
    "tasks": [
        {
            "id": "2hjmtct",
            "custom_id": None,
            "name": "testing",
            "text_content": None,
            "description": None,
            "status": {
                "status": "to do",
                "color": "#d3d3d3",
                "type": "open",
                "orderindex": 0,
            },
            "orderindex": "1.16570915448270000000000000000000",
            "date_created": "1657091544894",
            "date_updated": "1657098936411",
            "date_closed": None,
            "archived": False,
            "creator": {
                "id": 55224230,
                "username": "Parth Panchal",
                "color": "#2ea52c",
                "email": "parth.p@7span.com",
                "profilePicture": "https://attachments.clickup.com/profilePictures/55224230_QN4.jpg",
            },
            "assignees": [
                {
                    "id": 55224230,
                    "username": "Parth Panchal",
                    "color": "#2ea52c",
                    "initials": "PP",
                    "email": "parth.p@7span.com",
                    "profilePicture": "https://attachments.clickup.com/profilePictures/55224230_QN4.jpg",
                }
            ],
            "watchers": [],
            "checklists": [],
            "tags": [],
            "parent": None,
            "priority": None,
            "due_date": None,
            "start_date": None,
            "points": None,
            "time_estimate": None,
            "custom_fields": [
                {
                    "id": "fd115c03-f971-4f44-adb8-94ac088a77f3",
                    "name": "ctc",
                    "type": "short_text",
                    "type_config": {},
                    "date_created": "1657091367164",
                    "hide_from_guests": False,
                    "value": "1000000",
                    "required": False,
                },
                {
                    "id": "bfca8c8e-634a-4543-971b-909c7e7322b9",
                    "name": "email",
                    "type": "email",
                    "type_config": {},
                    "date_created": "1657089917052",
                    "hide_from_guests": False,
                    "value": "test@gmail.com",
                    "required": False,
                },
                {
                    "id": "6bce46e0-5d72-4be9-ab60-4a3eae1603a9",
                    "name": "experience",
                    "type": "short_text",
                    "type_config": {},
                    "date_created": "1657091352952",
                    "hide_from_guests": False,
                    "value": "1",
                    "required": False,
                },
                {
                    "id": "13ae96f3-1140-4f83-879f-0ca7ae842594",
                    "name": "location",
                    "type": "short_text",
                    "type_config": {},
                    "date_created": "1657091376104",
                    "hide_from_guests": False,
                    "value": "Ahmedabad",
                    "required": False,
                },
                {
                    "id": "ce641c6a-0afe-40ad-8add-ba8f74d28bfb",
                    "name": "mediator",
                    "type": "labels",
                    "type_config": {
                        "options": [
                            {
                                "id": "56635045-2dc8-44d2-9bec-0421b0432b98",
                                "label": "referred by friend",
                                "color": "#f900ea",
                            },
                            {
                                "id": "d8e41d7a-b449-41dc-9b07-540acb67a0f9",
                                "label": "instagram/facebook",
                                "color": "#1bbc9c",
                            },
                            {
                                "id": "c2f1675c-3b72-42ea-82a8-81fac5c535b9",
                                "label": "other",
                                "color": "#AF7E2E",
                            },
                        ]
                    },
                    "date_created": "1657091496277",
                    "hide_from_guests": False,
                    "value": ["56635045-2dc8-44d2-9bec-0421b0432b98"],
                    "required": False,
                },
                {
                    "id": "9f3f2e7b-013e-41f1-bde2-9c313f4e2805",
                    "name": "mobile",
                    "type": "phone",
                    "type_config": {},
                    "date_created": "1657089997421",
                    "hide_from_guests": False,
                    "value": " 91 1234 567 890",
                    "required": False,
                },
                {
                    "id": "9900d159-9bf6-4796-9a88-ee2f58345b89",
                    "name": "skills",
                    "type": "short_text",
                    "type_config": {},
                    "date_created": "1657091317832",
                    "hide_from_guests": False,
                    "value": "flutter, python",
                    "required": False,
                },
                {
                    "id": "16a41880-d6fe-46e1-9212-3e493fff3d36",
                    "name": "summary",
                    "type": "text",
                    "type_config": {},
                    "date_created": "1657091515072",
                    "hide_from_guests": False,
                    "value": "This is auto test.",
                    "required": False,
                },
                {
                    "id": "1ab85655-602e-47dc-a351-b75c6655e06c",
                    "name": "whatsapp_id",
                    "type": "short_text",
                    "type_config": {},
                    "date_created": "1657097928256",
                    "hide_from_guests": False,
                    "value": "918780495804",
                    "required": False,
                },
            ],
            "dependencies": [],
            "linked_tasks": [],
            "team_id": "37495037",
            "url": "https://app.clickup.com/t/2hjmtct",
            "permission_level": "create",
            "list": {"id": "193238502", "name": "applicants", "access": True},
            "project": {
                "id": "115314510",
                "name": "hidden",
                "hidden": True,
                "access": True,
            },
            "folder": {
                "id": "115314510",
                "name": "hidden",
                "hidden": True,
                "access": True,
            },
            "space": {"id": "61373465"},
        }
    ]
}

c = {
    "tasks": [
        {
            "id": "2hjnjnt",
            "custom_id": None,
            "name": "hitch hicker",
            "text_content": None,
            "description": None,
            "status": {
                "status": "to do",
                "color": "#d3d3d3",
                "type": "open",
                "orderindex": 0,
            },
            "orderindex": "5.00000000000000000000000000000000",
            "date_created": "1657099634125",
            "date_updated": "1657099642929",
            "date_closed": None,
            "archived": False,
            "creator": {
                "id": 55224230,
                "username": "Parth Panchal",
                "color": "#2ea52c",
                "email": "parth.p@7span.com",
                "profilePicture": "https://attachments.clickup.com/profilePictures/55224230_QN4.jpg",
            },
            "assignees": [
                {
                    "id": 55224230,
                    "username": "Parth Panchal",
                    "color": "#2ea52c",
                    "initials": "PP",
                    "email": "parth.p@7span.com",
                    "profilePicture": "https://attachments.clickup.com/profilePictures/55224230_QN4.jpg",
                }
            ],
            "watchers": [],
            "checklists": [],
            "tags": [],
            "parent": None,
            "priority": None,
            "due_date": None,
            "start_date": None,
            "points": None,
            "time_estimate": None,
            "custom_fields": [
                {
                    "id": "fd115c03-f971-4f44-adb8-94ac088a77f3",
                    "name": "ctc",
                    "type": "short_text",
                    "type_config": {},
                    "date_created": "1657091367164",
                    "hide_from_guests": False,
                    "required": False,
                },
                {
                    "id": "bfca8c8e-634a-4543-971b-909c7e7322b9",
                    "name": "email",
                    "type": "email",
                    "type_config": {},
                    "date_created": "1657089917052",
                    "hide_from_guests": False,
                    "required": False,
                },
                {
                    "id": "6bce46e0-5d72-4be9-ab60-4a3eae1603a9",
                    "name": "experience",
                    "type": "short_text",
                    "type_config": {},
                    "date_created": "1657091352952",
                    "hide_from_guests": False,
                    "required": False,
                },
                {
                    "id": "cd6b452d-d6ac-4772-a1e8-e22594ec333e",
                    "name": "last_company",
                    "type": "short_text",
                    "type_config": {},
                    "date_created": "1657100722946",
                    "hide_from_guests": False,
                    "required": False,
                },
                {
                    "id": "13ae96f3-1140-4f83-879f-0ca7ae842594",
                    "name": "location",
                    "type": "short_text",
                    "type_config": {},
                    "date_created": "1657091376104",
                    "hide_from_guests": False,
                    "required": False,
                },
                {
                    "id": "ce641c6a-0afe-40ad-8add-ba8f74d28bfb",
                    "name": "mediator",
                    "type": "labels",
                    "type_config": {
                        "options": [
                            {
                                "id": "56635045-2dc8-44d2-9bec-0421b0432b98",
                                "label": "referred by friend",
                                "color": "#f900ea",
                            },
                            {
                                "id": "d8e41d7a-b449-41dc-9b07-540acb67a0f9",
                                "label": "instagram/facebook",
                                "color": "#1bbc9c",
                            },
                            {
                                "id": "c2f1675c-3b72-42ea-82a8-81fac5c535b9",
                                "label": "other",
                                "color": "#AF7E2E",
                            },
                        ]
                    },
                    "date_created": "1657091496277",
                    "hide_from_guests": False,
                    "required": False,
                },
                {
                    "id": "9f3f2e7b-013e-41f1-bde2-9c313f4e2805",
                    "name": "mobile",
                    "type": "phone",
                    "type_config": {},
                    "date_created": "1657089997421",
                    "hide_from_guests": False,
                    "required": False,
                },
                {
                    "id": "9900d159-9bf6-4796-9a88-ee2f58345b89",
                    "name": "skills",
                    "type": "short_text",
                    "type_config": {},
                    "date_created": "1657091317832",
                    "hide_from_guests": False,
                    "required": False,
                },
                {
                    "id": "16a41880-d6fe-46e1-9212-3e493fff3d36",
                    "name": "summary",
                    "type": "text",
                    "type_config": {},
                    "date_created": "1657091515072",
                    "hide_from_guests": False,
                    "required": False,
                },
                {
                    "id": "1ab85655-602e-47dc-a351-b75c6655e06c",
                    "name": "whatsapp_id",
                    "type": "short_text",
                    "type_config": {},
                    "date_created": "1657097928256",
                    "hide_from_guests": False,
                    "value": "917227856454",
                    "required": False,
                },
            ],
            "dependencies": [],
            "linked_tasks": [],
            "team_id": "37495037",
            "url": "https://app.clickup.com/t/2hjnjnt",
            "permission_level": "create",
            "list": {"id": "193238502", "name": "applicants", "access": True},
            "project": {
                "id": "115314510",
                "name": "hidden",
                "hidden": True,
                "access": True,
            },
            "folder": {
                "id": "115314510",
                "name": "hidden",
                "hidden": True,
                "access": True,
            },
            "space": {"id": "61373465"},
        }
    ]
}

d = {
    "tasks": [
        {
            "id": "2hjmtct",
            "custom_id": None,
            "name": "testing",
            "text_content": None,
            "description": None,
            "status": {
                "status": "to do",
                "color": "#d3d3d3",
                "type": "open",
                "orderindex": 0,
            },
            "orderindex": "1.16570915448270000000000000000000",
            "date_created": "1657091544894",
            "date_updated": "1657098936411",
            "date_closed": None,
            "archived": False,
            "creator": {
                "id": 55224230,
                "username": "Parth Panchal",
                "color": "#2ea52c",
                "email": "parth.p@7span.com",
                "profilePicture": "https://attachments.clickup.com/profilePictures/55224230_QN4.jpg",
            },
            "assignees": [
                {
                    "id": 55224230,
                    "username": "Parth Panchal",
                    "color": "#2ea52c",
                    "initials": "PP",
                    "email": "parth.p@7span.com",
                    "profilePicture": "https://attachments.clickup.com/profilePictures/55224230_QN4.jpg",
                }
            ],
            "watchers": [],
            "checklists": [],
            "tags": [],
            "parent": None,
            "priority": None,
            "due_date": None,
            "start_date": None,
            "points": None,
            "time_estimate": None,
            "custom_fields": [
                {
                    "id": "fd115c03-f971-4f44-adb8-94ac088a77f3",
                    "name": "ctc",
                    "type": "short_text",
                    "type_config": {},
                    "date_created": "1657091367164",
                    "hide_from_guests": False,
                    "value": "1000000",
                    "required": False,
                },
                {
                    "id": "bfca8c8e-634a-4543-971b-909c7e7322b9",
                    "name": "email",
                    "type": "email",
                    "type_config": {},
                    "date_created": "1657089917052",
                    "hide_from_guests": False,
                    "value": "test@gmail.com",
                    "required": False,
                },
                {
                    "id": "6bce46e0-5d72-4be9-ab60-4a3eae1603a9",
                    "name": "experience",
                    "type": "short_text",
                    "type_config": {},
                    "date_created": "1657091352952",
                    "hide_from_guests": False,
                    "value": "1",
                    "required": False,
                },
                {
                    "id": "b7650abe-74ee-4a1b-84bc-f56655711050",
                    "name": "full_name",
                    "type": "short_text",
                    "type_config": {},
                    "date_created": "1657108765012",
                    "hide_from_guests": False,
                    "required": False,
                },
                {
                    "id": "cd6b452d-d6ac-4772-a1e8-e22594ec333e",
                    "name": "last_company",
                    "type": "short_text",
                    "type_config": {},
                    "date_created": "1657100722946",
                    "hide_from_guests": False,
                    "required": False,
                },
                {
                    "id": "13ae96f3-1140-4f83-879f-0ca7ae842594",
                    "name": "location",
                    "type": "short_text",
                    "type_config": {},
                    "date_created": "1657091376104",
                    "hide_from_guests": False,
                    "value": "Ahmedabad",
                    "required": False,
                },
                {
                    "id": "ce641c6a-0afe-40ad-8add-ba8f74d28bfb",
                    "name": "mediator",
                    "type": "labels",
                    "type_config": {
                        "options": [
                            {
                                "id": "56635045-2dc8-44d2-9bec-0421b0432b98",
                                "label": "referred by friend",
                                "color": "#f900ea",
                            },
                            {
                                "id": "d8e41d7a-b449-41dc-9b07-540acb67a0f9",
                                "label": "instagram/facebook",
                                "color": "#1bbc9c",
                            },
                            {
                                "id": "c2f1675c-3b72-42ea-82a8-81fac5c535b9",
                                "label": "other",
                                "color": "#AF7E2E",
                            },
                        ]
                    },
                    "date_created": "1657091496277",
                    "hide_from_guests": False,
                    "value": ["56635045-2dc8-44d2-9bec-0421b0432b98"],
                    "required": False,
                },
                {
                    "id": "9f3f2e7b-013e-41f1-bde2-9c313f4e2805",
                    "name": "mobile",
                    "type": "phone",
                    "type_config": {},
                    "date_created": "1657089997421",
                    "hide_from_guests": False,
                    "value": " 91 1234 567 890",
                    "required": False,
                },
                {
                    "id": "9900d159-9bf6-4796-9a88-ee2f58345b89",
                    "name": "skills",
                    "type": "short_text",
                    "type_config": {},
                    "date_created": "1657091317832",
                    "hide_from_guests": False,
                    "value": "fluttter, python",
                    "required": False,
                },
                {
                    "id": "16a41880-d6fe-46e1-9212-3e493fff3d36",
                    "name": "summary",
                    "type": "text",
                    "type_config": {},
                    "date_created": "1657091515072",
                    "hide_from_guests": False,
                    "value": "This is auto test.",
                    "required": False,
                },
                {
                    "id": "1ab85655-602e-47dc-a351-b75c6655e06c",
                    "name": "whatsapp_id",
                    "type": "short_text",
                    "type_config": {},
                    "date_created": "1657097928256",
                    "hide_from_guests": False,
                    "value": "918780495804",
                    "required": False,
                },
            ],
            "dependencies": [],
            "linked_tasks": [],
            "team_id": "37495037",
            "url": "https://app.clickup.com/t/2hjmtct",
            "permission_level": "create",
            "list": {"id": "193238502", "name": "applicants", "access": True},
            "project": {
                "id": "115314510",
                "name": "hidden",
                "hidden": True,
                "access": True,
            },
            "folder": {
                "id": "115314510",
                "name": "hidden",
                "hidden": True,
                "access": True,
            },
            "space": {"id": "61373465"},
        }
    ]
}


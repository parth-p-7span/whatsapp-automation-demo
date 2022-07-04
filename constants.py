WA_ENDPOINT = 'https://graph.facebook.com/v13.0/106519662119427/messages'

header = {
    "Authorization": "Bearer EABMCARdnUF8BAAPYpAXpZB4Dt3S7uxFZCKeD7iuCECaycZAvKoNz6s7mAJywflAci2FZBknuxYiG7COC4ZAUaOfFMNzptSHa7ZC6Sahn0SPAV2hFCMN3CilUyUYOMvem4pg6E9nJZCCZBZBXT0ZCAfKU8tNdrIZCpvujzI5JQUxYHtNCjxDJKWB1aZBZBozSFL3zVWJKoYhxT5EutLdT6aqg4sv3U",
    "Content-Type": "application/json"
}

interactive_msg_body = {
    "type": "button",
    "body": {
        "text": "How did you come to know about 7Span?"
    },
    "footer": {
        "text": "Seven Bot"
    },
    "action": {
        # "button": "Select Any Medium",
        # "sections": [
        #     {
        #         "title": "",
        #         "rows": [
        #             {
        #                 "id": "1",
        #                 "title": "Referred by Friend",
        #                 "description": ""
        #             },
        #             {
        #                 "id": "2",
        #                 "title": "Instagram/Facebook",
        #                 "description": ""
        #             },
        #             {
        #                 "id": "3",
        #                 "title": "Other",
        #                 "description": ""
        #             },
        #             {
        #                 "id": "4",
        #                 "title": "HR Mail",
        #                 "description": ""
        #             }
        #         ]
        #     }
        # ],
        "buttons": [
            {
              "type": "reply",
              "reply": {
                "id": "1",
                "title": "Referred by Friend"
              }
            },
            {
              "type": "reply",
              "reply": {
                "id": "2",
                "title": "Instagram/Facebook"
              }
            },
            {
              "type": "reply",
              "reply": {
                "id": "3",
                "title": "Other"
              }
            },
          ]
    }
}

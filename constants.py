WA_ENDPOINT = 'https://graph.facebook.com/v13.0/106519662119427/messages'

header = {
    "Authorization": "Bearer EABMCARdnUF8BAKCfXH8Cbr95aWZAqWGwvdUpwAi1qTmIbZBTlfnmQZB2xGga34zXp4uZCOIsg5NGNWoszIrTmOb8xieX1oDev0gcJCcKppRzaCUyAsqa5k5KTcAXn72IfeRIebpD9amQN5dUc1OuTY7D58attejKhyH824ZBCUVPj3v2JxWeKwn5CHxqv2ZBORy4oaOQtfz03lzZAx9ub1X",
    "Content-Type": "application/json"
}

interactive_msg_body = {
    "type": "button",
    "body": {
        "text": "10. How did you come to know about 7Span?"
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

a = "kjaf"

WA_ENDPOINT = 'https://graph.facebook.com/v13.0/106519662119427/messages'

header = {
    "Authorization": "Bearer EABMCARdnUF8BAIDqRLwBmDz5DEoq1BbIUmoz91oLz67ayLWHNrDoomvg0GGLLeVw7wptojDwvVuwIljCmpBzhop8Bw2dZCfbDtZBSbrSVWeANP4XPKhEZAfl9ZAhFDCVSOaWNLZCobvJKSKVzI0UNV1x60cTe2osZAyZBRSOEPKqieGfgbkFgZA3VotZATCmlY7XtMM75nKdRGIqI7GxCdwqW",
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

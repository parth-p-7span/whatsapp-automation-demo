WA_ENDPOINT = 'https://graph.facebook.com/v13.0/106519662119427/messages'

header = {
    "Authorization": "Bearer EABMCARdnUF8BAAPYpAXpZB4Dt3S7uxFZCKeD7iuCECaycZAvKoNz6s7mAJywflAci2FZBknuxYiG7COC4ZAUaOfFMNzptSHa7ZC6Sahn0SPAV2hFCMN3CilUyUYOMvem4pg6E9nJZCCZBZBXT0ZCAfKU8tNdrIZCpvujzI5JQUxYHtNCjxDJKWB1aZBZBozSFL3zVWJKoYhxT5EutLdT6aqg4sv3U",
    "Content-Type": "application/json"
}

interactive_msg_body = {
  "type": "button",
  "body": {
    "text": "you can select the data multiple times but only one data can be select at a single time."
  },
  "footer": {
    "text": "Seven Bot"
  },
  "action": {
    "sections": [
       {
          "title":"your-section-title-content",
          "rows": [
            {
              "id":"1",
              "title": "row-title-content-1",
              "description": "row-description-content"
            },
            {
              "id":"2",
              "title": "row-title-content-2",
              "description": "row-description-content"
            },
            {
              "id":"3",
              "title": "row-title-content-3",
              "description": "row-description-content"
            },
            {
              "id":"4",
              "title": "row-title-content-4",
              "description": "row-description-content"
            }
          ]
        }
    ],
    "buttons": [
        {
          "type": "reply",
          "reply": {
            "id": "unique-postback-id",
            "title": "First Button’s Title"
          }
        },
        {
          "type": "reply",
          "reply": {
            "id": "unique-postback-id",
            "title": "Second Button’s Title"
          }
        }
      ]
  }
}
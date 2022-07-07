WA_ENDPOINT = 'https://graph.facebook.com/v13.0/106519662119427/messages'

header = {
    "Authorization": "Bearer EABMCARdnUF8BAJZBw2SqFgbAlfuI2MZBZCXcYdR0ounYJsgK9ZBRM4bgembblx8QvfKVRXvWHl75iXxqOUVoFrnYAcTkBL2311oKcgZCGfZAid4d6uMheDMCRtFfPkO8ShzrzlGFJfNlYpU1ERCGGmlvTqUEZCCI5YZB3odxTbh5qZBXSiUFo63cooBL6DsRk2ZAv8B5LEMDUffE9sOJmSV1QC",
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

parth_clickup_token = "pk_55224230_PRW3UPHYHCOHIBWZQNF20ATOVOJ7I6GB"

clickup_header = {"Content-type": "application/json", "Authorization": parth_clickup_token}

# APIs
get_team = "https://api.clickup.com/api/v2/team"
get_task = "https://api.clickup.com/api/v2/task"
list_url = "https://api.clickup.com/api/v2/list/193238502/task"

# clickup custom field ids
email_field_id = "bfca8c8e-634a-4543-971b-909c7e7322b9"
mobile_field_id = "9f3f2e7b-013e-41f1-bde2-9c313f4e2805"
skills_field_id = "9900d159-9bf6-4796-9a88-ee2f58345b89"
experience_field_id = "6bce46e0-5d72-4be9-ab60-4a3eae1603a9"
ctc_field_id = "fd115c03-f971-4f44-adb8-94ac088a77f3"
location_field_id = "13ae96f3-1140-4f83-879f-0ca7ae842594"
summary_field_id = "16a41880-d6fe-46e1-9212-3e493fff3d36"
mediator_field_id = "ce641c6a-0afe-40ad-8add-ba8f74d28bfb"
whatsapp_field_id = "1ab85655-602e-47dc-a351-b75c6655e06c"
name_field_id = "b7650abe-74ee-4a1b-84bc-f56655711050"
last_company_field_id = "cd6b452d-d6ac-4772-a1e8-e22594ec333e"

# whatsapp custom field ids
custom_field_ids = {
    "Referred by Friend": "56635045-2dc8-44d2-9bec-0421b0432b98",
    "Instagram/Facebook": "d8e41d7a-b449-41dc-9b07-540acb67a0f9",
    "Other": "c2f1675c-3b72-42ea-82a8-81fac5c535b9"
}

from flask import Flask, request
import requests
import json

import constants
import func
# import clickup
from firebase import Firebase

app = Flask(__name__)
app.config['SECRET_KEY'] = '12cne83nds3v-faj32bde-bba8-cje23-2dbr'

instance = Firebase()


@app.route('/', methods=['GET', 'POST'])
def home():
    return 'HOME'


@app.route('/webhook', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        verify_token = '23rf313uf-9du2bbc0-cj382nsd-nc238'

        if 'hub.mode' in request.args:
            mode = request.args.get('hub.mode')
            print('MODE => ', mode)

        if 'hub.verify_token' in request.args:
            token = request.args.get('hub.verify_token')
            print("TOKEN => ", token)

        if 'hub.challenge' in request.args:
            challenge = request.args.get('hub.challenge')
            print("CHALLENGE => ", challenge)

        if 'hub.mode' in request.args and 'hub.verify_token' in request.args:
            mode = request.args.get('hub.mode')
            token = request.args.get('hub.verify_token')

            if mode == 'subscribe' and token == verify_token:
                print('WEBHOOK VERIFIED')
                challenge = request.args.get('hub.challenge')
                return challenge, 200
            else:
                return 'ERROR', 403

        data = request.data
        body = json.loads(data.decode('utf8'))
        print("BODY => ", body)
        if 'object' in body and body['object'] == 'whatsapp_business_account':

            message_value = body['entry'][0]['changes'][0]['value']
            message_product = message_value['messaging_product']
            if message_product == 'whatsapp':
                if 'messages' in message_value:
                    author_name = message_value['contacts'][0]['profile']['name']
                    message_object = message_value['messages'][0]
                    message_type = message_object['type']
                    message_id = message_object['id']
                    user_id = message_object['from']

                    func.mark_as_read(message_id)

                    users_data = instance.get_user_data(user_id)

                    last_msg = -2
                    for i, value in enumerate(users_data):
                        if value == 0:
                            last_msg = i - 1
                            break

                    print("-------->", users_data)

                    if message_type == "interactive":
                        message_text = message_object['interactive']['button_reply']['title']
                        instance.update_user(user_id, "platform", message_text)
                        # clickup.set_custom_field_value(task_id, constants.mediator_field_id,
                        #                                [constants.custom_field_ids[message_text]])
                        string = "11. Please upload your resume then you are finish with the process."
                        response = func.send_message(string, message_object['from'])
                        print(response)

                    elif message_type == "document" and last_msg == 11:
                        string = "Thank you for applying to 7Span, our HR will contact you shortly."
                        response = func.send_message(string, message_object['from'])
                        print(response)

                    elif message_type == "text":
                        message_text = message_object['text']['body']

                        if (message_text.lower() == "hi" or message_text.lower() == "hello" or message_text.lower() == "hii") and last_msg == -1:
                            instance.delete_data(user_id)
                            instance.create_user(user_id, author_name)
                            # response = clickup.create_new_task(author_name)
                            # clickup.set_custom_field_value(response['id'], constants.whatsapp_field_id,
                            #                                message_object['from'])

                            string = f"Hi {author_name},\nThankyou for applying in 7Span. I am auto-reply Bot of 7Span. You just have to answer few questions to send your application.\n\n1.Please enter your full name."
                            response = func.send_message(string, message_object['from'])
                            print(response)

                        if last_msg == 0:
                            instance.update_user(user_id, "name", message_text)
                            # clickup.update_task_name(task_id, message_text)
                            # clickup.set_custom_field_value(task_id, constants.name_field_id, message_text)
                            string = "2. Please enter your official email address."
                            response = func.send_message(string, message_object['from'])
                            print(response)

                        if last_msg == 1:
                            instance.update_user(user_id, "email", message_text)
                            # clickup.set_custom_field_value(task_id, constants.email_field_id, message_text)
                            string = "3. Please enter your official mobile number."
                            response = func.send_message(string, message_object['from'])
                            print(response)

                        if last_msg == 2:
                            instance.update_user(user_id, "mobile", message_text)
                            # clickup.set_custom_field_value(task_id, constants.mobile_field_id, f'+91{message_text}')
                            string = "4. Please enter your skills separated by comma. e.g. React, Laravel, Angular, Python"
                            response = func.send_message(string, message_object['from'])
                            print(response)

                        if last_msg == 3:
                            instance.update_user(user_id, "skills", message_text)
                            # clickup.set_custom_field_value(task_id, constants.skills_field_id, message_text)
                            string = "5. Please enter your total years of experience."
                            response = func.send_message(string, message_object['from'])
                            print(response)

                        if last_msg == 4:
                            instance.update_user(user_id, "experience", message_text)
                            # clickup.set_custom_field_value(task_id, constants.experience_field_id, message_text)
                            string = "6. Please enter your current/last company name"
                            response = func.send_message(string, message_object['from'])
                            print(response)

                        if last_msg == 5:
                            instance.update_user(user_id, "last_company", message_text)
                            # clickup.set_custom_field_value(task_id, constants.last_company_field_id, message_text)
                            string = "7. Please enter your current CTC(Per Annum)"
                            response = func.send_message(string, message_object['from'])
                            print(response)

                        if last_msg == 6:
                            instance.update_user(user_id, "ctc", message_text)
                            # clickup.set_custom_field_value(task_id, constants.ctc_field_id, message_text)
                            string = "8. Please enter your current location"
                            response = func.send_message(string, message_object['from'])
                            print(response)

                        if last_msg == 7:
                            instance.update_user(user_id, "location", message_text)
                            # clickup.set_custom_field_value(task_id, constants.location_field_id, message_text)
                            string = "9. Please enter little summary about you."
                            response = func.send_message(string, message_object['from'])
                            print(response)

                        if last_msg == 8:
                            instance.update_user(user_id, "summary", message_text)
                            # clickup.set_custom_field_value(task_id, constants.summary_field_id, message_text)
                            response = func.send_selection_msg(message_object['from'])
                            print(response)

            return 'EVENT_RECEIVED', 200
        else:
            return 'ERROR', 404


if __name__ == '__main__':
    app.run()

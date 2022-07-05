from flask import Flask, request
import requests
import json
import func

app = Flask(__name__)
app.config['SECRET_KEY'] = '12cne83nds3v-faj32bde-bba8-cje23-2dbr'


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
                    message_author = message_value['messages'][0]['from']
                    message_object = message_value['messages'][0]
                    message_text = message_object['text']['body']
                    message_type = message_object['type']

                    if "skills" in message_text:
                        response = func.send_selection_msg(message_object['from'])
                        print(response)

                    if "hi" in message_text:
                        response = func.send_message("enter_email", message_object['from'])
                        print(response)
            return 'EVENT_RECEIVED', 200
        else:
            return 'ERROR', 404


if __name__ == '__main__':
    # app.run(host='localhost', port=8080, debug=True)
    app.run()

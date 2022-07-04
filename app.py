from flask import Flask, request
import requests
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = '12cne83nds3v-faj32bde-bba8-cje23-2dbr'


@app.route('/', methods=['GET','POST'])
def home():
    return 'HOME'


@app.route('/webhook', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        verify_token = '23rf313uf-9du2bbc0-cj382nsd-nc238'

        if 'hub.mode' in request.args:
            mode = request.args.get('hub.mode')
            print('MODE => ',mode)

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
        return 'SOMETHING', 200

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
        print("DATA ==> ", data)
        print("BODY ==> ", body)
        if 'object' in body and body['object'] == 'page':
            entries = body['entry']
            for entry in entries:
                webhook_event = entry['messaging'][0]
                print(webhook_event)

                sender_psid = webhook_event['sender']['id']
                print('Sender PSID => ', sender_psid)

                if 'message' in webhook_event:
                    print('WEBHOOK EVENT MESSAGE => ', webhook_event['message'])
                return 'EVENT_RECEIVED', 200
        else:
            return 'ERROR', 404


if __name__ == '__main__':
    # app.run(host='localhost', port=8080, debug=True)
    app.run()

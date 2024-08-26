from flask import Flask, request
import requests
import os

app = Flask(__name__)

API_TOKEN = '7371248217:AAH-2QT4wuHv4arRq49dbUCevoWO6ZndsB0'

@app.route('/webhook', methods=['POST'])
def webhook():
    update = request.get_json()
    chat_id = update['message']['chat']['id']
    message_text = update['message']['text']

    # Xử lý tin nhắn và phản hồi
    reply = "You said: " + message_text
    send_message(chat_id, reply)
    
    return "OK", 200

def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{API_TOKEN}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    requests.post(url, json=payload)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

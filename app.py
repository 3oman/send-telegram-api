import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api')
def info():
    id = request.args.get('id') 
    token = request.args.get('token') 
    mss = request.args.get('text')
    is_html = request.args.get('html')  # يتحقق إذا كان المستخدم يريد إرسال الرسالة بصيغة HTML

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    
    payload = {
        'chat_id': id,
        'text': mss
    }

    if is_html == "1":
        payload['parse_mode'] = 'HTML'

    response = requests.post(url, data=payload)
    return response.json()

if __name__ == "__main__":
    app.run(debug=True)

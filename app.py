import requests
from flask import Flask, request
from urllib.parse import unquote

app = Flask(__name__)

@app.route('/api')
def info():
    id = request.args.get('id') 
    token = request.args.get('token') 
    mss = request.args.get('text')
    is_html = request.args.get('html')

    # فك الترميز في حال تم إرسال النص مشفراً
    mss = unquote(mss) if mss else ''

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

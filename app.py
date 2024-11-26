import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api')
def info():
    id = request.args.get('id') 
    token = request.args.get('token') 
    mss = request.args.get('text')
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={mss}"
    response = requests.post(url)
    return response.json()
if __name__ == "__main__":
    app.run(debug=True)

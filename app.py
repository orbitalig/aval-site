from flask import Flask, request, render_template, jsonify
import requests
import config

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/join', methods=['POST'])
def join():
    link = request.json.get('link')
    invite_code = link.split('/')[-1]

    headers = {
        "Authorization": f"{config.TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {}

    response = requests.post(f"https://discord.com/api/v9/invites/{invite_code}", headers=headers, json=payload)
    response_text = response.text
    if response.status_code == 200:
        return jsonify(message="Successfully joined the group chat!"), 200
    else:
        return jsonify(message=f"Failed to join the group chat. Status code: {response.status_code}\n{response_text}"), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

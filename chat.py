from flask import Flask, render_template, request, jsonify  # jsonifyをインポート

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_bot_reply', methods=['POST'])
def get_bot_reply():
    message = request.form['message']
    bot_reply = generate_bot_reply(message)
    return jsonify({'reply': bot_reply})  # JSON形式で返信内容を返す

def generate_bot_reply(message):
    if message.lower() == 'hello':
        return "Hi"
    else:
        return "what?" + message

if __name__ == '__main__':
    app.run(debug=True)

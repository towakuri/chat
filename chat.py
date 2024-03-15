from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_bot_reply', methods=['POST'])
def get_bot_reply():
    message = request.form['message']
    # ここにボットの返信を生成するコードを追加する
    bot_reply = generate_bot_reply(message)
    return bot_reply

def generate_bot_reply(message):
    # 仮のボット返信の生成
    return "Hello! I'm a bot. You said: " + message

if __name__ == '__main__':
    app.run(debug=True)

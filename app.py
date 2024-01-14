from flask import Flask, render_template, request, jsonify
from chatgpt import chat_with_gpt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_input = request.form['user_input']
    gpt_response = chat_with_gpt(user_input)
    return jsonify({'response': gpt_response})

if __name__ == '__main__':
    app.run(debug=True)
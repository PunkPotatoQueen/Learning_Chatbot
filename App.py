from flask import Flask, render_template, request, jsonify
from main import chatbot, adicionar_pergunta_resposta

app = Flask(__name__)  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot_response():
    user_input = request.form['user_input']
    response_data = chatbot(user_input)  
    return jsonify(response_data)  

@app.route('/ensinar', methods=['POST'])
def ensinar():
    question = request.form['question']
    answer = request.form['answer']
    adicionar_pergunta_resposta(question, answer)
    return jsonify({"status": "success", "message": "Aprendi uma nova resposta!"})

if __name__ == '__main__':
    app.run(debug=True)

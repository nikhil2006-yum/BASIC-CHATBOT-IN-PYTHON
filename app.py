from flask import Flask, render_template, request, jsonify
from chatbot.logic import generate_response
from chatbot.memory import Memory

app = Flask(__name__)
memory = Memory()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    response = generate_response(user_input)

    memory.add(user_input, response)

    return jsonify({
        "response": response,
        "history": memory.get_history()
    })

if __name__ == "__main__":
    app.run(debug=True)

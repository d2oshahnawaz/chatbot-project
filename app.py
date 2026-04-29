from flask import Flask, render_template, request, jsonify
import random
from train_model import predict_intent
from chatbot_model import responses

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.json["message"].lower()

    intent = predict_intent(user_input)

    if intent in responses:
        reply = random.choice(responses[intent])
    else:
        reply = "Sorry, I don't understand."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
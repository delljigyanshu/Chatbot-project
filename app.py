from flask import Flask, render_template, request, jsonify
from chatbot import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.json.get("message")
    if user_input:
        response = get_response(user_input)
        return jsonify({"response": response})
    else:
        return jsonify({"response": "Please enter a valid message."})

if __name__ == "__main__":
    app.run(debug=True)


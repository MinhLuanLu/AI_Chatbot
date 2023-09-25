from flask import Flask, render_template, request
from chatbot import initialize_openai, chat_with_chatgpt

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    initialize_openai()
    chat_response = None
    user_input = "Ask me anything..."

    if request.method == "POST":
        user_input = request.form.get("id")
        chat_response = chat_with_chatgpt(user_input)
        if user_input == "":
            user_input = "Waiting...    "

    return render_template("index.html", chat_response=chat_response, user_input=user_input)

@app.route('/about')
def about():
    return render_template('about.html')

     
if __name__ == "__main__":
    app.run(debug=True)
 
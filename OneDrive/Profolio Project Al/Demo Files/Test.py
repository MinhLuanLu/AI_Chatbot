import pyttsx3
import speech_recognition as sr
from flask import Flask, render_template, request
import openai

app = Flask(__name__)

chatbot_name = "Javis"

with open("API_KEY.txt", "r") as file:
    api_key = file.read().strip()
    openai.api_key = api_key

def chat_with_chatgpt(prompt, model="gpt-3.5-turbo"):
    conversation = [
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": ""}
    ]

    response = openai.ChatCompletion.create(
        model=model,
        messages=conversation,
        max_tokens=100,
        temperature=0.5,
    )

    message = response['choices'][0]['message']['content'].strip()
    return message

@app.route('/')
def index():
    return render_template('chatbot_GUI1.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['userInput']
    chatbot_response = chat_with_chatgpt(user_input)
    return chatbot_response

def chatbot_speak(text):
    chatbot_say = pyttsx3.init()
    chatbot_say.say(text)
    chatbot_say.runAndWait()
    chatbot_say.stop()

if __name__ == "__main__":
    app.run(debug=True)

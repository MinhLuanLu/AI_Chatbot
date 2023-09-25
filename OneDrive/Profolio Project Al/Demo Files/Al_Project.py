import requests
import openai
import pyttsx3
import speech_recognition

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

def wellcome_chatbot():
    name = input("Enter your name here: ")
    chatbot_say = pyttsx3.init()
    chatbot_say.say("Hi, I´m" + chatbot_name)
    chatbot_say.say("Hello" + name + " What can I do for you?...")
    chatbot_say.runAndWait()
    chatbot_say.stop()
    

def text_response ():
    user = input("Ask: \n")
    chatbot = chat_with_chatgpt(user)
    print("\nUser: \n" + user + ".\n" + "\n" + "Chatbot:\n" + chatbot)

    chatbot_say = pyttsx3.init()
    chatbot_say.say(chatbot)
    chatbot_say.runAndWait()
    chatbot_say.stop()


def voice_response():
    hearing = speech_recognition.Recognizer()
    with speech_recognition.Microphone()as mic:
        print("Listening.....")
        audio = hearing.listen(mic)
    try:
        user = hearing.recognize_google(audio)
        chatbot = chat_with_chatgpt(user)
        print("\nUser: \n" + user + ".\n" + "\n" + "Chatbot:\n" + chatbot)

        chatbot_say = pyttsx3.init()
        chatbot_say.say(chatbot)
        chatbot_say.runAndWait()
        chatbot_say.stop()
            
    except:
        chatbot_say.say("speech not recognised")
        chatbot_say.runAndWait()
        chatbot_say.stop()

attempts = 0


wellcome_chatbot()
while attempts < 10:
    voice_response()
    attempts += 1

    if attempts >= 10:
        print("Sorry. But you have 0 attempts left")
        break
    else:
        print("You have " + str(10 - 1) + " attemps left")
    
    

import openai

def initialize_openai(api_key_path="API_KEY.txt"):
    with open(api_key_path, "r") as file:
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

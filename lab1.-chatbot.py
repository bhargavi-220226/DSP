import random

def greet_user():
    print("🤖 Chatbot: Hello! I'm your upgraded Python chatbot!")
    name = input("🤖 Chatbot: Before we start, what's your name?\nYou: ")
    print(f"🤖 Chatbot: Nice meeting you, {name}! Let's chat. 😊")
    print("🤖 Chatbot: Type 'bye' anytime to exit.\n")
    return name
keywords = {
    "hello": "Hello there!",
    "hi": "Hi! How can I help you today?",
    "help": "Sure! I'm happy to assist. Try asking for a joke or quote!",
    "name": "I'm an upgraded Python chatbot—simple and smart!",
    "weather": "I don't fetch live weather yet, but Python can do it using APIs!",
    "creator": "I was created by a student for a chatbot lab project!",
    "favorite": "I love chatting with awesome people like you!",
    "time": "I don’t know the time, but Python can fetch it using datetime!"
}
jokes = [
    "Why do programmers hate nature? Too many bugs! 😆",
    "Why was the computer cold? It forgot to close Windows! 😂",
    "Why do Java developers wear glasses? Because they don’t C#! 🤓"
]
quotes = [
    "Believe you can and you're halfway there.",
    "Every moment is a fresh beginning.",
    "Dream big. Work hard. Stay focused.",
]

def generate_response(text):
    text = text.lower()
    for key in keywords:
        if key in text:
            return keywords[key]
    if "joke" in text:
        return random.choice(jokes)
    if "quote" in text:
        return random.choice(quotes)
    if "how are you" in text or ("how" in text and "you" in text):
        return "I'm doing great — thanks for asking! 😊"
    if "bye" in text:
        return "bye"
    return "Hmm... I don't know that. Try asking for help, a joke, or a quote!"
def start_chat():
    name = greet_user()

    while True:
        message = input(f"{name}: ")
        response = generate_response(message)

        if response == "bye":
            print("🤖 Chatbot: Bye! Have a great day! 👋")
            break

        print("🤖 Chatbot:", response)
start_chat()

from chatbot.nlp import process_input

def generate_response(user_input):
    tokens = process_input(user_input)

    if "hello" in tokens or "hi" in tokens:
        return "Hey! How can I help you?"
    elif "name" in tokens:
        return "I'm an AI chatbot built with Python."
    elif "help" in tokens:
        return "I can chat, remember conversations, and respond smartly!"
    elif "bye" in tokens:
        return "Goodbye!"
    else:
        return "Interesting... tell me more."

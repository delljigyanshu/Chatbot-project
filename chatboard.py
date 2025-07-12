import json
import random
import re

# Load intents
with open('intents.json') as file:
    intents = json.load(file)

def clean_input(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text

def get_response(user_input):
    user_input = clean_input(user_input)

    for intent in intents['intents']:
        for pattern in intent['patterns']:
            pattern = clean_input(pattern)
            if pattern in user_input:
                return random.choice(intent['responses'])

    return "I'm sorry, I didn't understand that. Can you please rephrase?"

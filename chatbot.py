import json
import random
class ChatBot:
    def __init__(self):
        with open("intents.json") as file:
            self.intents = json.load(file)
    def get_response(self, user_input):
        user_input = user_input.lower()
        for intent in self.intents["intents"]:
            for pattern in intent["patterns"]:
                if pattern in user_input:
                    return random.choice(intent["responses"])
        return "Sorry, I don't undersatnd"         
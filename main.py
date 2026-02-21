from ChatBot import ChatBot

def main():
    bot = ChatBot()

    print("AI Chatbot Started! Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "quit":
            print("Bot: Goodbye!")
            break

        response = bot.get_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
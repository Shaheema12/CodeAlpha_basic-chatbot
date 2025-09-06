
def chat():
    print("CodeAlphaBot: Hello Type something to start chatting (type 'bye' or 'exit' to quit)")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print(" CodeAlphaBot:",response)
        if user_input.lower() in ["bye", "exit"]:
            break
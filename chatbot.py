
def chatbot_response(user_input):
    responses = {
        "hello": "Hi there!",
        "hi": "hello",
        "how are you":"I'm doing well,thank you",
        "what is your name": "I'm CodeAlphaBot.",
        "bye":"GoodBye!",
        "exit":"see you later"
    }
    user_input = user_input.lower()
    return responses.get(user_input,"I'm not sure how to respond to that!.")

def chat():
    print("CodeAlphaBot: Hello Type something to start chatting (type 'bye' or 'exit' to quit)")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print(" CodeAlphaBot:",response)
        if user_input.lower() in ["bye", "exit"]:
            break
chat()

    
   
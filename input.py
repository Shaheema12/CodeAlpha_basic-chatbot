def chatbot_response(user_input):
    user_input = user_input.lower()
    return responses.get(user_input, "I'm not sure how to respond to that.")
import random
from train_model import predict_intent
from chatbot_model import responses

print("\n🤖 College Information Chatbot")
print("Type 'bye' or 'exit' to quit\n")

while True:

    user_input = input("You: ").lower()

    if user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a nice day.")
        break

    try:
        intent = predict_intent(user_input)

        if intent in responses:
            reply = random.choice(responses[intent])
            print("Bot:", reply)
        else:
            print("Bot: Sorry, I don't understand your question.")

    except:
        print("Bot: Something went wrong.")
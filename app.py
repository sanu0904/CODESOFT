# Simple Rule-Based Chatbot
# Chatbot Name: Alex

print("Alex: Hello! I am Alex, your chatbot.")
print("Alex: Type 'bye alex' if you want to end the chat.\n")

while True:

    # Taking input from user
    user_message = input("SUSHANT: ").lower()

    # Greeting responses
    if user_message == "hello alex" or user_message == "hi alex":
        print("Alex: Hi! Nice to meet you.")

    # Asking chatbot name
    elif "what is your name" in user_message:
        print(" My name is Alex.")

    # Asking about chatbot
    elif "how are you" in user_message:
        print("Alex: I am doing great. Thanks for asking!")

    # Asking time
    elif "who made you" in user_message:
        print("Alex: my devloper is sushant sir")

    # Asking about Python
    elif "what is python" in user_message:
        print("Alex: Python is an easy and powerful programming language.")

    # Goodbye message
    elif user_message == "bye alex":
        print("Alex: Goodbye! Have a wonderful day.")
        break

    # Default response
    else:
        print("Alex: Sorry, I did not understand that.")

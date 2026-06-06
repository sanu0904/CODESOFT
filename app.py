#chatbot-ALEX

 
print("Alex: Hello! I am Alex, your chatbot.")
print("Alex: Type 'bye alex' if you want to end the chat.\n")

while True:

    user_input = input("SUSHANT: ").lower()

    if user_message == "hello alex" or user_message == "hi alex":

        print("Alex: Hi! Nice to meet you.")

    elif "what is your name" in user_message:
        print(" My name is Alex.")

    elif "how are you" in user_message:
        print("Alex: I am fine. Thanks for asking!")

    elif "who made you" in user_message:
        print("Alex: my devloper is sushant sir")

    elif "what is python" in user_message:
        print("Alex: Python is an easy and powerful programming language.")

    elif user_message == "bye alex":
        print("Alex: Bye mate! Have a wonderful day.")
        break

    else:
        print("Alex: Sorry i am still at learning phase.")

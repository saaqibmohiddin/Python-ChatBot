print("🤖 ChatBot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("🤖 ChatBot: Hi! How are you?")

    elif user == "how are you":
        print("🤖 ChatBot: I am fine. Thank you!")

    elif user == "your name":
        print("🤖 ChatBot: My name is Python Bot.")

    elif user == "what is ai":
        print("🤖 ChatBot: AI stands for Artificial Intelligence.")

    elif user == "who created you":
        print("🤖 ChatBot: I was created using Python.")

    elif user == "good morning":
        print("🤖 ChatBot: Good Morning! Have a great day.")

    elif user == "good night":
        print("🤖 ChatBot: Good Night! Sweet dreams.")

    elif user == "bye":
        print("🤖 ChatBot: Goodbye!")
        break

    else:
        print("🤖 ChatBot: Sorry, I don't understand.")
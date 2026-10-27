
import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="PyTalk - Python ChatBot",
    page_icon="🤖",
    layout="centered"
)

# Chatbot responses
def get_response(user):
    user = user.lower().strip()

    if user == "hello":
        return "Hi! How are you?"

    elif user == "how are you":
        return "I am fine. Thank you!"

    elif user == "your name":
        return "My name is Python Bot."

    elif user == "what is ai":
        return "AI stands for Artificial Intelligence."

    elif user == "who created you":
        return "I was created using Python."

    elif user == "good morning":
        return "Good Morning! Have a great day."

    elif user == "good night":
        return "Good Night! Sweet dreams."

    elif user == "bye":
        return "Goodbye!"

    else:
        return "Sorry, I don't understand."

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! Welcome to PyTalk. How can I help you?"
        }
    ]

# Heading
st.title("🤖 PyTalk")
st.subheader("Your Personal Python ChatBot")
st.write("Chat with your Python-powered assistant.")

# Clear chat button
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! Welcome to PyTalk. How can I help you?"
        }
    ]
    st.rerun()

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    response = get_response(user_input)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    st.rerun()

st.caption("Built with Python and Streamlit | PyTalk")

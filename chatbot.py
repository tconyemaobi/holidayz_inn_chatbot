import streamlit as st
import requests
import json
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space

# Set page configuration
st.set_page_config(page_title="Holidayz Inn Booking Chatbot", page_icon="🏨", layout="centered")

# Custom CSS for better styling
st.markdown("""
<style>
    .stApp {
        background-color: #f0f2f6;
    }
    .stTextInput > div > div > input {
        background-color: white;
    }
    .stChat {
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
    }
    .user-message {
        background-color: #e1f5fe;
    }
    .bot-message {
        background-color: #f0f4c3;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar with hotel information
with st.sidebar:
    st.image("HolidayzInn.png", caption="Holidayz Inn")
    # st.title("Holidayz Inn")
    st.write("Welcome to Holidayz Inn, your home away from home!")
    st.write("Our chatbot is here to assist you with your booking needs.")
    add_vertical_space(2)
    st.write("© 2024 Holidayz Inn. All rights reserved.")

# Main chat interface
colored_header(label="Holidayz Inn Booking Chatbot", description="How can I assist you today?", color_name="blue-70")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Send a request to Rasa to get the welcome message
    response = requests.post("http://localhost:5005/webhooks/rest/webhook",
                             json={"sender": "user", "message": "/start"})
    for message in response.json():
        st.session_state.messages.append({"role": "assistant", "content": message['text']})

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Type your message here..."):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Send user input to Rasa and get response
    with st.spinner("Thinking..."):
        rasa_response = requests.post("http://localhost:5005/webhooks/rest/webhook",
                                      json={"sender": "user", "message": prompt})
        rasa_response_json = rasa_response.json()

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        for response in rasa_response_json:
            st.markdown(response['text'])
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response['text']})

# Add a footer
st.markdown("---")
st.markdown("Powered by Rasa and Streamlit")

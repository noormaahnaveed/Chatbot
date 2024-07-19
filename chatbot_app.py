import openai
import streamlit as st

# Set your OpenAI API key here
openai_api_key = "sk-proj-9uxtZZuJrdCYKJyGTpvmT3BlbkFJJzrYGILOhpC6Exa3nJ7N"

st.title("💬 My Simple Chatbot")
st.caption("🚀 A Streamlit chatbot powered by OpenAI")

# Sidebar for API key display
with st.sidebar:
    st.write(f"API Key: {openai_api_key}")

# Initialize the chat messages history
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# Display the chat messages from the history
for msg in st.session_state["messages"]:
    st.write(f"{msg['role']}: {msg['content']}")

# Function to handle new user input and get the assistant's response
def handle_input():
    prompt = st.session_state["input"]
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    # Append user message to the messages history
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.write(f"user: {prompt}")

    # Set the OpenAI API key and create the client
    openai.api_key = openai_api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state["messages"]
    )

    # Extract and display the assistant's response
    msg = response.choices[0].message["content"]
    st.session_state["messages"].append({"role": "assistant", "content": msg})
    st.write(f"assistant: {msg}")

    # Clear the input box after submitting
    st.session_state["input"] = ""

# Placeholder for the input box at the bottom
input_placeholder = st.empty()

# Input prompt for the user
input_placeholder.text_input("Type your message here...", key="input", on_change=handle_input)

import streamlit as st
from app import run_agent

st.set_page_config(
    page_title="🛒 AI Store Assistant",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 AI Customer Support Agent")
st.markdown("Ask anything about your orders or products.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
question = st.chat_input("Ask a question...")

if question:

    # User message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # Agent response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = run_agent(question)

            st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )
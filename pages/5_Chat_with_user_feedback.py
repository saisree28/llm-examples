import streamlit as st
from langchain_community.llms import Ollama
from streamlit_feedback import streamlit_feedback
import json
from datetime import datetime

st.title("📝 Chat with Feedback (Local LLM)")

# Initialize local LLM
llm = Ollama(model="mistral")  # or "mistral"

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "How can I help you? Leave feedback to help me improve!"}
    ]

if "response" not in st.session_state:
    st.session_state["response"] = None

messages = st.session_state.messages

# Display chat history
for msg in messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
if prompt := st.chat_input("Tell me a joke about sharks"):
    messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Generate response using local LLM
    response = llm.invoke(prompt)
    st.session_state["response"] = response

    with st.chat_message("assistant"):
        messages.append({"role": "assistant", "content": response})
        st.write(response)

# Feedback section
if st.session_state["response"]:
    feedback = streamlit_feedback(
        feedback_type="thumbs",
        optional_text_label="[Optional] Please provide an explanation",
        key=f"feedback_{len(messages)}",
    )

    if feedback:
        feedback_data = {
            "timestamp": str(datetime.now()),
            "chat": messages,
            "feedback": feedback
        }

        # Save feedback locally
        with open("feedback_log.json", "a") as f:
            f.write(json.dumps(feedback_data) + "\n")

        st.toast("Feedback recorded locally!", icon="📝")
import streamlit as st
from langchain_community.llms import Ollama

st.title("🦜🔗 LangChain Quickstart (Local LLM)")

# Initialize local model
llm = Ollama(model="mistral")  # you can also use "mistral"

def generate_response(input_text):
    response = llm.invoke(input_text)
    st.info(response)

with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "What are 3 key advice for learning how to code?"
    )
    submitted = st.form_submit_button("Submit")

    if submitted:
        generate_response(text)
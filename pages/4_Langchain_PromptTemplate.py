import streamlit as st
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate

st.title("🦜🔗 LangChain - Blog Outline Generator (Local LLM)")

# Initialize local LLM
llm = Ollama(model="mistral")  # or "mistral"

def blog_outline(topic):
    template = (
        "As an experienced data scientist and technical writer, "
        "generate a clear and structured outline for a blog about {topic}."
    )

    prompt = PromptTemplate(
        input_variables=["topic"],
        template=template
    )

    formatted_prompt = prompt.format(topic=topic)

    response = llm.invoke(formatted_prompt)

    return st.info(response)


with st.form("myform"):
    topic_text = st.text_input("Enter topic:", "")
    submitted = st.form_submit_button("Submit")

    if submitted and topic_text:
        blog_outline(topic_text)
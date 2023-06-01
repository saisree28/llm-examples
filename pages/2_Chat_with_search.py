import streamlit as st
from langchain.agents import initialize_agent, AgentType
from langchain_community.llms import Ollama
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.callbacks import StreamlitCallbackHandler

st.title("🔎 LangChain - Chat with Search (Local LLM)")

"""
This version uses:
- Ollama (local model)
- DuckDuckGo search tool
- No OpenAI API key
"""

# Initialize local LLM
llm = Ollama(model="mistral")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I'm a chatbot who can search the web. How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Who won the Women's U.S. Open in 2018?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    search = DuckDuckGoSearchRun(name="Search")

    search_agent = initialize_agent(
        tools=[search],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        handle_parsing_errors=True,
        verbose=True,
    )

    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = search_agent.run(prompt, callbacks=[st_cb])
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)
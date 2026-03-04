# LLM vs Chatbot

## What is LLM?
The term **LLM** usually refers to a **Large Language Model** in the field of artificial intelligence.

### What it is
- A type of AI system trained on massive amounts of text data.
- Built using **deep learning techniques**, especially the **Transformer architecture**.
- Designed to understand, process, and generate human-like language.

### How it works
- **Input embeddings**: Converts words into numerical vectors.
- **Positional encoding**: Adds information about word order.
- **Self-attention**: Helps the model understand relationships between words in context.
- **Training**: Uses billions of parameters and huge datasets to learn grammar, facts, and reasoning patterns.

### What it can do
- Answer questions conversationally.
- Write essays, articles, or code.
- Translate between languages.
- Summarize long documents.
- Assist in creative tasks like storytelling or brainstorming.

### Examples
- **ChatGPT** (OpenAI)
- **Google Gemini**
- **Anthropic Claude**
- **Meta LLaMA**

---

## LLM vs Chatbot

Not exactly — an **LLM** and a **chatbot** are related, but they’re not the same thing.

### LLM (Large Language Model)
- The underlying AI technology.
- Trained on massive text datasets.
- Provides the ability to understand and generate human-like language.
- Examples: GPT-4, Claude, LLaMA.

### Chatbot
- An application built on top of an LLM (or other AI systems).
- Designed to interact with users in a conversational way.
- Can include extra features like memory, personality, integration with tools (e.g., calendars, search engines).
- Examples: Microsoft Copilot, customer service bots, website assistants.

---

## Analogy
Think of it like this:
- The **LLM** is the *engine*.
- The **chatbot** is the *car* built around that engine, with a steering wheel, seats, and dashboard so people can actually use it.

---

## Summary
- Every modern chatbot usually relies on an LLM.
- Not every LLM is automatically a chatbot — it needs an interface and purpose built around it.

# Building AI-Powered Apps with Streamlit & LangChain

## Overview
This project demonstrates how to build an interactive AI-powered application using **Streamlit** and **LangChain**, with integrations for local LLMs and web search tools.

---

## 🧩 Key Components

### Streamlit
- A Python framework for building interactive web apps quickly.
- Provides UI elements like buttons, text inputs, and outputs.
- Example: `import streamlit as st`

---

### LangChain
- A framework for building applications powered by LLMs.
- Helps connect models to external data sources and tools.
- Provides abstractions for **agents**, **chains**, and **tools**.

---

### Ollama
- A local LLM runner that allows you to run models (like LLaMA, Mistral, etc.) on your machine.
- Integrated into LangChain via:
  ```python
  from langchain_community.llms import Ollama

---

## DuckDuckGoSearchRun 
- A LangChain tool that enables web search using **DuckDuckGo**. 
- Allows agents to fetch fresh information from the internet. 
- Imported via: ```python from langchain_community.tools import DuckDuckGoSearchRun

---

# LangChain: initialize_agent

## Overview
`initialize_agent` is a core function in **LangChain** used to create an **agent**.  
Agents are decision-making systems that can use tools (like search engines, calculators, or APIs) to answer queries and perform tasks.

---

## What is an Agent?
- An agent is a controller that decides **which tool to use** and **how to use it** based on the user’s input.
- It leverages an LLM (Large Language Model) for reasoning and tool selection.
- Agents enable dynamic workflows where the model can interact with external systems.

---

## initialize_agent
- A LangChain function that sets up an agent with:
  - A list of tools (e.g., search, calculators, APIs).
  - An LLM (e.g., Ollama, OpenAI GPT).
  - An agent type (defines reasoning style and behavior).

### Example
```python
from langchain.agents import initialize_agent, AgentType
from langchain_community.llms import Ollama
from langchain_community.tools import DuckDuckGoSearchRun

# Initialize LLM
llm = Ollama(model="llama2")

# Initialize tools
search = DuckDuckGoSearchRun()

# Create agent
agent = initialize_agent(
    tools=[search],
    llm=llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)
```

---

# LangChain Components: AgentType & StreamlitCallbackHandler

## AgentType
Defines the type of agent behavior in LangChain.  
Different agent types determine how the agent interprets instructions and interacts with tools.

### Examples
- **ZERO_SHOT_REACT_DESCRIPTION**  
  - Agent decides which tool to use based on the query.  
  - Useful for one-off questions where the agent must reason and act without prior context.

- **CHAT_CONVERSATIONAL_REACT_DESCRIPTION**  
  - Agent maintains conversational context across multiple turns.  
  - Useful for chatbots or assistants that need memory of past interactions.

---

## StreamlitCallbackHandler
A callback that connects LangChain’s agent outputs to **Streamlit’s UI**.

### Features
- Displays intermediate steps in the Streamlit app.
- Shows tool usage and reasoning in real time.
- Useful for debugging and transparency when building interactive applications.

### Example Usage
```python
from langchain.callbacks import StreamlitCallbackHandler

# Create agent with Streamlit callback
agent = initialize_agent(
    tools=[search],
    llm=llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    callbacks=[StreamlitCallbackHandler()]
)
```

# LangChain Components Summary

## AgentType
Defines how the agent reasons and interacts.

### Examples
- **ZERO_SHOT_REACT_DESCRIPTION**  
  → Tool selection based on query.  
  → Best for one-off questions where the agent must decide which tool to use without prior context.

- **CHAT_CONVERSATIONAL_REACT_DESCRIPTION**  
  → Maintains conversation context.  
  → Best for chatbots or assistants that need memory of past interactions.

---

## StreamlitCallbackHandler
A callback that connects LangChain’s agent outputs to **Streamlit’s UI**.

### Features
- Displays intermediate steps in the Streamlit app.
- Shows tool usage and reasoning in real time.
- Makes the process visible and transparent.
- Useful for debugging and improving user trust.

---

## ✅ Summary
- **AgentType** defines how the agent reasons and interacts:
  - `ZERO_SHOT_REACT_DESCRIPTION` → tool selection based on query.
  - `CHAT_CONVERSATIONAL_REACT_DESCRIPTION` → maintains conversation context.
- **StreamlitCallbackHandler** connects agent reasoning to Streamlit UI, making the process visible and transparent.


---


# LLM Examples with Streamlit

A collection of practical examples demonstrating how to build applications using **Large Language Models (LLMs)** with **Streamlit**. This repository serves as a learning resource and starter kit for developers exploring LLM integration, LangChain, and AI-powered applications.

---

## **Repository Overview**

This repository contains examples to help you learn and experiment with LLM-powered applications. The apps include:

- Chatbot for real-time conversation
- File Q&A for uploading documents and asking questions
- LangChain examples for structured prompt workflows
- Integration of OpenAI APIs via Streamlit

---

## **Folder & File Structure**

| Folder/File | Purpose | Benefit | Outcome |
|-------------|---------|---------|---------|
| `.devcontainer/` | VS Code Dev Container configuration | Provides consistent development environment | Developers can run the project without local setup conflicts |
| `.github/workflows/` | GitHub Actions workflows | Automates testing, linting, or deployment | Maintains code quality and reduces errors |
| `pages/` | Streamlit Python scripts demonstrating LLM examples | Ready-to-run LLM apps | Users can experiment with chatbots, file Q&A, and LangChain examples |
| `.gitignore` | Files/folders ignored by Git | Keeps repo clean and secure | Unnecessary or sensitive files are not committed |
| `.pre-commit-config.yaml` | Pre-commit hook configuration | Enforces code style before commits | Ensures standardized and clean code |
| `.ruff.toml` | Python linter configuration | Static analysis for code issues | Catch errors early and adhere to best practices |
| `Chatbot.py` | Main interactive chatbot app | Demonstrates LLM integration | Users can ask questions and get real-time AI responses |
| `app_test.py` | Test cases for the apps | Validates functionality | Prevents regressions and ensures app stability |
| `requirements.txt` | Python packages for running apps | Simplifies environment setup | Users can install all dependencies easily |
| `requirements-dev.txt` | Python packages for development/testing | Supports contributors | Enables testing, linting, and development workflow |
| `LICENSE` | Apache-2.0 License | Legal usage and distribution terms | Protects both contributors and users |

---

# How LLMs Are Used in This Repository

This section explains how **Large Language Models (LLMs)** are integrated into the `llm-examples` repository, including their purpose, workflow, and benefits.

---

## **1️⃣ Core Concept**

LLMs are neural networks trained to understand and generate human-like text. In this repository, LLMs are used to:

- Respond to user questions (**Chatbot**)  
- Answer questions about uploaded documents (**File Q&A**)  
- Assist in structured workflows via **LangChain PromptTemplates**

The apps integrate LLMs through APIs (OpenAI models like `gpt-3.5-turbo` or `gpt-4`) in **Streamlit** applications.

---

## **2️⃣ Usage Across Examples**

### **a) Chatbot.py**
- **Purpose:** Interactive text-based chatbot.
- **How LLM is used:**  
  1. User types a message.  
  2. Streamlit app sends the message to the LLM API.  
  3. LLM generates a response.  
- **Outcome:** Real-time AI conversation.  
- **Benefits:**  
  - Quick prototyping of chatbot interface.  
  - Demonstrates LLM conversational abilities.

### **b) File Q&A Scripts (e.g., File_QA.py)**
- **Purpose:** Users can upload documents (PDF, TXT) and ask questions about them.  
- **How LLM is used:**  
  1. Uploaded file is read and converted to text.  
  2. Text is chunked and sent as context to the LLM.  
  3. User questions are sent along with relevant context.  
- **Outcome:** LLM provides answers based on the uploaded content.  
- **Benefits:**  
  - On-demand document comprehension.  
  - Practical example of knowledge extraction with LLMs.

### **c) LangChain Examples**
- **Purpose:** Demonstrates structured prompt workflows and chains.  
- **How LLM is used:**  
  - LangChain manages multi-step interactions with the LLM (PromptTemplates, reasoning chains).  
- **Outcome:** Developers learn to orchestrate LLM calls for complex tasks.  
- **Benefits:**  
  - Efficient multi-step AI workflows.  
  - Teaches best practices in prompt engineering.

---

## **3️⃣ Technical Flow of LLM Usage**

1. **User Input:** Text typed by the user or file uploaded via Streamlit.  
2. **Preprocessing:**  
   - Text cleaning  
   - Chunking large documents for File Q&A  
3. **LLM API Call:**  
   - Using OpenAI API key  
   - Sending prompt/context to model (`gpt-3.5-turbo` or `gpt-4`)  
4. **Response Handling:**  
   - LLM returns generated text  
   - Streamlit app displays response to the user

---

## **4️⃣ Benefits of Using LLMs Here**

- Real-time AI interactions with minimal setup  
- Easy to extend to tasks like summarization, translation, or question-answering  
- Educational examples for developers to learn **AI integration patterns**

---

## **5️⃣ Key Takeaways**

- LLMs are **API-driven**; no local training is required  
- Streamlit provides a **friendly UI** for interacting with LLMs  
- LangChain shows **structured prompt and chain workflows** for advanced applications

---

## **6️⃣ Installation & Run Instructions**

Follow these steps to set up and run the LLM examples locally.

### **1. Clone the Repository**

In powershell
git clone https://github.com/saisree28/llm-examples.git
cd llm-examples

### **2. Create a Virtual Environment**
python -m venv .venv
.venv\Scripts\activate

### **3. Install Dependencies**
pip install -r requirements.txt

### **4. Set Your OpenAI API Key**
$env:OPENAI_API_KEY="your_api_key_here"  
Purpose: The apps need this key to access OpenAI models like GPT-3.5 or GPT-4.

### **5. Run the Streamlit Apps**
Chatbot
- streamlit run pages/Chatbot.py

File Q&A
- streamlit run pages/File_QA.py

LangChain Quickstart
- streamlit run pages/LangChain_Quickstart.py


Open your browser at http://localhost:8501 to interact with the apps.




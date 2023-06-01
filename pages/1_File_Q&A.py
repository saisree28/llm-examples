import streamlit as st
from langchain_community.llms import Ollama
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain.chains import RetrievalQA
import tempfile
import os

st.title("📄 File Q&A (Local RAG with Ollama)")

# Initialize local LLM
llm = Ollama(model="mistral")

uploaded_file = st.file_uploader("Upload a file", type=("txt", "md"))

if uploaded_file:
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_path = tmp_file.name

    # Load document
    loader = TextLoader(temp_path)
    documents = loader.load()

    # Split into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    docs = text_splitter.split_documents(documents)

    # Create embeddings
    embeddings = OllamaEmbeddings(model="mistral")

    # Create vector store
    vectorstore = FAISS.from_documents(docs, embeddings)

    # Create RetrievalQA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(),
    )

    question = st.text_input(
        "Ask something about the document",
        placeholder="Can you give me a short summary?"
    )

    if question:
        response = qa_chain.run(question)
        st.write("### Answer")
        st.write(response)

    # Cleanup temp file
    os.remove(temp_path)
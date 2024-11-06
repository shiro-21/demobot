import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import os
from dotenv import load_dotenv


# Load environment variables
load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Streamlit App Interface
st.set_page_config(page_title="Enhanced LangChain Chatbot", page_icon="🤖")
st.title("🌐 Chatbot with LLama3")

# User prompt and prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("user", "Question: {question}")
    ]
)

# Text area for better input experience
input_text = st.text_area("Enter your question or topic:", height=100, placeholder="Type here...")

# Ollama Model and Parser
llm = Ollama(model="llama3")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Button to submit query
if st.button("Get Answer", key="submit"):
    if input_text:
        with st.spinner("Thinking..."):
            try:
                # Get the response from the model
                response = chain.invoke({"question": input_text})
                # Display response in a styled text box
                st.markdown("### 🤖 Response:")
                st.markdown(f"<div style='background-color:#f1f3f4; padding:15px; border-radius:10px;'>{response}</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error("Oops! Something went wrong. Please try again.")
    else:
        st.warning("Please enter a question or topic to proceed.")

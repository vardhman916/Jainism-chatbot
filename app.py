from langchain_google_genai import ChatGoogleGenerativeAI
# it helps to call the llm api
from langchain_core.prompts import ChatPromptTemplate
#it helps to create a prompt template
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser
# StrOutputParser() will extract and return the LLM's response as a plain
from langchain.schema.runnable import RunnableParallel
# from langchain.chains import LLMChain
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
#dot env helps to load environment variables from a .env file

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

#prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful jain philosophy assistant.You know all the things about jain philosophy.Please response to the user queries."),
        ("user", "Question:{question}"),
    ]
)
# like we telling the model to behave like this It influences tone, style, and focus.
# This is the actual user input/question.
 
 ##streamlit framework
st.title('Geo Jainism Chatbot')
input_text = st.text_input("Enter your question here:")

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.5, google_api_key=api_key)
output_parser = StrOutputParser()
chain = prompt|llm|output_parser
if input_text:
    st.write(chain.invoke({'question': input_text}))
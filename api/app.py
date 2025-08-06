from fastapi import FastAPI
from langchain_google_genai import ChatGoogleGenerativeAI
#chat model for gemini
from langchain_google_genai import ChatGoogleGenerativeAI
from langserve import add_langchain_routes
import uvicorn
import os
from langchain_community.llms import OllamaCpp
from dotenv import load_dotenv
load_dotenv()

os.environ['gemini_api'] = os.getenv("GEMINI_API_KEY") 

app = FastAPI(
    title = 'Langchain Server',
    description = "A simple API server"
)
add_routes(

    app,
    ChatGoogleGenerativeAI(model="gemini-2.0-flash"),
    path="/gemini"
)
model = ChatGoogleGenerativeAI()
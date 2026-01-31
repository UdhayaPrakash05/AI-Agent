import os
from langchain_ollama import ChatOllama
from langchain_cerebras import ChatCerebras
from dotenv import load_dotenv

load_dotenv()

ollama = False
if ollama:
    llm = ChatOllama(model="gemma3:1b")
else:
    cerebras_key = os.getenv("CEREBRAS_API_KEY")
    if not cerebras_key:
        raise ValueError("CEREBRAS_API_KEY not found in environment variables. Set it in .env or as an environment variable.")
    llm = ChatCerebras(model="gpt-oss-120b", api_key=cerebras_key)
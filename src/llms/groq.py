import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()  

class GroqLLM:
    def __init__(self):
        load_dotenv()

    def getllm(self):
        try:
            os.environ["GROQ_API_KEY"] = self.groq_api_key=os.getenv("GROQ_API_KEY")
            llm=ChatGroq(model="groq-3.5-turbo", temperature=0)
            return llm
        except Exception as e:
            print(f"Error initializing Groq LLM: {e}")
            return None

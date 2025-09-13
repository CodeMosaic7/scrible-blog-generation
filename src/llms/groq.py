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
            llm = ChatGroq(model_name="llama-3.3-70b-versatile",temperature=0.7)
            return llm
        except Exception as e:
            print(f"Error initializing Groq LLM: {e}")
            return None

import uvicorn
from fastapi import FastAPI, Request
import os
import dotenv

from graphs.graph_builder import GraphBuilder
from llms.groq import GroqLLM

dotenv.load_dotenv()

app=FastAPI(title="Blog Generation API")

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

@app.get("/check")
def check():
    return {"status":"API is running"}

@app.post("/blogs",)
async def generate_blog(request: Request):
    """Generates a blog based on the provided requirements description."""
    req_data = await request.json()  #
    description = req_data.get("description", "")
    groqllm = GroqLLM(model="gpt-4o", temperature=0.7)
    llm = groqllm.getllm()
    graph_builder = GraphBuilder(llm)
    graph = graph_builder.setup(usecase="topic")
    
    #
    initial_state = {
        "topic": req_data.get("topic", ""),  
        "keywords": req_data.get("keywords", []),
        "audience": req_data.get("audience", "")
    }
    
    result_state = graph.invoke(initial_state)
    return {"data": result_state}


if __name__=="__main__":
    uvicorn.run("app:app",host="0.0.0.0",port=8000,reload=True)
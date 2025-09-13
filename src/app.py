import uvicorn
from fastapi import FastAPI, Request, HTTPException
import os
import dotenv

from src.graphs.graph_builder import GraphBuilder
from src.llms.groq import GroqLLM
from src.states.blog import BlogState,Blog,BlogRequestNested,BlogResponse

dotenv.load_dotenv()

app=FastAPI(title="Blog Generation API")
# Environment Variables
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

# Routes
@app.get("/check")
def check():
    return {"status":"API is running"}

@app.post("/blogs", response_model=BlogResponse)
async def generate_blog(blog_request: BlogRequestNested):
    """Generates a blog based on the provided requirements description."""
    print(blog_request)
    try:
        llm=GroqLLM()
        
        
        graph_builder = GraphBuilder(llm.getllm())
        graph = graph_builder.setup(usecase="topic")
        
        initial_state = {
            "blog": "",
            "topic": blog_request.topic
            
        }
        
        result_state = graph.invoke(initial_state)
        print("Debug:",result_state)
        
        response_data: BlogState = {
            "blog": result_state["blog"],
            "topic": result_state.get("topic", blog_request.topic), 
           
        }
        
        return BlogResponse(
            data=response_data,
            status="success"
        )
        
    except Exception as e:
        print(f"Error processing request: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))



if __name__=="__main__":
    uvicorn.run("app:app",host="0.0.0.0",port=8000,reload=True)
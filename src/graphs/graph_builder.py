from langgraph.graph import StateGraph, START, END

from src.llms.groq import GroqLLM
from src.states.blog import BlogState
from src.nodes.BlogNodes import BlogNode

class GraphBuilder:
    def __init__(self, llm: GroqLLM):
        self.llm = llm
        
    def build_graph(self) -> StateGraph:
        """Builds a state graph based on the provided requirements description."""
        graph = StateGraph(BlogState)
        blog_node = BlogNode(self.llm)
        
        graph.add_node("title_creation", blog_node.title_creation)
        graph.add_node("content_generation", blog_node.content_generation)
        
        graph.add_edge(START, "title_creation")
        graph.add_edge("title_creation", "content_generation")
        graph.add_edge("content_generation", END)
        
        return graph
    
    def setup(self, usecase="topic"):
        """Setup and compile the graph for the given usecase"""
        if usecase == "topic":
            graph = self.build_graph()
            return graph.compile()
        else:
            raise ValueError(f"Unknown usecase: {usecase}")
from langgraph.graph import StateGraph, START, END

from llms.groq import GroqLLM
from states.blog import BlogState
from nodes.BlogNodes import BlogNode


class GraphBuilder:
    def __init__(self, llm: GroqLLM):
        self.llm = llm
        self.graph=StateGraph(BlogState)

    def build_graph(self, description: str) -> StateGraph:
        """Builds a state graph based on the provided requirements description."""
        # Nodes

        block_node_obj = BlogNode(self.llm)
        self.graph = StateGraph()
        self.graph.add_node("title_creation",self.block_node_obj.title_creation)
        self.graph.add_node("content_generation",self.block_node_obj.content_generation)
        # Edges
        self.graph.add_edge(START, "title_creation")
        self.graph.add_edge("title_creation", "content_generation")
        self.graph.add_edge("content_generation", END)
        return self.graph
    
    
    def setup(self,usecase):
        if usecase=="topic":
            self.build_graph()
        return self.graph.compile()

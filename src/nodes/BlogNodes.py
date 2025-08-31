from states.blog import BlogState

class BlogNode:
    """Base Class for any Blog node"""
    def __init__(self,llm):
        self.llm=llm

        def title_creation(self,state:BlogState):
            """Creates a title for the blog based on the keywords"""
            if "topic" in state or tate["topic"]:
                prompt=f"""Your are expert in writing catchy blog titles. Use Markdown format to create a title for a blog on the 
                topic {state['topic']}. The title should be engaging, SEO freindly and relevant to the topic."""
                res=self.llm.invoke(prompt)
                return {"blog":{"title":res.content}}
            else:            
                raise ValueError("Topic is required to create a title")
            
        def content_generation(self,state:BlogState):
            """Generates content for the blog based on the title and keywords"""
            if "title" in state or state["title"]:
                prompt=f"""You are expert in writing blogs. Use Markdown format to create a detailed blog content based on the title 
                {state['title']}. The content should be engaging, SEO freindly and relevant to the title."""
                res=self.llm.invoke(prompt)
                return {"blog":{"title": state['blog']['title'],"content":res.content}}
            else:            
                raise ValueError("Title is required to create content")
            



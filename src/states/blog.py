from typing import TypedDict, Optional
from pydantic import BaseModel, Field


class Blog(BaseModel):
    title: str = Field(..., description="The title of the blog post")
    content: str = Field(..., description="The content of the blog post")

class BlogState(TypedDict):
    blog: Blog
    topic: str
    # current_language: str
    
class BlogRequestNested(BaseModel):
    """Request model that matches your BlogState structure"""
    topic: str
    
class BlogResponse(BaseModel):  
    data: BlogState
    status: str = Field(..., description="Status of the blog generation process")


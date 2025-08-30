from typing import TypedDict
from pydantic import BaseModel, Field


class Blog(BaseModel):
    title: str = Field(..., description="The title of the blog post")
    content: str = Field(..., description="The content of the blog post") #... show that content and title are required fields


class BlogState(TypedDict):
    blog: Blog
    topic: str
    keywords: list[str]
    audience: str
    tone: str
    title: str
    outline: str
    draft: str
    edited_draft: str
    seo_keywords: list[str]
    meta_description: str
    images: list[str]
    published: bool
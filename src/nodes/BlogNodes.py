from src.states.blog import BlogState, Blog

class BlogNode:
    
    def __init__(self, llm):
        self.llm = llm
    
    def title_creation(self, state: BlogState) -> BlogState:
        """Create a title for the blog based on the keywords"""        
        try:
            if "topic" not in state:
                raise ValueError("State missing 'topic' field")
            
            if not state["topic"] or not state["topic"].strip():
                raise ValueError("Topic cannot be empty")
            
            topic = state["topic"].strip()
            
            prompt = f"""You are an expert in writing catchy blog titles. Create a compelling, SEO-friendly title for a blog about: {topic}

Requirements:
- Make it engaging and clickable
- Keep it under 60 characters for SEO
- Make it relevant to the topic
- Use proper capitalization
- Do not include markdown formatting in the title itself

Topic: {topic}

Generate only the title, nothing else:"""

            res = self.llm.invoke(prompt)            
            # The fix: res is an AIMessage object, so we access res.content directly
            generated_title = res.content.strip()  
            generated_title = generated_title.replace('#', '').replace('*', '').replace('"', '').strip()
            
            print(f"Generated title: {generated_title}")
            
            current_blog = state["blog"]
            updated_blog = Blog(
                title=generated_title,
                content=current_blog.content if current_blog else ""
            )
            
            # Return updated state
            updated_state = dict(state)  # Create a copy
            updated_state["blog"] = updated_blog
            
            print(f"Title creation completed successfully")
            return updated_state
            
        except Exception as e:
            print(f"Error in title_creation: {e}")
            import traceback
            traceback.print_exc()
            raise
    
    def content_generation(self, state: BlogState) -> BlogState:
        """Generates content for the blog based on the title and keywords"""
        print(f"content_generation called with state keys: {state.keys()}")
        
        try:
            # Validate input
            if "blog" not in state:
                raise ValueError("State missing 'blog' field")
            
            blog = state["blog"]
            if not blog or not blog.title or not blog.title.strip():
                raise ValueError("Blog title is required to generate content")
            
            title = blog.title.strip()
            topic = state.get("topic", "")
            audience = state.get("audience", "general readers")
            
            print(f"Generating content for title: {title}")
            
            prompt = f"""You are an expert blog writer. Create comprehensive, engaging blog content based on the following:

Title: {title}
Topic: {topic}
Target Audience: {audience}

Requirements:
- Write in Markdown format
- Create a well-structured article with proper headings
- Make it SEO-friendly and engaging
- Include an introduction, main content sections, and conclusion
- Aim for 800-1200 words
- Use bullet points, numbered lists where appropriate
- Make it informative and valuable for readers

Generate the complete blog content:"""

            res = self.llm.invoke(prompt)
            print(f"Content generation LLM response type: {type(res)}")
            
            generated_content = res.content.strip() 
                        
            updated_blog = Blog(
                title=blog.title,
                content=generated_content
            )
            
            updated_state = dict(state)  
            updated_state["blog"] = updated_blog
            
            print(f"Content generation completed successfully")
            return updated_state
            
        except Exception as e:
            print(f"Error in content_generation: {e}")
            import traceback
            traceback.print_exc()
            raise
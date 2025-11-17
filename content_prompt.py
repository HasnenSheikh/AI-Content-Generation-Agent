from langchain_core.prompts import PromptTemplate

content_prompt = PromptTemplate.from_template("""
Write a {format} on the topic: "{topic}"  
Audience: {audience}  
Tone: {tone}  
Word count target: {length} words

Make it engaging, relevant, and well-structured.
""")

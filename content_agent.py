import os
from groq import Groq
from content_prompt import content_prompt

DEFAULT_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

def generate_content(topic, audience, format, tone, length, model: str | None = None):
    
    model = model or DEFAULT_MODEL

    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY environment variable not set")

    client = Groq(api_key=api_key)

    prompt_text = content_prompt.format(
        topic=topic,
        audience=audience,
        format=format,
        tone=tone,
        length=length
    )

    completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful and a creative content-writing assistant."},
            {"role": "user", "content": prompt_text}
        ],
        model=model,
        temperature=0.6,
        max_tokens=800
    )

    return completion.choices[0].message.content

import streamlit as st
from content_agent import generate_content

st.title("✍️ AI Content Generation Agent")

topic = st.text_input("Enter topic:", "AI in healthcare")
audience = st.text_input("Target audience:", "healthcare executives")
format = st.selectbox("Content format:", ["Blog Post", "LinkedIn Post", "Email", "Product Description"])
tone = st.selectbox("Tone:", ["Professional", "Conversational", "Witty", "Urgent"])
length = st.slider("Word count target:", 50, 1000, 300)

if st.button("Generate Content"):
    content = generate_content(topic, audience, format, tone, length)
    st.subheader("📝 Generated Content")
    st.text_area("Content", content, height=400)
    st.download_button("Download as .txt", content, file_name="content.txt")
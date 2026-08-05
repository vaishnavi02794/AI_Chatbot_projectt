import streamlit as st
from google import genai

client = genai.Client(
    client = genai.Client(
    api_key=st.secrets["GOOGLE_API_KEY"],
    vertexai=False
),
   

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 AI Chatbot")

prompt = st.chat_input("Type your message")

if prompt:
    st.write("You:", prompt)

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    st.write("Bot:", response.text)
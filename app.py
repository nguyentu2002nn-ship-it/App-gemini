import streamlit as st
import google.generativeai as genai

# 1. Cấu hình
st.set_page_config(page_title="My AI App", layout="centered")

# 2. API Key (Thay key của bạn vào đây)
API_KEY = "AIzaSyAGUG8S8AHmtfd8902Ghs4xTupNI8Gpyqc"
genai.configure(api_key=API_KEY)

# 3. Thiết lập Model & System Instruction
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="Bạn là một trợ lý thông minh." # Thay đổi nội dung này theo ý bạn
)

# 4. Giao diện Chat
st.title("🤖 My Custom AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Hỏi tôi điều gì đó..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = model.generate_content(prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})

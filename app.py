import streamlit as st
from google import genai

# 1. Cấu hình giao diện
st.set_page_config(page_title="My AI App", layout="centered")

# 2. Nhập API Key (Hãy đảm bảo Key nằm trong dấu ngoặc kép)
API_KEY = "AIzaSyC0X_zaicRUrboJjDqCoPTx8O72JPHJ3Yo"

# Khởi tạo Client theo chuẩn mới 2026
client = genai.Client(api_key=API_KEY)

# 3. Giao diện chính
st.title("🤖 My Custom AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Hiển thị lịch sử chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Xử lý chat
if prompt := st.chat_input("Hỏi tôi điều gì đó..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Gọi model gemini-2.0-flash mới nhất
            response = client.models.generate_content(
                model="gemini-2.0-flash", 
                contents=prompt,
                config={'system_instruction': "Bạn là một trợ lý ảo thông minh và thân thiện."}
            )
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Đã xảy ra lỗi: {e}")



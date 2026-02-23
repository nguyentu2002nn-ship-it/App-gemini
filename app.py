import streamlit as st
import google.generativeai as genai

# 1. Cấu hình giao diện Mobile-first
st.set_page_config(page_title="My AI App", page_icon="🤖", layout="centered")

# Nhãn dán tùy chỉnh CSS để giao diện giống App điện thoại
st.markdown("""
    <style>
    .main { max-width: 500px; margin: 0 auto; }
    .stChatMessage { border-radius: 15px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_config=True)

# 2. Thiết lập API (Thay API Key của bạn vào đây)
API_KEY = "AIzaSyAGUG8S8AHmtfd89O2Ghs4xTupNI8Gpyqc"
SYSTEM_INSTRUCTION = "gemini-1.5-flash"

if API_KEY == "gemini-1.5-flash":
    st.error("⚠️ Bạn chưa điền API Key vào code!")
else:
    genai.configure(api_key=API_KEY)
    
    # Cấu hình Model
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction=SYSTEM_INSTRUCTION
    )

    # 3. Quản lý lịch sử chat
    if "messages" not in st.session_state:
        st.session_state.messages = []

    st.title("📱 My Custom AI")
    st.caption("Ứng dụng chạy trên nền tảng Gemini Flash 1.5")

    # Hiển thị các tin nhắn cũ
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 4. Xử lý nhập liệu
    if prompt := st.chat_input("Hỏi tôi điều gì đó..."):
        # Lưu tin nhắn người dùng
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Gọi AI phản hồi
        with st.chat_message("assistant"):
            with st.spinner("Đang suy nghĩ..."):
                try:
                    # Gửi toàn bộ lịch sử để AI nhớ ngữ cảnh
                    response = model.generate_content(prompt)
                    ai_text = response.text
                    st.markdown(ai_text)
                    st.session_state.messages.append({"role": "assistant", "content": ai_text})
                except Exception as e:
                    st.error(f"Lỗi API: {e}")

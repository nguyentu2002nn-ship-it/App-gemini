import streamlit as st
import google.generativeai as genai

# Cấu hình giao diện Mobile-friendly
st.set_page_config(page_title="My AI App", page_icon="📱")

# Nhập API Key của bạn
API_KEY = "AIzaSyAGUG8S8AHmtfd89O2Ghs4xTupNI8Gpyqc"

# Thiết lập System Instruction từ App của bạn
SYSTEM_INSTRUCTION = """
Dán nội dung 'System Instruction' từ Google AI Studio của bạn vào đây
"""

if API_KEY == "AIzaSyAGUG8S8AHmtfd89O2Ghs4xTupNI8Gpyqc":
    st.error("Vui lòng nhập API Key để ứng dụng hoạt động!")
else:
    genai.configure(api_key=API_KEY)
    
    # Cấu hình Model với System Instruction
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction=SYSTEM_INSTRUCTION
    )

    if "chat_session" not in st.session_state:
        st.session_state.chat_session = model.start_chat(history=[])

    st.title("My Custom AI")

    # Hiển thị tin nhắn
    for message in st.session_state.chat_session.history:
        with st.chat_message("user" if message.role == "user" else "assistant"):
            st.markdown(message.parts[0].text)

    # Ô nhập liệu ở dưới cùng màn hình
    if prompt := st.chat_input("Nhập câu hỏi..."):
        with st.chat_message("user"):
            st.markdown(prompt)
        
        response = st.session_state.chat_session.send_message(prompt)
        
        with st.chat_message("assistant"):
            st.markdown(response.text)
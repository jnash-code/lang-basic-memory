# สิ่งที่ได้เรียนรู้ภายใน repo นี้
## 1.
ให้
```
ret = StreamlitChatMessageHistory(key="chat_messages")
```
จะได้ว่า
`st.session_state.chat_messages` เหมือน `ret.messages`

## 2.
การ include/exclude ชื่อ package ออกจาก requirements.txt จะมีผล กับ application บน streamlit cloud เท่านั้น ไม่เกี่ยวกับเวลารันใน Simple Browser ของ codespace

ถ้าจะให้ import package ใน codespace ได้ ต้อง pip install <pkg-name> ใน terminal เอา

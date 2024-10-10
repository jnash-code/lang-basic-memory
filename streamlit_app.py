import streamlit as st

"๋Just edited branch 2 a moment ago"

from langchain_community.chat_message_histories import (
    StreamlitChatMessageHistory,
)

history = StreamlitChatMessageHistory(key="chat_messages")

history.add_user_message("hi!")
history.add_ai_message("whats up?")


"From returned variable"
history.messages

"From session_state"
st.session_state.chat_messages
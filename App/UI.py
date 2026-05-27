import streamlit as st

st.title("Xerloks Rouses")
st.chat_input()
with st.chat_message("user"):
    st.write("Hello! How can I help you today?")
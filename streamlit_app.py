import streamlit as st

st.title("Echo bot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.chat_message(message["role"]).markdown(message["content"])

prompt = st.chat_input("Say something :D")
if prompt:
    st.chat_message("user").markdown(prompt)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

if prompt:
    response = """Why hello there!
    Let me repeat what you just said:\n""" + prompt

    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )


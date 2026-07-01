import streamlit as st

st.title("Echo bot")

# set up chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# display chat history thus far
for message in st.session_state.messages:
    st.chat_message(message["role"]).markdown(message["content"])

prompt = st.chat_input("Say something :D")
if (prompt != None): # if the user hits send with nonempty prompt
    # display the prompt as a user-sent chat message
    st.chat_message("user").markdown(prompt)

    # store in chat history
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # formulate response
    response = """Why hello there!
    Let me repeat what you just said:\n""" + prompt

    # display response as assistant-sent chat message
    st.chat_message("assistant").markdown(response)

    # also store in chat history
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )


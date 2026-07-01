import streamlit as st
# note to self:
# - the entire script is rerun after every interaction!
# - only data in st.session_state still exists between reruns

import os
# from llama_index.core.workflow import Context
from llama_index.core import load_index_from_storage, StorageContext
from llama_index.llms.google_genai import GoogleGenAI
from google.genai.errors import APIError, ClientError

st.title("Echo bot")

# set up chat history if not already (if first run)
if "messages" not in st.session_state:
    st.session_state.messages = []

# display chat history thus far
for message in st.session_state.messages:
    st.chat_message(message["role"]).markdown(message["content"])

# set up sidebar
canceled = """byok_radio = st.sidebar.radio(
    "Choose API key",
    ("Use from secrets.toml", "Use your own")
)
"""
API_KEY = st.sidebar.text_input(
    label="Enter Gemini API key",
    value=""
)

MODEL_NAME = st.sidebar.radio(
    "Choose model",
    ("gemini-3.5-flash", "gemini-3.1-flash-lite")
)

# well, you can switch LLMs, so yes this is rerun...
llm_connect_success = False
response = ""
if (API_KEY != ""):
    st.session_state.llm = GoogleGenAI(
        model=MODEL_NAME,
        api_key=API_KEY
    )
    client = st.session_state.llm._client
    try:
        client.models.list(config={"page_size": 1})
    except APIError as e:
        response = f"Invalid API key:\n{e}"
        # llm_connect_success = False
    except Exception as e:
        response = f"Unexpected error:\n{e}"
        # llm_connect_success = False
    else:
        llm_connect_success = True

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
    if response == "":
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


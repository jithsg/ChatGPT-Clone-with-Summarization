import os
import openai
import tiktoken
import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv
from langchain import OpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import (ConversationBufferMemory, 
                                                  ConversationSummaryMemory, 
                                                  ConversationBufferWindowMemory
                                                  )

from langchain.memory import ConversationTokenBufferMemory

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = openai_api_key


def getresponse(userInput):
    llm = OpenAI(
        temperature=0,
        model_name='text-davinci-003'  #we can also use 'gpt-3.5-turbo'
    )
    conversation = ConversationChain(
        llm=llm,
        verbose=True,
        memory=ConversationBufferMemory()
    )

    conversation("Good morning AI!")
    conversation("My name is sharath!")
    conversation("I am a software engineer!")
    print(conversation.memory.buffer)
    response = conversation.predict(input="What is my name")
    return response

st.set_page_config(page_title="Chat GPT Clone", page_icon=":robot_face:")
st.markdown("<h1 style='text-align: center;'>How can I assist you? </h1>", unsafe_allow_html=True)

st.sidebar.title("😎")
api_key = st.sidebar.text_input("What's your API key?",type="password")
summarise_button = st.sidebar.button("Summarise the conversation", key="summarise")
if summarise_button:
    summarise_placeholder = st.sidebar.write("Nice chatting with you my friend ❤️:\n\n + 'Hello Friend'")
    #summarise_placeholder.write("Nice chatting with you my friend ❤️:\n\n"+st.session_state['conversation'].memory.buffer)

response_container = st.container()
# Here we will have a container for user input text box
container = st.container()

with container:
    with st.form(key='my_form', clear_on_submit=True):
        user_input = st.text_area("Your question goes here:", key='input', height=100)
        submit_button = st.form_submit_button(label='Send')
        if submit_button:
            answer = getresponse(user_input)
            with response_container:
                st.write(answer)
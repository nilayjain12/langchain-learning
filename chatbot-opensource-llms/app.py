# importing the necessary libraries
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# initializing the prompt
prompt = PromptTemplate(
    input_variables=["question"],  # Must define input variables
        template="""
        <|system|>
        You are a helpful assistant that answers any user questions in a simple, readable language.
        </s>
        <|user|>
        Question: {question}
        </s>
        <|assistant|>
        """
)

# initialize the streamlit app
st.title("Langchain Chatbot with Ollama")
intput_text = st.text_input("Enter your query...")

# calling Ollama open source model
llm = Ollama(model="tinyllama")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if intput_text:
    response = chain.invoke({"question": intput_text})
    st.write(response)
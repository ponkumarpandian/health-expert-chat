import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
 
load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGSMITH_API_KEY"]=os.getenv("LANGSMITH_API_KEY")
 
model1=ChatOpenAI(model="gpt-4o-mini",temperature=0.5)
 
from langchain_core.prompts import ChatPromptTemplate
 
prompt=ChatPromptTemplate.from_messages([
 
    ("system","you are an health expert please answer user queries accordingly, if user is asking queries which are not related to health then just say please ask health related queries"),
    ("user","Question:{question}")
])
 
parser=StrOutputParser()
 
chain= prompt | model1 | parser
 
st.title("Health Expert")
input_text=st.text_input(" Ask health queries")
 
if input_text:
    st.write(chain.invoke({'question':input_text}))
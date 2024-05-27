import streamlit as st
import random
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

openai_api_key = st.secrets["openai_key"]
llm = ChatOpenAI(api_key=openai_api_key, model="gpt-4o")
random_number = random.randint(0,1)

st.title("Turing Test")
st.subheader("Mensch vs KI - erkennst du den Unterschied?")

question = st.text_input("Frage/Prompt")
human_text = st.text_area("Deine Antwort:")
prompt = f"Du beantwortest Fragen und Prompts in sehr menschenähnlichem Stil. Halte dich eher kurz und schreibe nicht zu formal, sondern wie man in einer Unterhaltung sprechen würde. Antworte auf diesen prompt: {question}"
if st.button("Generiere Antwort"):
    with st.spinner("Antworten werden bereitgestellt..."):
        ai_text = llm.invoke([HumanMessage(content=prompt)]).content
        l, r = st.columns(2)
        with l:
            if random_number == 0:
                st.info(human_text)
            else:
                st.info(ai_text)


        with r:
            if random_number == 1:
                st.info(human_text)
            else:
                st.info(ai_text)
        
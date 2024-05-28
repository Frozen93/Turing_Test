import streamlit as st
import random
import time
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

openai_api_key = st.secrets["openai_key"]
llm = ChatOpenAI(api_key=openai_api_key, model="gpt-4o")
random_number = random.randint(0,1)

if "score" not in st.session_state:
    st.session_state.score = 0

@st.experimental_fragment
def decision_fragment():
    decision = st.selectbox("Mensch oder KI?", ["-", "Mensch", "KI"])
    if decision == "-":
        st.markdown("Von wem stammt der linke Text?")
    elif decision == "Mensch" and random_number==0:
        st.markdown("**Richtig!**")
        time.sleep(1)
        st.session_state["score"] += 1
        st.rerun()
    elif decision == "KI" and random_number == 1:
        st.markdown("**Richtig!**")
        time.sleep(1)
        st.session_state["score"] += 1
        time.sleep(1)
        st.rerun()
    else: 
        st.markdown("**Das stimmt leider nicht!**")
        st.rerun()

st.title("Turing Test")
st.subheader("Mensch vs KI - erkennst du den Unterschied?")

question = st.text_input("Frage/Prompt")
human_text = st.text_input("Deine Antwort:", type="password")
prompt = f"Du beantwortest Fragen und Prompts in sehr menschenähnlichem Stil. Erwähne möglichst NICHT, dass du GPT oder ein Spraschmodell bist. Gestalte den Stil und die Länge des textes möglichst genau wie in dieser Beispielantwort: {human_text}. Antworte auf diesen prompt: {question}"
if st.button("Generiere Antwort"):
    with st.spinner("Antworten werden bereitgestellt..."):
        ai_text = llm.invoke([HumanMessage(content=prompt)]).content
        l, r = st.columns(2)
        with l:
            if random_number == 0:
                st.info(human_text)
            else:
                st.info(ai_text)
            decision_fragment()

        with r:
            if random_number == 1:
                st.info(human_text)
            else:
                st.info(ai_text)
st.markdown(f"**Deine Punktzahl ist: {st.session_state['score']}**")    
        

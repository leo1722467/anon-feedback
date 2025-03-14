import streamlit as st
import database
import hashlib

# Garantir que o usuário esteja autenticado
if "user" not in st.session_state:
    st.warning("Você precisa fazer login para acessar esta página.")
    st.switch_page("pages/2_Login.py")

st.title("💬 Enviar Feedback Anônimo")

feedback_text = st.text_area("Digite seu feedback:")

if st.button("Enviar"):
    if feedback_text:
        user_hash = hashlib.sha256(st.session_state["user"].encode()).hexdigest()
        database.save_feedback(user_hash, feedback_text)
        st.success("Feedback enviado com sucesso!")

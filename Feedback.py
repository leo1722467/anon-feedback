import streamlit as st
import firebase
import hashlib

def show_feedback_page():
    # A linha abaixo é removida ou comentada
    # st.set_page_config(page_title="💬 Enviar Feedback Anônimo", page_icon="🔒", layout="wide")

    if "user" not in st.session_state:
        st.error("Você precisa estar logado para enviar feedbacks!")
        return

    user_hash = hashlib.sha256(st.session_state["user"].encode()).hexdigest()
    
    feedback_text = st.text_area("Digite seu feedback:")
    
    if st.button("Enviar"):
        if feedback_text:
            if firebase.check_duplicate_feedback(user_hash, feedback_text):
                st.warning("❗ Você já enviou esse mesmo feedback recentemente!")
            else:
                firebase.save_feedback(user_hash, feedback_text)
                st.success("✅ Feedback enviado com sucesso!")

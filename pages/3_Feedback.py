import streamlit as st
import database
import hashlib

st.title("💬 Enviar Feedback Anônimo")

if "user" not in st.session_state:
    st.error("Você precisa estar logado para enviar feedbacks!")
else:
    user_hash = hashlib.sha256(st.session_state["user"].encode()).hexdigest()
    
    feedback_text = st.text_area("Digite seu feedback:")

    if st.button("Enviar"):
        if feedback_text:
            # Verificar se já existe um feedback idêntico no banco
            if database.check_duplicate_feedback(user_hash, feedback_text):
                st.warning("❗ Você já enviou esse mesmo feedback recentemente!")
            else:
                database.save_feedback(user_hash, feedback_text)
                st.success("✅ Feedback enviado com sucesso!")

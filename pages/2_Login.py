import streamlit as st
import database
import time

st.title("🔑 Login")

username = st.text_input("Usuário")
password = st.text_input("Senha", type="password")

if st.button("Entrar"):
    if database.check_login(username, password):
        st.session_state["user"] = username
        st.success("Login realizado com sucesso! Redirecionando para a página de feedbacks...")

        time.sleep(2)  # Espera 2 segundos antes de redirecionar
        st.switch_page("pages/3_Feedback.py")  # Redireciona para a página de feedbacks
    else:
        st.error("Usuário ou senha incorretos!")

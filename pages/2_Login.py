# No início do seu script principal ou arquivo específico
import streamlit as st
import firebase

# Configuração global da página - chamada uma vez no início
st.set_page_config(page_title="Feedback App", page_icon="🔒", layout="wide")

# Restante do seu código
import Feedback

if "user" not in st.session_state:
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if firebase.check_login(username, password):
            st.session_state["user"] = username
            st.success("Login realizado com sucesso!")
            Feedback.show_feedback_page()  # Supõe que esta função não chame set_page_config
        else:
            st.error("Usuário ou senha incorretos!")
else:
    Feedback.show_feedback_page()  # Exibe a página de feedback se já logado

import streamlit as st
import firebase

st.title("🔒 Cadastro de Usuário (Apenas para Administradores)")

# Verificar se o admin já está logado
if "admin_logged_in" not in st.session_state:
    st.session_state["admin_logged_in"] = False

ADMIN_PASSWORD = st.secrets["ADMIN_PASSWORD"]

# Formulário de login do administrador
if not st.session_state["admin_logged_in"]:
    admin_input = st.text_input("Digite a senha do Administrador", type="password")
    if st.button("Entrar como Admin"):
        if admin_input == ADMIN_PASSWORD:
            st.session_state["admin_logged_in"] = True
            st.success("Acesso concedido! Você pode cadastrar novos usuários.")
            st.rerun()
        else:
            st.error("Senha incorreta!")

# Se o admin estiver logado, exibir o formulário de cadastro
if st.session_state["admin_logged_in"]:
    username = st.text_input("Novo Usuário")
    password = st.text_input("Senha do Novo Usuário", type="password")

    if st.button("Cadastrar Usuário"):
        if username and password:
            success = firebase.add_user(username, password)
            if success:
                st.success("Usuário cadastrado com sucesso!")
            else:
                st.error("Usuário já existe!")

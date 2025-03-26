import streamlit as st
import firebase
import pandas as pd
import os

st.title("🔒 Painel do Administrador")

ADMIN_PASSWORD = st.secrets["ADMIN_PASSWORD"]

admin_login = st.text_input("Senha do Administrador", type="password")

if admin_login == ADMIN_PASSWORD:
    feedbacks = firebase.get_feedbacks()  # Mudança para buscar feedbacks do Firebase

    if feedbacks:
        # Preparar os dados para o DataFrame
        data = {
            "Feedback": [fb['feedback'] for fb in feedbacks],
            "Timestamp": [fb['timestamp'] for fb in feedbacks],
            "User Hash": [fb['user_hash'] for fb in feedbacks]
        }

        # Criar o DataFrame
        df = pd.DataFrame(data)

        # Exibir o DataFrame no Streamlit
        st.dataframe(df)
    else:
        st.error("Nenhum feedback encontrado!")

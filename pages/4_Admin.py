import streamlit as st
import database
import pandas as pd
import os

st.title("🔒 Painel do Administrador")


ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin123")

admin_login = st.text_input("Senha do Administrador", type="password")

if admin_login == ADMIN_PASSWORD:
    feedbacks = database.get_feedbacks()
    
    df = pd.DataFrame(feedbacks, columns=["ID", "User Hash", "Feedback", "Data"])
    st.dataframe(df)
else:
    st.error("Acesso Negado!")

import streamlit as st

st.set_page_config(page_title="Anon Feedback", page_icon="💬", layout="centered")

st.title("📢 Anon Feedback")
st.write("Bem-vindo ao sistema de feedbacks anônimos!")

st.sidebar.success("Selecione uma página acima para navegar.")

# Esconder a página de feedbacks removendo-a da navegação

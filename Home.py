import streamlit as st
HOME_TEXT = st.secrets["HOME_TEXT"]
IMG_URL = st.secrets["IMG_URL"]

# Configuração da página para ocupar toda a largura
st.set_page_config(
    page_title="Anon Feedback",
    page_icon="💬",
    layout="wide"  # Usa toda a largura da tela
)

# Estilização da página para fundo azul-marinho e texto branco
st.markdown(
    """
    <style>
        .stApp {
            background-color: white;
        }
        h1, h2, h3, h4, h5, h6, p, div {
            color: black !important;
        }
        .stMarkdown {
            color: black !important;
            align: center;
        }
        .main-content {
            max-width: auto;
            margin: auto;
            padding: 10px;
        }
        .stImage {
            display: flex;
            justify-content: center;
        }
        .stTitle {
            max-width: auto;
            margin: auto;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Centralizando conteúdo na largura total da tela
with st.container():
    st.image(IMG_URL, width=250)

    st.title("📢 Bem-vindo ao Canal de Relatos Psicossociais")

    st.markdown(
        HOME_TEXT,
        unsafe_allow_html=True
    )

# Barra lateral
st.sidebar.success("Selecione uma página acima para navegar.")

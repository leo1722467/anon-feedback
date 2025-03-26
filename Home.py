import streamlit as st

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
    st.image("https://samserv.com.br/img/logo.png", width=250)

    st.title("📢 Bem-vindo ao Canal de Relatos Psicossociais")

    st.markdown(
        """
        <div class="main-content">
            <p style="font-size:18px; line-height:1.6; color:white; text-align:justify;">
            A <b>Samserv</b> valoriza o bem-estar e a saúde mental de todos os colaboradores. Para reforçar esse compromisso, criamos este espaço dedicado ao relato de situações que possam impactar o ambiente de trabalho sob a perspectiva psicossocial.
            <br><br>
            Aqui, você pode compartilhar de forma segura e confidencial experiências relacionadas a <b>pressões excessivas, assédio moral, terrorismo psicológico, discriminação, dificuldades na conciliação entre vida profissional e pessoal</b>, além de outros fatores que possam comprometer sua saúde emocional e o clima organizacional.
            <br><br>
            <b>Seu feedback é essencial</b> para que possamos identificar e tratar essas questões, promovendo um ambiente de trabalho mais saudável, respeitoso e produtivo para todos.
            <br><br>
            Fique à vontade para relatar sua experiência de maneira objetiva e sincera. Suas informações serão tratadas com <b>seriedade e discrição</b>.
            <br><br>
            <b>Juntos, podemos construir um ambiente de trabalho mais equilibrado e acolhedor.</b>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Barra lateral
st.sidebar.success("Selecione uma página acima para navegar.")

import firebase_admin
from firebase_admin import credentials, firestore
import streamlit as st
import json

# Carregar credenciais do secrets.toml
firebase_secrets = st.secrets["firebase"]

# Converter os dados do secrets.toml para um dicionário JSON
cred_dict = {
    "type": firebase_secrets["type"],
    "project_id": firebase_secrets["project_id"],
    "private_key_id": firebase_secrets["private_key_id"],
    "private_key": firebase_secrets["private_key"].replace("\\n", "\n"),
    "client_email": firebase_secrets["client_email"],
    "client_id": firebase_secrets["client_id"],
    "auth_uri": firebase_secrets["auth_uri"],
    "token_uri": firebase_secrets["token_uri"],
    "auth_provider_x509_cert_url": firebase_secrets["auth_provider_x509_cert_url"],
    "client_x509_cert_url": firebase_secrets["client_x509_cert_url"],
}

# Inicializar Firebase apenas se ainda não estiver inicializado
if not firebase_admin._apps:
    cred = credentials.Certificate(cred_dict)
    firebase_admin.initialize_app(cred)

# Criar cliente do Firestore
db = firestore.client()

# Supondo que você tenha uma função add_user em firebase.py
import firebase
import time


# username = "teste_usuario"
# password = "senha_segura"
# if firebase.add_user(username, password):
#     print("Usuário criado com sucesso!")
# else:
#     print("Falha ao criar usuário ou usuário já existe.")

# time.sleep(2)

# if firebase.check_login(username, password):
#     print("Login bem-sucedido!")
# else:
#     print("Falha no login. Verifique usuário e senha.")

# time.sleep(2)

# feedback = "Este é um feedback de teste."
# if firebase.save_feedback(username, feedback):
#     print("Feedback enviado com sucesso!")
# else:
#     print("Falha ao enviar feedback.")

# time.sleep(2)

feedbacks = firebase.get_feedbacks()
for fb in feedbacks:
    print(fb)


import pandas as pd
import streamlit as st

# Suponha que 'feedbacks' seja a lista de dicionários que você mostrou no exemplo
feedbacks = firebase.get_feedbacks()

# Verificar se feedbacks não está vazio
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
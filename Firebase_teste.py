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

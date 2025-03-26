from firebase_config import db
import bcrypt
from firebase_admin import firestore
import hashlib

def add_user(username, password):
    # Criar um hash SHA-256 do nome de usuário
    username_hash = hashlib.sha256(username.encode()).hexdigest()
    users_ref = db.collection("users").document(username_hash)

    # Verifica se o usuário já existe
    if users_ref.get().exists:
        return False  # Usuário já existe

    # Criptografa a senha
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    # Salva no Firestore
    users_ref.set({"password": hashed_password})
    return True

def check_login(username, password):
    username_hash = hashlib.sha256(username.encode()).hexdigest()
    users_ref = db.collection("users").document(username_hash)
    user_doc = users_ref.get()

    if not user_doc.exists:
        return False  # Usuário não encontrado

    stored_password = user_doc.to_dict().get("password")

    # Verifica a senha
    if bcrypt.checkpw(password.encode(), stored_password.encode()):
        return True
    return False


# Salvar feedback no Firestore
def save_feedback(user_hash, feedback_text):
    feedback_ref = db.collection("feedbacks").document()
    feedback_ref.set({
        "feedback": feedback_text,
        "timestamp": firestore.SERVER_TIMESTAMP,
        "user_hash": user_hash  # Mantém o anonimato do usuário
    })
    return True

# Obter todos os feedbacks
def get_feedbacks():
    feedbacks_ref = db.collection("feedbacks")
    feedbacks = feedbacks_ref.order_by("timestamp", direction=firestore.Query.DESCENDING).stream()
    all_feedbacks = [{"feedback": fb.to_dict()["feedback"], "timestamp": fb.to_dict().get("timestamp"), "user_hash": fb.to_dict().get("user_hash")} for fb in feedbacks]
    return all_feedbacks


# Verificar feedback duplicado
def check_duplicate_feedback(user_hash, feedback_text):
    feedbacks_ref = db.collection("feedbacks")
    # Buscar feedbacks com o mesmo texto e hash de usuário
    feedbacks = feedbacks_ref.where("feedback", "==", feedback_text).where("user_hash", "==", user_hash).stream()

    return any(feedbacks)  # Retorna True se encontrar um feedback idêntico

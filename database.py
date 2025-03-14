import sqlite3
import os
import bcrypt

# Caminho do banco de dados
DB_PATH = os.path.join(os.path.dirname(__file__), "feedbacks.db")

# Função para conectar ao banco
def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

# Função para criar as tabelas se não existirem
def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Criar tabela de usuários
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)
    
    # Criar tabela de feedbacks
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS feedbacks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_hash TEXT NOT NULL,
        feedback TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    conn.commit()
    conn.close()

# Função para adicionar um novo usuário
def add_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        conn.close()
        return True
    except:
        conn.close()
        return False  # Retorna False se o usuário já existir

# Função para verificar login
def check_login(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    
    conn.close()
    
    if user and bcrypt.checkpw(password.encode(), user[0]):
        return True
    return False

# Função para salvar feedback
def save_feedback(user_hash, feedback):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO feedbacks (user_hash, feedback) VALUES (?, ?)", (user_hash, feedback))
    
    conn.commit()
    conn.close()

# Função para obter feedbacks
def get_feedbacks():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM feedbacks")
    feedbacks = cursor.fetchall()
    
    conn.close()
    return feedbacks

# Inicializar o banco de dados ao importar este arquivo
init_db()

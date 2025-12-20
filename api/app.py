from flask import Flask, request, jsonify
import sqlite3
import subprocess
import hashlib
import os
import re

app = Flask(__name__)

# 🔐 Secret récupéré depuis une variable d’environnement
SECRET_KEY = os.environ.get("SECRET_KEY", "default-secret")

# -------------------------------
# Connexion base de données
# -------------------------------
def get_db():
    return sqlite3.connect("users.db")

# -------------------------------
# LOGIN sécurisé (anti SQL injection)
# -------------------------------
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    hashed_pwd = hashlib.sha256(password.encode()).hexdigest()

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, hashed_pwd)
    )
    result = cursor.fetchone()

    if result:
        return jsonify(status="success", user=username)

    return jsonify(status="error", message="Invalid credentials"), 401

# -------------------------------
# PING sécurisé (pas de shell=True)
# -------------------------------
@app.route("/ping", methods=["POST"])
def ping():
    host = request.json.get("host", "")

    if not re.match(r"^[a-zA-Z0-9.-]+$", host):
        return jsonify(error="Invalid host"), 400

    result = subprocess.run(
        ["ping", "-c", "1", host],
        capture_output=True,
        text=True
    )

    return jsonify(output=result.stdout)

# -------------------------------
# COMPUTE sécurisé (pas de eval)
# -------------------------------
@app.route("/compute", methods=["POST"])
def compute():
    data = request.get_json()
    a = data.get("a", 0)
    b = data.get("b", 0)

    return jsonify(result=a + b)

# -------------------------------
# HASH sécurisé (SHA-256)
# -------------------------------
@app.route("/hash", methods=["POST"])
def hash_password():
    pwd = request.json.get("password", "")
    hashed = hashlib.sha256(pwd.encode()).hexdigest()
    return jsonify(sha256=hashed)

# -------------------------------
# Lecture fichier sécurisée
# -------------------------------
@app.route("/readfile", methods=["POST"])
def readfile():
    filename = request.json.get("filename", "")

    if ".." in filename or filename.startswith("/"):
        return jsonify(error="Invalid filename"), 400

    try:
        with open(filename, "r") as f:
            content = f.read()
        return jsonify(content=content)
    except FileNotFoundError:
        return jsonify(error="File not found"), 404

# -------------------------------
# DEBUG supprimé (bonne pratique)
# -------------------------------

@app.route("/hello", methods=["GET"])
def hello():
    return jsonify(message="Welcome to the secure DevSecOps API")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Blueprint, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, get_jwt_identity
from db import get_db

auth = Blueprint('auth', __name__)
bcrypt = Bcrypt()  # No pasar app aquí

@auth.route('/auth/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed = bcrypt.generate_password_hash(data['password']).decode('utf-8')

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (username, password) VALUES (%s, %s)", (data['username'], hashed))
    conn.commit()
    cursor.close()

    return jsonify({"msg": "Usuario registrado"}), 201

@auth.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE username = %s", (data['username'],))
    user = cursor.fetchone()
    cursor.close()
    # access_token = create_access_token(identity={
    #     'id': user['id'],
    #     'username': user['username']
    # })
    if user and bcrypt.check_password_hash(user['password'], data['password']):
        access_token = create_access_token(identity=str(user['id']))  # ✅ conversión a string
        return jsonify({"access_token":access_token,"username": user['username']}), 200

    return jsonify({"msg": "Credenciales inválidas"}), 401
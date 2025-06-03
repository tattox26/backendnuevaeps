from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from db import get_db

medicamentos = Blueprint('medicamentos', __name__)

@medicamentos.route('/medicamentos', methods=['GET'])
@jwt_required()
def listar_medicamentos():
    try: 
        conn = get_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, nombre FROM medicamentos")
        resultados = cursor.fetchall()        
        return jsonify({
            "medicamentos": resultados
        }), 200    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
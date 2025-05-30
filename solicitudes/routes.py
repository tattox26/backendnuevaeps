from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from db import get_db

solicitudes = Blueprint('solicitudes', __name__)

@solicitudes.route('/solicitudes', methods=['POST'])
@jwt_required()

def crear_solicitud():
    try:
        data = request.get_json()
        user_id = get_jwt_identity()
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO solicitudes (medicamento_id, usuario_id, numero_orden, direccion, telefono, correo)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            data['medicamento_id'], 
            user_id,
            data.get('numero_orden'),
            data.get('direccion'),
            data.get('telefono'),
            data.get('correo')
        ))
        conn.commit()
        cursor.close()
        return jsonify({"msg": "Solicitud creada"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@solicitudes.route('/solicitudes', methods=['GET'])
@jwt_required()
def listar_solicitudes():
    try:
        user_id = get_jwt_identity()
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        offset = (page - 1) * per_page
        conn = get_db()
        cursor = conn.cursor(dictionary=True)
        # Consulta paginada
        cursor.execute("""
                SELECT s.*, m.nombre AS medicamento_nombre
                FROM solicitudes s
                JOIN medicamentos m ON s.medicamento_id = m.id
                WHERE s.usuario_id = %s
                LIMIT %s OFFSET %s
            """, (user_id, per_page, offset))
        resultados = cursor.fetchall()

        # Opcional: contar total para saber cuántas páginas hay
        cursor.execute("SELECT COUNT(*) as total FROM solicitudes WHERE usuario_id = %s", (user_id,))
        total = cursor.fetchone()['total']

        cursor.close()

        return jsonify({
            "solicitudes": resultados,
            "total": total,
            "page": page,
            "per_page": per_page
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


#@bp.route('/medicamentos', methods=['GET'])
@solicitudes.route('/medicamentos', methods=['GET'])
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
    return jsonify(medicamentos)
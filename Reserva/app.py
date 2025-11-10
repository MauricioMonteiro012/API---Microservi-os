from flask import Blueprint, jsonify, request

bp = Blueprint('reserva', __name__)

reservas = []
reserva_id = 1

@bp.route('/', methods=['GET'])
def status():
    return "API Reserva funcionando!"

@bp.route('', methods=['POST'])
def criar_reserva():
    global reserva_id
    data = request.json
    r = {"id": reserva_id, "turma_id": data["turma_id"], "data": data["data"]}
    reservas.append(r)
    reserva_id += 1
    return jsonify({"id": r["id"], "mensagem": "Reserva criada"}), 201

@bp.route('', methods=['GET'])
def listar_reservas():
    return jsonify(reservas), 200

@bp.route('/<int:id>', methods=['GET'])
def obter_reserva(id):
    r = next((x for x in reservas if x["id"] == id), None)
    return (jsonify(r), 200) if r else (jsonify({"erro": "Não encontrada"}), 404)
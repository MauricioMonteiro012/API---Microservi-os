from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/reservas', methods=['POST'])
def criar_reserva():
    """
    Cria uma reserva de sala
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            turma_id:
              type: integer
              example: 3
            data:
              type: string
              example: "2025-11-10"
    responses:
      201:
        description: Reserva criada com sucesso
    """
    return jsonify({"mensagem": "Reserva criada"}), 201

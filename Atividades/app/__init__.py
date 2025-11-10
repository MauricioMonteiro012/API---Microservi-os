from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/atividades', methods=['POST'])
def criar_atividade():
    """
    Cria uma nova atividade
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            professor_id:
              type: integer
              example: 1
            turma_id:
              type: integer
              example: 3
            titulo:
              type: string
              example: "Prova de Matemática"
            nota:
              type: number
              example: 8.5
    responses:
      201:
        description: Atividade criada com sucesso
    """
    return jsonify({"mensagem": "Atividade criada"}), 201

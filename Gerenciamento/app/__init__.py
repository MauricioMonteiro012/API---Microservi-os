from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/professores', methods=['POST'])
def criar_professor():
    """
    Cadastra um novo professor
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            nome:
              type: string
              example: "Maria"
            disciplina:
              type: string
              example: "Matemática"
    responses:
      201:
        description: Professor criado com sucesso
    """
    return jsonify({"mensagem": "Professor criado"}), 201

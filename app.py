from flask import Flask
from flasgger import Swagger
from Atividades.app import bp as atividades_bp
from Gerenciamento.app import bp as gerenciamento_bp
from Reserva.app import bp as reserva_bp

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/')
def home():
    return "API Gateway Funcionando!"

app.register_blueprint(atividades_bp, url_prefix='/atividades')
app.register_blueprint(gerenciamento_bp, url_prefix='/gerenciamento')
app.register_blueprint(reserva_bp, url_prefix='/reservas')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
# 👥 Integrantes do Projeto

- *Emilly Silva Eduardo Pereira* – RA: 2403751  
- *Gabrielly Soares Marinho* – RA: 2403430  
- *Maurício Monteiro Filho* – RA: 2302967


# 📚 API de Gerenciamento de Professores, Turmas e Alunos

Este projeto é uma *API RESTful desenvolvida em Flask* para gerenciar Professores, Turmas e Alunos.  
Ela foi construída aplicando *Programação Orientada a Objetos (POO)* e boas práticas de *arquitetura MVC, com **persistência em banco SQLite via SQLAlchemy* e documentação automática com *Swagger*.  
Além disso, a aplicação pode ser *containerizada com Docker* para facilitar sua implantação.

---

## 🎯 Objetivos do Projeto
- Prover um sistema simples e eficiente para cadastro, consulta, atualização e exclusão de Professores, Turmas e Alunos.
- Aplicar conceitos de *POO* e *arquitetura MVC* no Flask.
- Demonstrar o uso do *ORM SQLAlchemy* em conjunto com SQLite.
- Expor as funcionalidades via *API RESTful*.
- Criar documentação da API com *Swagger*.
- Versionar todo o código no *GitHub*.
- Permitir a execução da aplicação em *containers Docker*.

---

## 🛠️ Tecnologias Utilizadas
- Python 3.10+
- Flask
- Flask-SQLAlchemy
- Flask-Migrate (opcional)
- Flasgger (Swagger)
- SQLite
- Docker

---

## 📐 Arquitetura do Projeto

A aplicação segue o padrão *MVC*:

- *Models*: Camada que representa as tabelas do banco de dados e seus relacionamentos (Professor, Turma, Aluno).
- *Controllers*: Camada que contém as rotas e a lógica de negócio.
- *Views*: Camada que representa as respostas (no caso desta API, JSON).

### Estrutura de Pastas

---

## 🗄️ Modelo de Dados

### Entidades e Relacionamentos

- Um *Professor* pode ter várias *Turmas* (1:N).
- Uma *Turma* pertence a um único *Professor*.
- Uma *Turma* pode ter vários *Alunos* (1:N).
- Um *Aluno* pertence a uma única *Turma*.

### Dicionário de Dados

| Entidade | Campo | Tipo | Obrigatório | Descrição |
|----------|-------|------|-------------|-----------|
| *Professor* | id (PK) | Integer | Sim | Identificador único do professor |
| | nome | String | Sim | Nome do professor |
| | idade | Integer | Sim | Idade do professor |
| | materia | String | Sim | Matéria lecionada |
| | observacoes | Text | Não | Observações gerais sobre o professor |
| *Turma* | id (PK) | Integer | Sim | Identificador único da turma |
| | descricao | String | Sim | Descrição/nome da turma |
| | professor_id (FK) | Integer | Sim | Chave estrangeira referenciando Professor |
| | ativa | Boolean | Sim | Status se a turma está ativa ou não |
| *Aluno* | id (PK) | Integer | Sim | Identificador único do aluno |
| | nome | String | Sim | Nome do aluno |
| | idade | Integer | Sim | Idade do aluno |
| | turma_id (FK) | Integer | Sim | Chave estrangeira referenciando Turma |
| | data_nascimento | Date | Sim | Data de nascimento do aluno |
| | nota_primeiro_semestre | Float | Sim | Nota do 1º semestre |
| | nota_segundo_semestre | Float | Sim | Nota do 2º semestre |
| | media_final | Float | Calculado | Média final do aluno |

### Diagrama Entidade-Relacionamento
Professor (1) ─── (N) Turma (1) ─── (N) Aluno

---

## 🔗 Rotas da API

### Professores
- GET /professores – Lista todos os professores.
- POST /professores – Cadastra um novo professor.
- GET /professores/<id> – Detalha um professor específico.
- PUT /professores/<id> – Atualiza dados de um professor.
- DELETE /professores/<id> – Remove um professor.

### Turmas
- GET /turmas – Lista todas as turmas.
- POST /turmas – Cadastra uma nova turma.
- GET /turmas/<id> – Detalha uma turma específica.
- PUT /turmas/<id> – Atualiza dados de uma turma.
- DELETE /turmas/<id> – Remove uma turma.

### Alunos
- GET /alunos – Lista todos os alunos.
- POST /alunos – Cadastra um novo aluno.
- GET /alunos/<id> – Detalha um aluno específico.
- PUT /alunos/<id> – Atualiza dados de um aluno.
- DELETE /alunos/<id> – Remove um aluno.

---

## ▶️ Como Executar Localmente

1. *Clonar o repositório*
   ```bash
   git clone https://github.com/MauricioMonteiro012/API---Microservi-os.git
   cd Projeto_FLASK_API



   # Projeto_FLASK_API - Continuação

## Como rodar (Docker)

1. Clone seu repositório localmente (se já não estiver):
   git clone https://github.com/MauricioMonteiro012/API---Microservi-os.git
2. Coloque as pastas `gerenciamento`, `reservas`, `atividades` com os arquivos descritos.
3. Execute:
   docker compose up --build

Os serviços ficarão acessíveis em:
- Gerenciamento: http://localhost:5001
- Reservas: http://localhost:5002
- Atividades: http://localhost:5003

## Como rodar o Swagger
- # No PowerShell do Windows:
$env:FLASK_APP = "app.py"
flask run --host=0.0.0.0 --port=5000
http://127.0.0.1:5000/apidocs

## Endpoints (exemplos)
- GET /turmas (gerenciamento)
- POST /reservas {turma_id, descricao, data} (reservas)
- POST /atividades {titulo, descricao, turma_id, professor_id} (atividades)
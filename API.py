from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração do Banco de Dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Definição do Modelo do Banco de Dados
class Registro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Registro %r>' % self.nome

# Rota para Buscar todos os Registros do Banco de Dados
@app.route('/registros', methods=['GET'])
def buscar_registros():
    registros = Registro.query.all()
    return jsonify([{'id': registro.id, 'nome': registro.nome, 'idade': registro.idade, 'email': registro.email} for registro in registros])

# Rota para Cadastrar um Registro no Banco de Dados
@app.route('/registros', methods=['POST'])
def cadastrar_registro():
    nome = request.json['nome']
    idade = request.json['idade']
    email = request.json['email']
    registro = Registro(nome=nome, idade=idade, email=email)
    db.session.add(registro)
    db.session.commit()
    return jsonify({'message': 'Registro cadastrado com sucesso!'})

# Rota para Excluir um Registro do Banco de Dados
@app.route('/registros/<int:id>', methods=['DELETE'])
def excluir_registro(id):
    registro = Registro.query.get(id)
    if registro:
        db.session.delete(registro)
        db.session.commit()
        return jsonify({'message': 'Registro excluído com sucesso!'})
    else:
        return jsonify({'message': 'Registro não encontrado!'})

if __name__ == '__main__':
    app.run(debug=True)



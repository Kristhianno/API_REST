from flask import Flask, jsonify, request

from bdFake import Clientes

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/Clientes', methods=['GET'])
def return_AllClientes():
    return jsonify({'Clientes': Clientes})


@app.route('/Clientes/<string:nome>', methods=['GET'])
def return_OneCliente(nome):
    OneCliente = [Cliente for Cliente in Clientes if Cliente['nome'] == nome]
    return jsonify({'Cliente': OneCliente[0]})


@app.route('/Clientes', methods=['POST'])
def create_Cliente():
    Cliente = {'id': request.json['id'],
               'nome': request.json['nome'],
               'profissao': request.json['profissao'],
               'idade': request.json['idade'],
               'email': request.json['email']
               }
    Clientes.append(Cliente)
    return jsonify({'Lista de Clientes': Clientes})


if __name__ == '__main__':
    app.run(debug=True, port=8080)


# app.run()

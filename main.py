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


@app.route('/Clientes/<string:profissao>', methods=['PUT'])
def update_Cliente(profissao):
    UpdateCliente = [
        Cliente for Cliente in Clientes if Cliente['profissao'] == profissao]
    UpdateCliente[0]['profissao'] = request.json['profissao']
    return jsonify({'Clientes': UpdateCliente[0]})


@app.route('/Clientes/<string:nome>', methods=['DELETE'])
def delet_Cliente(nome):
    delCliente = [Cliente for Cliente in Clientes if Cliente['nome'] == nome]
    Clientes.remove(delCliente[0])
    return jsonify({'Clientes': delCliente[0]})


if __name__ == '__main__':
    app.run(debug=True, port=8080)


# app.run()

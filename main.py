from flask import Flask, jsonify, make_response, request

from bdFake import Clientes

app = Flask(__name__)  # instancia do Flask


# por padrão o Flask ordena os dados de A-Z.
app.config['JSON_SORT_KEYS'] = False


# decorator do flask para indicar que a função criada é uma requisição do usuario portanto uma rota que precisa ser executada com o método GET.
@app.route('/Clientes', methods=['GET'])
def pegar_Clientes():  # função que retorna a lista JSON de todos os clientes cadastrados.
    # configurando a forma como esta lista será apresentada ao usuário.
    return make_response(jsonify(Clientes))


# decorator do flask para indicar que a função criada é uma requisição do usuario portanto uma rota que precisa ser executada com o método POST.
@app.route('/Clientes', methods=['POST'])
def criar_Cliente():  # função que cria um novo Cliente.
    Cliente = request.json  # O arquivo enviado ao banco de dados será do tipo .json
    # Chamando o Banco de dados para adicionar o novo dado em seu conjunto de dados 'lista'
    Clientes.append(Cliente)
    # Retornando a nova lista de Clientes atualizadas depois de adicionar mais um cliente.
    return make_response(
        jsonify(
            mensagem='Lista de Clientes',
            dados=Clientes
        )
    )


app.run()  # executa a API Rest

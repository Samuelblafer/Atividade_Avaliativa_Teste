from flask import Flask, request, jsonify
from src.estoque import Estoque, ErroEstoque

app = Flask(__name__)
estoque = Estoque()


@app.route('/produto', methods=['POST'])
def adicionar():
    data = request.get_json() or {}
    nome = data.get('nome')
    quantidade = data.get('quantidade')
    if nome is None or quantidade is None:
        return jsonify({'error': 'Campos "nome" e "quantidade" são obrigatórios.'}), 400

    try:
        # usar métodos da classe Estoque para manter a lógica
        msg = estoque.adicionar_produto(nome, quantidade)
        if 'Adicionadas' in msg:
            return jsonify({'message': msg}), 201
        return jsonify({'error': msg}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/produto', methods=['DELETE'])
def remover():
    data = request.get_json() or {}
    nome = data.get('nome')
    quantidade = data.get('quantidade')
    if nome is None or quantidade is None:
        return jsonify({'error': 'Campos "nome" e "quantidade" são obrigatórios.'}), 400

    try:
        msg = estoque.remover_produto(nome, quantidade)
        if 'Removidas' in msg:
            return jsonify({'message': msg}), 200
        return jsonify({'error': msg}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/produto/<nome>', methods=['GET'])
def verificar(nome):
    qtd = estoque.verificar_estoque(nome)
    return jsonify({'nome': nome.strip().lower(), 'quantidade': qtd}), 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

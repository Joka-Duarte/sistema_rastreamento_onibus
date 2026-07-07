from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Rota 1: Motorista enviando coordenadas (POST)
@app.route('/api/v1/telemetria/batch', methods=['POST'])
def receber_telemetria():
    dados = request.get_json()
    
    # Validação simples exigida no contrato
    if not dados or 'idLinha' not in dados:
        return jsonify({"status": "erro", "mensagem": "O campo 'idLinha' é obrigatório."}), 400
    
    qtd_coordenadas = len(dados.get('coordenadas', []))
    
    # Resposta de Sucesso (201 Created)
    return jsonify({
        "status": "sucesso",
        "mensagem": f"{qtd_coordenadas} coordenadas processadas e salvas.",
        "timestampSincronizacao": datetime.now().isoformat() + "Z"
    }), 201


# Rota 2: Passageiro consultando o ônibus (GET)
@app.route('/api/v1/linhas/<idLinha>/veiculos', methods=['GET'])
def consultar_rota(idLinha):
    # Retornando dados simulados para a demonstração
    return jsonify({
      "idLinha": idLinha,
      "totalVeiculosAtivos": 1,
      "veiculos": [
        {
          "idVeiculo": "V-204",
          "ultimaLatitude": -31.33010,
          "ultimaLongitude": -54.10015,
          "timestampCaptura": datetime.now().isoformat() + "Z"
        }
      ]
    }), 200

if __name__ == '__main__':
    # host='0.0.0.0' permite receber conexões de outros aparelhos na mesma rede local
    app.run(debug=True, host='0.0.0.0', port=5000)
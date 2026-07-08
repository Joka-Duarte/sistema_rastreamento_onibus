from flask import Flask, request, jsonify, render_template
from datetime import datetime
import uuid

app = Flask(__name__)

# Bancos de dados em memória
banco_de_dados = { "RU01": {} }
banco_avisos = {}

# --- ROTAS DE INTERFACE (HTML) ---
@app.route('/motorista', methods=['GET'])
def abrir_motorista():
    return render_template('motorista.html')

@app.route('/passageiro', methods=['GET'])
def abrir_passageiro():
    return render_template('passageiro.html')

# --- ROTAS DA API ---

# Rota 1: Receber telemetria do motorista
@app.route('/api/v1/telemetria/batch', methods=['POST'])
def receber_telemetria():
    dados = request.get_json()
    if not dados or 'idLinha' not in dados:
        return jsonify({"status": "erro", "mensagem": "O campo 'idLinha' é obrigatório."}), 400
    
    id_linha = dados['idLinha']
    id_veiculo = dados.get('idVeiculo', 'V-Desconhecido')
    coordenadas = dados.get('coordenadas', [])
    
    if id_linha not in banco_de_dados:
        banco_de_dados[id_linha] = {}
        
    if coordenadas:
        ultima_coord = coordenadas[-1]
        banco_de_dados[id_linha][id_veiculo] = {
            "ultimaLatitude": ultima_coord.get("latitude"),
            "ultimaLongitude": ultima_coord.get("longitude"),
            "timestampCaptura": ultima_coord.get("timestampCaptura")
        }
        
    return jsonify({
        "status": "sucesso",
        "mensagem": f"{len(coordenadas)} coordenadas processadas.",
        "timestampSincronizacao": datetime.now().isoformat() + "Z"
    }), 201

# Rota 2: Consultar posição dos ônibus
@app.route('/api/v1/linhas/<id_linha>/veiculos', methods=['GET'])
def consultar_rota(id_linha):
    veiculos_ativos = []
    if id_linha in banco_de_dados:
        for id_veiculo, dados in banco_de_dados[id_linha].items():
            veiculos_ativos.append({
                "idVeiculo": id_veiculo,
                "ultimaLatitude": dados["ultimaLatitude"],
                "ultimaLongitude": dados["ultimaLongitude"],
                "timestampCaptura": dados["timestampCaptura"]
            })
    
    if not veiculos_ativos:
        return jsonify({"status": "aviso", "mensagem": "Nenhum veículo operando nesta linha."}), 404
        
    return jsonify({
        "idLinha": id_linha,
        "totalVeiculosAtivos": len(veiculos_ativos),
        "veiculos": veiculos_ativos
    }), 200

# Rota 3: Gerenciar Avisos da Comunidade/Motorista
@app.route('/api/v1/linhas/<id_linha>/avisos', methods=['GET', 'POST'])
def gerenciar_avisos(id_linha):
    if id_linha not in banco_avisos:
        banco_avisos[id_linha] = []
        
    # Se for POST, está CRIANDO um aviso novo
    if request.method == 'POST':
        dados = request.get_json()
        origem = dados.get("origem", "passageiro") # Descobre quem enviou (padrão é passageiro)
        
        novo_aviso = {
            "idAviso": str(uuid.uuid4())[:8],
            "tipoProblema": dados.get("tipoProblema", "Problema na Linha"),
            "origem": origem,
            "votosUteis": 1,
            "votosDesatualizados": 0
        }
        banco_avisos[id_linha].append(novo_aviso)
        return jsonify({"status": "sucesso", "mensagem": "Aviso publicado."}), 201

    # Se for GET, está LENDO os avisos
    avisos_ativos = []
    for aviso in banco_avisos[id_linha]:
        total_votos = aviso["votosUteis"] + aviso["votosDesatualizados"]
        
        # REGRA DE NEGÓCIO: Oculta se tiver 5+ votos e o dobro de negativos.
        # EXCEÇÃO: Nunca oculta se a origem for o "motorista" (Aviso Oficial)
        if aviso["origem"] != "motorista" and total_votos >= 5 and aviso["votosDesatualizados"] > (aviso["votosUteis"] * 2):
            continue 
            
        avisos_ativos.append(aviso)
        
    return jsonify({"avisos": avisos_ativos}), 200

# Rota 4: Votação nos Avisos
@app.route('/api/v1/avisos/<id_aviso>/votar', methods=['POST'])
def votar_aviso(id_aviso):
    dados = request.get_json()
    tipo_voto = dados.get("voto") 
    
    for linha, avisos in banco_avisos.items():
        for aviso in avisos:
            if aviso["idAviso"] == id_aviso:
                if tipo_voto == 'util':
                    aviso["votosUteis"] += 1
                elif tipo_voto == 'desatualizado':
                    aviso["votosDesatualizados"] += 1
                return jsonify({"status": "sucesso"}), 200
                
    return jsonify({"status": "erro", "mensagem": "Aviso não encontrado."}), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
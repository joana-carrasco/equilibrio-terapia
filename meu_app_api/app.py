import sqlite3
import re
import os
from datetime import datetime
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from config import DB_PATH, TABELA_CONSULENTES
from controller import obter_conselho
from logger import logger

FRONTEND_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'meu_app_front'))

app = Flask(__name__, static_folder=os.path.join(FRONTEND_FOLDER), static_url_path='')
CORS(app)

@app.route('/')
def home():
    logger.info("Página inicial acessada.")
    return send_from_directory(FRONTEND_FOLDER, 'index.html')

@app.route('/imagens/<path:filename>')
def imagens(filename):
    return send_from_directory(os.path.join(FRONTEND_FOLDER, 'imagens'), filename)

@app.route('/conselho', methods=['POST'])
def gerar_conselho():
    try:
        dados = request.get_json()
        ano_str = dados.get('ano')
        aniversario = dados.get('aniversario')

        
        if not ano_str or not aniversario:
            return jsonify({'erro': 'Ano e aniversário são obrigatórios.'}), 400

        
        if not ano_str.isdigit():
            return jsonify({'erro': 'Ano deve conter apenas números.'}), 400

        
        if len(ano_str) != 4:
            return jsonify({'erro': 'Ano deve conter exatamente 4 dígitos.'}), 400

        
        ano = int(ano_str)
        ano_atual = datetime.now().year
        limite_superior = ano_atual + 5

      
        if ano < ano_atual or ano > limite_superior:
            return jsonify({'erro': f'Ano inválido. Só é permitido gerar conselhos entre {ano_atual} e {limite_superior}.'}), 400

        
        try:
            partes = aniversario.split('/')
            if len(partes) != 3:
                raise ValueError
            dia, mes, ano_nasc = map(int, partes)
            data_nascimento = datetime(ano_nasc, mes, dia)
            if data_nascimento > datetime.now():
                return jsonify({'erro': 'Data de nascimento não pode ser no futuro.'}), 400
        except Exception:
            return jsonify({'erro': 'Formato de data inválido. Use DD/MM/AAAA.'}), 400

       
        logger.info(f"Solicitação de conselho recebida: ano={ano}, aniversario={aniversario}")
        resposta = obter_conselho(ano, aniversario)

        if resposta:
            return jsonify(resposta)
        else:
            return jsonify({'erro': 'Arcano não encontrado.'}), 404

    except Exception as e:
        logger.error(f"Erro ao gerar conselho: {e}")
        return jsonify({'erro': 'Erro interno ao gerar conselho.'}), 500


@app.route('/consulentes', methods=['POST'])
def cadastrar_consulente():
    try:
        dados = request.get_json()
        nome = dados.get('nome')
        email = dados.get('email')
        data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if not nome or not email:
            logger.warning("Tentativa de cadastro com dados incompletos.")
            return jsonify({'erro': 'Nome e e-mail são obrigatórios.'}), 400

       
        padrao_email = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
        if not re.match(padrao_email, email):
            logger.warning(f"E-mail inválido informado: {email}")
            return jsonify({'erro': 'Formato de e-mail inválido.'}), 400

        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute(f"INSERT INTO {TABELA_CONSULENTES} (nome, email, data_cadastro) VALUES (?, ?, ?)", (nome, email, data))
        conn.commit()
        conn.close()

        logger.info(f"Novo consulente cadastrado: {nome} - {email}")
        return jsonify({'mensagem': 'Usuário cadastrado com sucesso.'}), 201

    except Exception as e:
        logger.error(f"Erro ao cadastrar consulente: {e}")
        return jsonify({'erro': 'Erro interno ao cadastrar.'}), 500

@app.route('/historico', methods=['GET'])
def listar_historico():
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("SELECT id, ano, aniversario, numero_arcano, nome_arcano, conselho, data_geracao FROM historico_conselhos ORDER BY data_geracao DESC")
        resultados = cur.fetchall()
        conn.close()

        logger.info("Histórico de conselhos listado com sucesso.")
        historico = [
            {
                'id': row[0],
                'ano': row[1],
                'aniversario': row[2],
                'numero_arcano': row[3],
                'nome_arcano': row[4],
                'conselho': row[5],
                'data_geracao': row[6]
            }
            for row in resultados
        ]
        return jsonify(historico)

    except Exception as e:
        logger.error(f"Erro ao listar histórico: {e}")
        return jsonify({'erro': 'Erro interno ao buscar histórico.'}), 500

@app.route('/historico/<int:id>', methods=['DELETE'])
def deletar_conselho(id):
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("DELETE FROM historico_conselhos WHERE id = ?", (id,))
        conn.commit()
        conn.close()

        logger.info(f"Registro de conselho com ID {id} removido com sucesso.")
        return jsonify({'mensagem': 'Conselho removido com sucesso.'}), 200

    except Exception as e:
        logger.error(f"Erro ao remover conselho: {e}")
        return jsonify({'erro': 'Erro interno ao remover conselho.'}), 500

@app.route('/swagger.json')
def swagger_spec():
    return send_from_directory(os.path.dirname(__file__), 'swagger.json')

if __name__ == '__main__':
    logger.info("Servidor Flask iniciado em http://localhost:5000")
    app.run(debug=True)

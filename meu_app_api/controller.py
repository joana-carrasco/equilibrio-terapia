import os
import sqlite3
from logger import logger
from config import DB_PATH, TABELA_ARCANOS, TABELA_HISTORICO
from datetime import datetime
from models.models import Arcano, CalculadoraArcano


def carregar_lista_arcanos():
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute(f"SELECT numero, nome, conselho FROM {TABELA_ARCANOS}")
        rows = cur.fetchall()
        conn.close()
        logger.info(f"{len(rows)} arcanos carregados com sucesso do banco.")
        return [Arcano(numero, nome, conselho) for numero, nome, conselho in rows]
    except Exception as e:
        logger.error(f"Erro ao carregar arcanos de {DB_PATH}: {e}")
        return []


def obter_conselho(ano, aniversario, nome=None, email=None):
    try:
        arcanos = carregar_lista_arcanos()
        numero_arcano = CalculadoraArcano.calcular(ano, aniversario)
        logger.info(f"Cálculo do número do arcano para {ano}/{aniversario}: {numero_arcano}")

        for arcano in arcanos:
            conselho = arcano.obter_conselho()
            if conselho['numero'] == numero_arcano:
                logger.info(f"Arcano encontrado: {conselho['nome']} (nº {numero_arcano})")
                logger.debug(f"Chamando registrar_historico para arcano {numero_arcano}")
                registrar_historico(ano, aniversario, numero_arcano)
                return conselho

        logger.warning(f"Arcano nº {numero_arcano} não encontrado.")
        return None
    except Exception as e:
        logger.error(f"Erro ao obter conselho: {e}")
        return None

def registrar_historico(ano, aniversario, numero_arcano):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cur = conn.cursor()

            # Buscar nome e conselho
            cur.execute(f"SELECT nome, conselho FROM {TABELA_ARCANOS} WHERE numero = ?", (numero_arcano,))
            resultado = cur.fetchone()
            nome_arcano, conselho = resultado if resultado else ("Desconhecido", "Conselho não encontrado.")

            data_geracao = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            cur.execute(f'''
                INSERT INTO {TABELA_HISTORICO}
                (ano, aniversario, numero_arcano, nome_arcano, conselho, data_geracao)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (ano, aniversario, numero_arcano, nome_arcano, conselho, data_geracao))

            conn.commit()
            logger.info(f"Histórico registrado com sucesso: arcano {numero_arcano}, data {data_geracao}")
    except Exception as e:
        logger.error(f"Erro ao registrar histórico: {e}")

import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database", "arcanos.db")


TABELA_ARCANOS = "arcanos"
TABELA_CONSULENTES = "consulentes"
TABELA_HISTORICO = "historico_conselhos"

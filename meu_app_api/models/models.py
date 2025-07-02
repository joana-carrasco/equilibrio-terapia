from logger import logger

class Arcano:
    def __init__(self, numero, nome, conselho):
        self.__numero = numero
        self.__nome = nome
        self.__conselho = conselho

    def obter_conselho(self):
        return {
            "numero": self.__numero,
            "nome": self.__nome,
            "conselho": self.__conselho
        }

class CalculadoraArcano:
    @staticmethod
    def calcular(ano, aniversario):
        try:
            soma_ano = sum(int(d) for d in str(ano))
            aniversario = aniversario.replace("/", "")
            if not aniversario.isdigit():
                raise ValueError("Data de nascimento inválida. Deve conter apenas números e barras.")

            soma_nasc = sum(int(d) for d in aniversario)
            total = soma_ano + soma_nasc
            while total > 21:
                total = sum(int(d) for d in str(total))

            logger.info(f"Arcano calculado com sucesso - Ano: {ano}, Aniversário: {aniversario}, Resultado: {total}")
            return total

        except Exception as e:
            logger.error(f"Erro ao calcular arcano: {e}")
            return 0
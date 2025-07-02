Equilíbrio e Terapia – API de Conselhos com Tarot
Este é um projeto desenvolvido como parte da disciplina Desenvolvimento Full Stack Básico da PUC-Rio.
A aplicação entrega conselhos personalizados com base nos Arcanos Maiores do Tarot, utilizando o ano desejado e a data de nascimento do consulente como referência numerológica.

Funcionalidades
		Geração de conselho com base em cálculo numerológico dos Arcanos Maiores.

		Cadastro de consulentes com nome completo e e-mail.

		Registro automático do histórico de conselhos gerados.

		Listagem pública dos conselhos gerados (exibida no rodapé da página).

	Validação de dados e geração de logs com logger.py.


Estruturação de Pastas - 

meu_app_api/
├── app.py                # Arquivo principal da aplicação Flask
├── controller.py         # Lógica de negócio e conexão com banco
├── config.py             # Constantes de configuração e nomes das tabelas
├── logger.py             # Configuração centralizada de logs
├── requirements.txt      # Lista de dependências (Flask, etc.)
├── swagger.json          # Documentação Swagger da API
├── README.md             # Este arquivo

├── database/
│   ├── arcanos.db        # Banco de dados SQLite
│   ├── database.json     # Arquivo auxiliar de metadados (opcional)
│   └── __init__.py       # Inicialização do módulo database

├── models/
│   ├── models.py         # Classes e lógica de domínio
│   └── __init__.py

├── schemas/
│   └── __init__.py       # Pasta mantida para compatibilidade acadêmica



Como executar
	1. Clone o repositório

		git clone https://github.com/seu-usuario/equilibrio-terapia.git
		cd equilibrio-terapia/meu_app_api
		
	2. Crie o ambiente virtual
		python -m venv venv
		
	3. Ative o ambiente virtual
		
		No Windows:

		venv\Scripts\activate
		
		No Mac/Linux:

		source venv/bin/activate
		
	4. Instale as dependências
		
		pip install -r requirements.txt
		
		▶️ Executando o servidor
			python app.py
		
		Acesse em seu navegador: http://localhost:5000

Endpoints disponíveis
A documentação completa da API está disponível no arquivo swagger.json, contendo os seguintes endpoints:

		POST /conselho  - Gera um novo conselho com base na data e ano informados.

		POST /consulentes  - adastra um novo consulente (nome e e-mail).

		GET /historico  - Retorna o histórico de conselhos gerados.

		DELETE /historico/<id> – Remove um conselho específico do histórico. ✅ (Requisito importante incluído)



Observação sobre a pasta schemas/
A pasta schemas/ foi mantida apenas para seguir o modelo de estrutura apresentado na disciplina.
Neste projeto, as validações de dados são feitas diretamente no front-end e no controller da API, sem uso de bibliotecas como pydantic ou marshmallow.
Por isso, nenhum arquivo da pasta schemas/ está sendo utilizado no momento.

Logs
Todos os eventos importantes da aplicação (erros, ações de cadastro, geração de conselhos, etc.) são registrados automaticamente em:
		app.log

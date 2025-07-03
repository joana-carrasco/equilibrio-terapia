Equilíbrio e Terapia – API de Conselhos com Tarot
Projeto desenvolvido como parte da disciplina Desenvolvimento Full Stack Básico da PUC-Rio.
A aplicação entrega conselhos personalizados com base nos Arcanos Maiores do Tarot, utilizando o ano desejado e a data de nascimento do consulente como referência numerológica para envio de um conselho.
________________________________________
 Funcionalidades
•	 Geração de conselho com base em cálculo numerológico.
•	 Cadastro de consulentes com nome completo e e-mail.
•	 Registro automático no histórico de conselhos gerados.
•	 Listagem pública do histórico.
•	 Validações robustas de dados (ano, aniversário, e-mail).
•	 Geração automática de logs detalhados.
________________________________________

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
├── arcanos.db        # Banco de dados SQLite
├── database.json     # Lista de conselhos dos arcanos maiores do Tarot
└── __init__.py       # Arquivo informativo python

├── models/
├── models.py         # Classes e lógica de domínio: Arcano, CalculadoraArcano
└── __init__.py       # Arquivo informativo python

├── schemas/
└── __init__.py       # Arquivo informativo python
________________________________________
Como Executar
1.	Clone o repositório:
git clone https://github.com/joana-carrasco/equilibrio-terapia
cd equilibrio-terapia/meu_app_api

2.	Crie o ambiente virtual:
python -m venv venv

3.	Ative o ambiente virtual:
•	No Windows:
venv\Scripts\activate
•	No Mac/Linux:
source venv/bin/activate

4.	Instale as dependências:
pip install -r requirements.txt

5.	Execute o servidor:
python app.py

6.	Acesse em seu navegador:
http://localhost:5000
________________________________________
Endpoints disponíveis

A documentação completa da API está disponível no arquivo swagger.json. Os endpoints são:

•	POST /conselho
Gera um novo conselho com base na data de nascimento e ano desejado.
•	POST /consulentes
Cadastra um novo consulente (nome e e-mail).
•	GET /historico
Retorna a lista de conselhos já gerados pela aplicação.
•	DELETE /historico/<id>
Remove um conselho específico do histórico. 
________________________________________
Validações implementadas
•	Ano com 4 dígitos numéricos entre o ano atual e até 5 anos à frente.
•	Data de nascimento no formato DD/MM/AAAA, sem permitir datas futuras.
•	E-mail com regex padrão.
•	Tratamento de erros com mensagens amigáveis.
•	Cálculo do arcano restrito ao intervalo de 1 a 21 (Arcanos Maiores).
________________________________________
Observações sobre schemas/
A pasta schemas/ foi mantida apenas para seguir o modelo acadêmico da disciplina.
Neste projeto, as validações de dados são feitas diretamente na API (controller.py) e no front-end, sem uso de Pydantic ou Marshmallow.
________________________________________
Logs
Todos os eventos relevantes da aplicação são registrados automaticamente em:
meu_app_api/app.log
Logs incluem:
•	Acessos à página inicial
•	Requisições de conselho
•	Cadastros de usuários
•	Erros de validação ou conexão
•	Remoções no histórico
________________________________________
Autoria
Projeto criado por Joana Carrasco
Pós-graduação em Engenharia de Software – PUC-Rio

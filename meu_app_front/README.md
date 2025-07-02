Equilíbrio e Terapia – Front-End
Este repositório contém o front-end da aplicação Equilíbrio e Terapia. Ele é responsável por coletar as informações do usuário (nome, e-mail, data de nascimento e ano desejado) e exibir o conselho gerado com base no retorno da API.

✅ Tecnologias utilizadas
   HTML5
   CSS3
   JavaScript (puro)
   Consumo de API REST via fetch

📁 Estrutura

      meu_app_front/
      ├── index.html     # Página principal
      ├── style.css      # Estilos da interface
      ├── script.js      # Lógica de interação com a API e interface
      └── imagens/       # Imagens dos arcanos (1.jpg até 21.jpg)

▶️ Como visualizar
Certifique-se de que a API esteja ativa (consulte o README.md do backend).
Abra o arquivo index.html em seu navegador.
Preencha os campos:

   Ano desejado
   Data de nascimento

Clique em "Gerar Conselho" para visualizar o arcano correspondente ao ano desejado.

Para se cadastrar como consulente:

Clique em "Clique aqui" abaixo do conselho fornecido.

   Preencha os campos Nome e E-mail

Após gerar um conselho, você poderá visualizar o histórico de conselhos gerados e excluir conselhos individualmente.

Clique em "Histórico de Conselhos" para visualizar a lista de conselhos gerados na api.

Para excluir um conselho já gerado.

Clique em "Histórico de Conselhos" para visualizar a lista de conselhos gerados na api.

Clique no ícone da lixeira ao lado do conselho que deseja remover, e pronto o conselho será removido.

🔄 Comunicação com o Backend
O front consome os seguintes endpoints da API:

      POST /conselho – Geração do conselho com base no ano e data de nascimento.

      POST /consulentes – Cadastro do usuário.

      GET /historico – Consulta do histórico de conselhos.

      DELETE /historico/<id> – Exclusão de um conselho específico.

🎯 Funcionalidades
Máscara automática para a data de nascimento (formato DD/MM/AAAA)

Validações de campos (nome completo, e-mail, data futura, ano inválido)

Modal de cadastro com feedback visual

Exibição dinâmica do conselho gerado

Visualização e exclusão do histórico de conselhos

Botão de retorno para tela inicial

📌 Observações
As imagens dos Arcanos devem estar corretamente nomeadas (de 1.jpg até 21.jpg) na pasta /imagens.

O front-end depende que o backend esteja rodando localmente em http://localhost:5000.

Recomendado utilizar o navegador Google Chrome ou Mozilla Firefox para melhor compatibilidade.

Projeto desenvolvido para fins educacionais.
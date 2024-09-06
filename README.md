## Projeto-Carteira-Invest

Um projeto em Python que simula uma carteira de investimento, acompanhando diversos ativos e suas cotações.

## Ideia do Projeto

Este projeto tem como objetivo simular uma carteira de investimentos, oferecendo funcionalidades para monitorar e gerenciar diversos ativos financeiros, incluindo ações, FIIs, ETFs, renda fixa e criptomoedas.

### Funcionalidades Concluídas: 
  
- Acompanhamento de Dividendos: Monitore e gerencie os pagamentos de dividendos entre os ativos.
- Gráficos Interativos: Visualize os dados da carteira com gráficos dinâmicos.
- Separação por Ativos: Categorize os ativos por tipo (FIIs, Ações, ETFs, Renda Fixa, Crypto).
- Dashboard: Painel centralizado exibindo métricas-chave da carteira.
- Card: Pequenos card da carteira que informa se o ativo esta dando prejuizo ou lucro  na carteira
- Comparativos: Pelos dashboards da carteira o usuario consegue comparar os ativos com o seu P.M com a carteira atualizada pela cotação
- Valorização: Acompanhar o valor de mercado atual da carteira.
- Rentabilidade: Calcular e exibir a rentabilidade dos ativos.
- Histórico de Dividendos: Adicionar e visualizar o histórico de dividendos.
- Preço Teto Pessoal: Definir e acompanhar preços-alvo pessoais para os ativos.
- Preço Teto: Monitorar os preços dos ativos em relação aos tetos de mercado.
- Páginas Dedicadas: Criar páginas específicas para visualizações detalhadas de diferentes tipos de ativos.
- Relatorios 

### Em Desenvolvimento Futuro

- Usar uma api para pegar os dados de uma forma mais leve
- Integração com a Google, Facebook e a B3 
  
##
### Stack de Tecnologia usada

- `Python` -  Linguagem de programação principal usada.
- `PostgreSQL` - Sistema de banco de dados usado para armazenar os dados da carteira.
- `HTML/CSS/JS` - Tecnologias usadas para construir a interface do front-end.
  

##
### Bibliotecas e Frameworks Python

- `YFINANCE` - Para acessar dados financeiros e cotações de ativos.
- `FLASK` - Framework para construção da aplicação web.
- `PANDAS` - Biblioteca para manipulação e análise de dados.
- `SQLALCHEMY` -  ORM para interação com o banco de dados.
- `DASH` - Usada para criar gráficos dinâmicos e interativos.
- `kaleido`

##
### Considerações Futuras

- `MATPLOTLIB` & `SEABORN` - Bibliotecas potenciais para visualizações adicionais de dados.
- `COTAÇÃO EM TEMPO REAL` -  Implementar a funcionalidade de cotações em tempo real ou com atraso máximo de um dia.
- `VALORICAÇÃO`:  Funcionalidade dependente da implementação da cotação em tempo real.

##
### Instalação e Configuração: 

- Clone o repositório: - `git clone https://github.com/LucaSilvalsm/Projeto-Carteira-Invest.git` 
- Instale as dependências - `pip install -r requirements.txt` 
- Configure o banco de dados - Inicialize seu banco de dados PostgreSQL utilizando as configurações fornecidas.
- Execute a aplicação - `python app.py`


### Pagina Inicial: 
![127 0 0 1_5000_painel](https://github.com/user-attachments/assets/774373d6-2eac-45c6-bb57-a5e1e3edeb92)

### Pagina do Dividendos
![127 0 0 1_5000_painel_dividendos](https://github.com/user-attachments/assets/dbf29025-dbec-4571-8971-ec0e51f7cb47)

### Preço Teto da Carteira
![127 0 0 1_5000_painel_calcular_preco](https://github.com/user-attachments/assets/720485fa-a594-4239-a0ec-6ecce54129d7)




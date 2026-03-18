## 📊 Projeto Carteira Invest


Aplicação desenvolvida em Python para simulação e gestão de uma carteira de investimentos, permitindo o acompanhamento de ativos e suas cotações atualizadas.

## Ideia do Projeto

O objetivo do projeto é simular uma carteira de investimentos, oferecendo funcionalidades para monitorar e gerenciar diversos ativos financeiros, incluindo ações, FIIs, ETFs, renda fixa e criptomoedas.

### ⚙️ Funcionalidades Concluídas: 
  
- 📈 Acompanhamento de dividendos: Monitoramento e gestão dos pagamentos de dividendos dos ativos
- 📊 Gráficos interativos: Visualização de dados da carteira com gráficos dinâmicos
- 🗂️ Organização por ativos: Categorização por tipo (FIIs, Ações, ETFs, Renda Fixa e Criptomoedas)
- 📌 Dashboard: Painel centralizado com métricas-chave da carteira
- 💰 Status dos ativos: Indicação de lucro ou prejuízo com base na cotação atual
- 📉 Comparativos: Comparação entre preço médio e valor de mercado atualizado
- 📈 Valorização: Acompanhamento do valor total da carteira em tempo real (ou próximo disso)
- 📊 Rentabilidade: Cálculo automático da rentabilidade dos ativos
- 🧾 Histórico de dividendos: Registro e consulta de pagamentos recebidos
- 🎯 Preço teto pessoal: Definição de preços-alvo personalizados
- 📌 Preço teto de mercado: Monitoramento com base em parâmetros definidos
- 📄 Páginas dedicadas: Visualização detalhada por tipo de ativo
- 📤 Relatórios: Geração de relatórios da carteira
- 📡 Cotação em tempo real: Acompanhamento das cotações dos ativos em tempo real
  
### 🚧 Em Desenvolvimento Futuro

- Otimização da coleta de dados via APIs (melhor performance)
- Integração com novas plataformas e serviços (B3, Google, etc.)
  
##
### 🧠 Stack de Tecnologia usada

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
### 🔧 Considerações Futuras

- `MATPLOTLIB` & `SEABORN` - Bibliotecas potenciais para visualizações adicionais de dados.
- `COTAÇÃO EM TEMPO REAL` -  Implementar a funcionalidade de cotações em tempo real ou com atraso máximo de um dia.
- `VALORICAÇÃO`:  Funcionalidade dependente da implementação da cotação em tempo real.

##
### Instalação e Configuração: 

- Clone o repositório: - `git clone https://github.com/LucaSilvalsm/Projeto-Carteira-Invest.git` 
- Instale as dependências - `pip install -r requirements.txt` 
- Configure o banco de dados - Inicialize seu banco de dados PostgreSQL utilizando as configurações fornecidas.
- Execute a aplicação - `python app.py`



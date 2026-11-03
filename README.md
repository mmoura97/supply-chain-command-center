# Supply Chain Command Center

Uma aplicação gerencial e analítica desenvolvida em Python para apoiar gestores de logística e supply chain na tomada de decisões rápidas, monitorando estoques, status de produção, necessidades de remessa, alocação de *lanes* (rotas) e risco de ruptura.

O sistema simula a integração de relatórios extraídos de sistemas ERP (como SAP) para um banco de dados local estruturado, alimentando um painel interativo em tempo real.

## 🚀 Principais Funcionalidades

- **Simulação de Extração SAP:** Geração de relatórios de estoque, produção e logística parametrizados.
- **Banco de Dados Relacional:** Persistência e estruturação dos dados utilizando SQLite.
- **Painel Executivo (Dashboard):** Interface web interativa construída com Streamlit para consulta rápida de KPIs e filtros gerenciais.
- **Alertas de Ruptura e Gargalos:** Identificação automática de itens críticos, falta de rotas (*lanes*) e pendências de remessa.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Pandas** (Manipulação e estruturação de dados)
- **SQLite** (Armazenamento e consultas estruturadas)
- **Streamlit** (Desenvolvimento do dashboard interativo)
- **OpenPyXL** (Leitura e exportação de planilhas Excel)

## 📁 Arquitetura do Projeto

```text
supply-chain-command-center/
│
├── data/
│   ├── input/       # Relatórios brutos simulados do SAP
│   └── output/      # Relatórios consolidados e exportados
│
├── database/
│   └── supply_chain.db  # Banco de dados SQLite integrado
│
├── src/
│   └── ui/
│       └── app.py       # Painel interativo Streamlit
│
├── logs/            # Arquivos de auditoria e logs
├── setup_and_mock.py # Script de inicialização e carga de dados
├── requirements.txt  # Dependências do projeto
└── README.md# Supply Chain Command Center

Uma aplicação gerencial e analítica desenvolvida em Python para apoiar gestores de logística e supply chain na tomada de decisões rápidas, monitorando estoques, status de produção, necessidades de remessa, alocação de *lanes* (rotas) e risco de ruptura.

O sistema simula a integração de relatórios extraídos de sistemas ERP (como SAP) para um banco de dados local estruturado, alimentando um painel interativo em tempo real.

## 🚀 Principais Funcionalidades

- **Simulação de Extração SAP:** Geração de relatórios de estoque, produção e logística parametrizados.
- **Banco de Dados Relacional:** Persistência e estruturação dos dados utilizando SQLite.
- **Painel Executivo (Dashboard):** Interface web interativa construída com Streamlit para consulta rápida de KPIs e filtros gerenciais.
- **Alertas de Ruptura e Gargalos:** Identificação automática de itens críticos, falta de rotas (*lanes*) e pendências de remessa.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Pandas** (Manipulação e estruturação de dados)
- **SQLite** (Armazenamento e consultas estruturadas)
- **Streamlit** (Desenvolvimento do dashboard interativo)
- **OpenPyXL** (Leitura e exportação de planilhas Excel)

## 📁 Arquitetura do Projeto

```text
supply-chain-command-center/
│
├── data/
│   ├── input/       # Relatórios brutos simulados do SAP
│   └── output/      # Relatórios consolidados e exportados
│
├── database/
│   └── supply_chain.db  # Banco de dados SQLite integrado
│
├── src/
│   └── ui/
│       └── app.py       # Painel interativo Streamlit
│
├── logs/            # Arquivos de auditoria e logs
├── setup_and_mock.py # Script de inicialização e carga de dados
├── requirements.txt  # Dependências do projeto
└── README.md

Como Executar o Projeto
Clone o repositório e aceda à pasta:

Bash
git clone [https://github.com/seu-usuario/supply-chain-command-center.git](https://github.com/seu-usuario/supply-chain-command-center.git)
cd supply-chain-command-center
Crie e ative o ambiente virtual:

Bash
python -m venv venv
# No Windows: venv\Scripts\activate
# No Linux/Mac: source venv/bin/activate
Instale as dependências:

Bash
pip install -r requirements.txt
Gere os dados simulados e inicialize o banco SQLite:

Bash
python setup_and_mock.py
Execute o painel gerencial:

Bash
streamlit run src/ui/app.py
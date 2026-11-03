import os
import sqlite3
import pandas as pd
import numpy as np


def create_project_structure():
    folders = ["data/input", "data/output", "database", "src/core", "src/ui", "logs"]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    with open("requirements.txt", "w") as f:
        f.write("pandas\nopenpyxl\ncustomtkinter\nstreamlit\nsqlite3\n")

    print("✅ Estrutura de pastas e requirements.txt criados com sucesso.")


def generate_sap_mock_data():
    """Gera dados genéricos simulando relatórios extraídos do SAP (Produção, Estoque e Logística)."""
    np.random.seed(42)

    skus = [f"SKU-{i:03d}" for i in range(1, 16)]
    descricoes = [
        "Barra de Aço Special",
        "Perfil Galvanizado",
        "Bobina a Frio",
        "Tubo Industrial",
        "Cantoneira Estrutural",
        "Placa de Aço Carbono",
        "Arame Mig",
        "Chapa Grossa",
        "Perfil U Simples",
        "Tubo Schedule",
        "Viga I",
        "Vergalhão CA-50",
        "Conexão de Aço",
        "Flange Soldável",
        "Eletrodo Revestido",
    ]

    data = {
        "SKU": skus,
        "Descricao_Produto": descricoes,
        "Estoque_Atual": np.random.randint(10, 500, size=15),
        "Estoque_Minimo": 50,
        "Em_Producao": np.random.choice([0, 150, 300, 500], size=15),
        "Status_Producao": np.random.choice(
            ["Em Linha", "Concluído", "Aguardando Insumo", "Parado"], size=15
        ),
        "Necessidade_Remessa": np.random.choice(["Sim", "Não"], size=15),
        "Lane_Definida": np.random.choice(
            ["Definida", "Pendente", "Sem Rota"], size=15
        ),
        "Risco_Ruptura": np.random.choice(["Baixo", "Médio", "Alto Crítico"], size=15),
    }

    df = pd.DataFrame(data)

    # Salva como um relatório simulado do SAP em Excel
    output_path = "data/input/Relatorio_SAP_Estoque_Producao.xlsx"
    df.to_excel(output_path, index=False)
    print("✅ Relatório simulado do SAP gerado em 'data/input/'.")

    return df


def init_sqlite_database(df):
    """Carrega os dados simulados do SAP para um banco de dados SQLite local."""
    db_path = "database/supply_chain.db"
    conn = sqlite3.connect(db_path)

    # Salva o DataFrame como uma tabela no SQLite
    df.to_sql("tb_producao_estoque", conn, if_exists="replace", index=False)
    conn.close()
    print(
        "✅ Banco de dados SQLite inicializado com sucesso em 'database/supply_chain.db'."
    )


if __name__ == "__main__":
    create_project_structure()
    df_mock = generate_sap_mock_data()
    init_sqlite_database(df_mock)

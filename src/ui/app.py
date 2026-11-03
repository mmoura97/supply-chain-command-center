import streamlit as st
import sqlite3
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="Supply Chain Command Center", page_icon="📦", layout="wide"
)


# Função para carregar os dados do SQLite
@st.cache_data
def load_data():
    conn = sqlite3.connect("database/supply_chain.db")
    query = "SELECT * FROM tb_producao_estoque"
    df = pd.read_sql(query, conn)
    conn.close()
    return df


df = load_data()

# Título do Painel
st.title("📦 Supply Chain Command Center - Painel Gerencial SAP")
st.markdown(
    "Painel de apoio à decisão rápida: monitoramento de produção, remessas, rotas (*lanes*) e risco de ruptura."
)

# Métricas principais (KPIs no topo)
col1, col2, col3, col4 = st.columns(4)

total_skus = len(df)
ruptura_critica = len(df[df["Risco_Ruptura"] == "Alto Crítico"])
necessitam_remessa = len(df[df["Necessidade_Remessa"] == "Sim"])
lanes_pendentes = len(df[df["Lane_Definida"].isin(["Pendente", "Sem Rota"])])

col1.metric("Total de SKUs Monitorados", total_skus)
col2.metric("Risco de Ruptura (Crítico)", ruptura_critica, delta_color="inverse")
col3.metric("Necessitam Remessa", necessitam_remessa)
col4.metric("Lanes Pendentes/Sem Rota", lanes_pendentes, delta_color="inverse")

st.markdown("---")

# Filtros Laterais para os Gerentes
st.sidebar.header("Filtros de Gestão")
filtro_ruptura = st.sidebar.multiselect(
    "Filtrar por Risco de Ruptura:",
    options=df["Risco_Ruptura"].unique(),
    default=df["Risco_Ruptura"].unique(),
)

filtro_status = st.sidebar.multiselect(
    "Filtrar por Status de Produção:",
    options=df["Status_Producao"].unique(),
    default=df["Status_Producao"].unique(),
)

# Aplicando filtros
df_filtrado = df[
    (df["Risco_Ruptura"].isin(filtro_ruptura))
    & (df["Status_Producao"].isin(filtro_status))
]

# Tabela Interativa de Acompanhamento
st.subheader("📋 Visão Detalhada de Estoque e Produção")
st.dataframe(df_filtrado, use_container_width=True)

# Seção de Alertas Rápidos para os Gerentes
st.markdown("---")
st.subheader("🚨 Ações Recomendadas Imediatas")

col_a, col_b = st.columns(2)

with col_a:
    st.markdown("#### Itens com Ruptura Crítica ou Baixo Estoque")
    criticos = df[df["Risco_Ruptura"] == "Alto Crítico"][
        ["SKU", "Descricao_Produto", "Estoque_Atual", "Estoque_Minimo"]
    ]
    if not criticos.empty:
        st.dataframe(criticos, use_container_width=True)
    else:
        st.success("Nenhum item em ruptura crítica no momento!")

with col_b:
    st.markdown("#### Itens com Pendência de Lane (Rota)")
    sem_lane = df[df["Lane_Definida"].isin(["Pendente", "Sem Rota"])][
        ["SKU", "Descricao_Produto", "Lane_Definida"]
    ]
    if not sem_lane.empty:
        st.dataframe(sem_lane, use_container_width=True)
    else:
        st.success("Todas as lanes estão devidamente definidas!")

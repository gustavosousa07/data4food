import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import geopandas as gpd

st.set_page_config(layout="wide", page_title="data4Food Dashboard")


@st.cache_data
def load_data():

    date_rng = pd.to_datetime(pd.date_range(start='2016-01-01', end='2028-12-31', freq='M'))
    risk_data = pd.DataFrame(date_rng, columns=['date'])

    base_risk = np.linspace(30, 85, num=len(risk_data))
    noise = np.random.normal(0, 5, len(risk_data))
    risk_data['Índice de Risco'] = base_risk + noise
    risk_data['Índice de Risco'] = risk_data['Índice de Risco'].clip(lower=0)
    local_geojson_path = "brazil_states.json"
    gdf = gpd.read_file(local_geojson_path)

    risco_niveis = ['Baixo', 'Médio', 'Alto', 'Muito Alto']
    gdf['risco'] = np.random.choice(risco_niveis, size=len(gdf))
    gdf['cod_risco'] = gdf['risco'].map({'Baixo': 1, 'Médio': 2, 'Alto': 3, 'Muito Alto': 4})

    production_data = pd.DataFrame({
        'Região': ['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul'],
        'Milho': [120, 250, 800, 450, 600],
        'Soja': [150, 180, 950, 500, 750],
        'Feijão': [80, 300, 150, 250, 200]
    })
    
    return risk_data, gdf, production_data

risk_df, brazil_gdf, prod_df = load_data()


col1, col2 = st.columns([3, 1])
with col1:
    
    st.image('data4food (1).png', width=200) 
with col2:
    st.text_input("Pesquise aqui...", key="search")
    
st.markdown("---")

left_column, right_column = st.columns(2)


with left_column:
    st.subheader("Índice Preditivo de Risco de Fome")
    
    fig_risk = px.line(risk_df, x='date', y='Índice de Risco', template='plotly_white')
    fig_risk.update_traces(fill='tozeroy', line_color='#d32f2f')

    fig_risk.add_hline(y=75, line_dash="dot", line_color="black", annotation_text="Limite de Alerta")
    
    fig_risk.add_annotation(x=pd.to_datetime('2024-06-01'), y=80, text="Alerta", showarrow=True, arrowhead=1)
    
    fig_risk.add_vline(x=pd.to_datetime('2025-06-01'), line_dash="dash", line_color="gray")

    
    fig_risk.add_annotation(
        x=pd.to_datetime('2025-06-01'),
        y=risk_df['Índice de Risco'].max(),
        text="Previsão",
        showarrow=False,
        xshift=40,
        yanchor="top"
    )
    
    st.plotly_chart(fig_risk, use_container_width=True)

    st.subheader("Mercado")
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric(label="Preço do Milho (Saca)", value="R$ 62,68", delta="-1.5%")
    kpi2.metric(label="Preço da Soja (Saca)", value="R$ 135,20", delta="+0.8%")
    kpi3.metric(label="Variação Cesta Básica", value="2.1%", delta="0.5%", delta_color="inverse")

with right_column:
    st.subheader("Mapa de Calor: Risco Alimentar")
    
    fig_map = px.choropleth_mapbox(
        brazil_gdf,
        geojson=brazil_gdf.geometry,
        locations=brazil_gdf.index,
        color='cod_risco',
        color_continuous_scale='YlOrRd', 
        mapbox_style="carto-positron",
        zoom=3,
        center={"lat": -14.2350, "lon": -51.9253},
        opacity=0.6,
        labels={'cod_risco': 'Nível de Risco'}
    )
    fig_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig_map, use_container_width=True)

    st.subheader("Produção por Cultura Agrícola (mil toneladas)")
    
    fig_bar = px.bar(
        prod_df, 
        x='Região', 
        y=['Milho', 'Soja', 'Feijão'], 
        template='plotly_white',
        color_discrete_map={
            'Milho': '#f57c00', 
            'Soja': '#4caf50',  
            'Feijão': '#d32f2f' 
        }
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with st.sidebar:
    st.header("Navegação")
    st.button("Painel de Controle", use_container_width=True, type="primary")
    st.button("Análise Preditiva", use_container_width=True)
    st.button("Relatórios", use_container_width=True)
    st.button("Configurações", use_container_width=True)
    st.markdown("---")
    with st.expander("Filtro Geográfico"):
        st.write("América do Sul")
        st.write("África")
        st.write("Ásia")
import streamlit as st
import pandas as pd
import plotly.express as px

# --- CONFIGURACIÓN Y CARGA ---
# Usamos todo el ancho de la pantalla para que los gráficos luzcan mejor
st.set_page_config(page_title="Análisis de Vehículos US", layout="wide")

# Leemos el archivo (debe estar en la raíz junto a este app.py)
df = pd.read_csv('vehicles_us.csv')

# --- ENCABEZADO ---
st.title('🚗 Dashboard de Análisis de Vehículos Usados')
st.markdown("""
En este proyecto, exploramos un conjunto de datos de anuncios de venta de coches. 
A continuación, puedes generar visualizaciones interactivas para entender mejor el mercado.
""")
st.markdown("---")

# --- SECCIÓN 1: DISTRIBUCIÓN DEL INVENTARIO (BOTONES) ---
st.subheader('Exploración de Distribuciones')
st.write('Haz clic en los botones para generar gráficos basados en los hallazgos del EDA.')

col1, col2 = st.columns(2)

with col1:
    # Requisito: Uso de botones
    if st.button('Construir Histograma de Odómetro'):
        st.write('### Distribución del Millaje')
        fig_hist = px.histogram(df, x="odometer", title="Frecuencia de Vehículos por Kilometraje")
        st.plotly_chart(fig_hist, use_container_width=True)

with col2:
    # Segundo botón para otro hallazgo importante
    if st.button('Ver Tipos de Vehículos'):
        st.write('### Anuncios por Categoría')
        fig_type = px.histogram(df, x="type", color="type", title="Tipos de Vehículos en Venta")
        st.plotly_chart(fig_type, use_container_width=True)

st.markdown("---")

# --- SECCIÓN 2: RELACIONES Y PRECIOS (CHECKBOXES) ---
st.subheader('Análisis de Precios y Tendencias')

# Requisito: Uso de casillas de verificación (checkboxes)
build_scatter = st.checkbox('Construir Gráfico de Dispersión: Precio vs Odómetro')

if build_scatter:
    st.write('### Relación entre Precio y Desgaste')
    st.write('En este gráfico analizamos cómo el kilometraje influye directamente en el precio de los vehículos.')
    # Hallazgo clave: La depreciación visualizada
    fig_scatter = px.scatter(df, x="odometer", y="price", 
                             title="Precio vs Millaje",
                             opacity=0.4,
                             color_discrete_sequence=['indianred'])
    st.plotly_chart(fig_scatter, use_container_width=True)

# Checkbox adicional para transparencia de datos
if st.checkbox('Mostrar Tabla de Datos'):
    st.write('### Vista previa del Dataset')
    st.dataframe(df.head(100))

# --- PIE DE PÁGINA ---
st.markdown("---")
st.caption("Proyecto realizado como parte del Sprint 7 - Análisis de Datos con Python.")
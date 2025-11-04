import streamlit as st
import pandas as pd
import plotly.express as px

# Configurar la página
st.title('🚗 Análisis de Vehículos Usados')
st.write('Esta aplicación analiza un conjunto de datos de vehículos usados')

# Cargar los datos
@st.cache_data
def load_data():
    return pd.read_csv('vehicles_us.csv')

df = load_data()

# Mostrar información básica
st.subheader('📊 Información del dataset')
st.write(f'Total de vehículos: {len(df)}')
st.write(f'Columnas disponibles: {len(df.columns)}')

# Mostrar las primeras filas
if st.checkbox('Mostrar datos de muestra'):
    st.write(df.head())

# Histograma de precios
st.subheader('📈 Distribución de Precios')
fig_hist = px.histogram(df, x='price', nbins=50, 
                       title='Distribución de Precios de Vehículos')
fig_hist.update_layout(xaxis_title='Precio ($)', yaxis_title='Frecuencia')
st.plotly_chart(fig_hist)

# Gráfico de dispersión
st.subheader('🔍 Relación Precio vs Año del Modelo')
if st.button('Crear gráfico de dispersión'):
    fig_scatter = px.scatter(df, x='model_year', y='price',
                            title='Precio vs Año del Modelo')
    fig_scatter.update_layout(xaxis_title='Año del Modelo', 
                             yaxis_title='Precio ($)')
    st.plotly_chart(fig_scatter)
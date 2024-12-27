import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# lectura de datos
car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

# encabezado principal
st.header('Análisis de plan publicitario para venta de vehiculos')

# primeras filas de los datos
st.write("### Primeras filas de datos")
st.write(car_data.head())

st.write("### Relación entre odómetro y precio")
# grafico de dispersion
scatter_button = st.button('Construir gráfico de dispersión')  # crear botón
if scatter_button:
    # mensaje
    st.write(
        'Creación de un gráfico de líneas de dispersión para el conjunto de datos de anuncios de venta de coches')
    # grafico de dispersión
    fig = px.scatter(
        car_data,
        x='odometer',
        y='price',
        title="Relación entre odómetro y precio",
        color='price',  # Colorear según el precio
        color_continuous_scale='Viridis',  # Cambiar la paleta de colores
        size='odometer',  # Tamaño según el odómetro
        opacity=0.7,  # Opacidad ajustada
        template='plotly_dark',  # Tema oscuro para el gráfico
        # Mostrar datos adicionales al pasar el ratón
        hover_data=['model', 'year']
    )
    st.plotly_chart(fig)
# histograma
hist_button = st.button('Construir histograma')  # crear un botón
if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # crear un histograma
    fig = px.histogram(
        car_data,
        x="odometer",
        nbins=30,  # Ajustar el número de bins
        title="Distribución de Odómetro de los Vehículos",
        color='condition',  # Colorear según la condición del vehículo
        color_discrete_map={'excellent': 'green', 'good': 'orange',
                            'fair': 'red', 'like new': 'blue'},  # Colores personalizados
        template='plotly_dark'  # Tema oscuro
    )
    st.plotly_chart(fig, use_container_width=True)

# Filtro de vehículos
st.write("## Filtrar vehículos con menos de 100,000 millas y en excelente estado")
filtered_button = st.button(
    'Construir lista de vehículos filtrados')  # crear botón
if filtered_button:
    filtered_data = car_data[(car_data['odometer'] < 100000) & (
        car_data['condition'] == 'excellent')]
    st.write(filtered_data)

# Barra lateral para filtrar datos
st.sidebar.title("Filtros")
min_price = st.sidebar.slider("Precio mínimo", 0, 50000, 0)
max_price = st.sidebar.slider("Precio máximo", 0, 50000, 50000)
selected_type = st.sidebar.selectbox(
    "Tipo de vehículo", car_data['type'].unique())

filtered_data = car_data[(car_data['price'] >= min_price) & (
    car_data['price'] <= max_price) & (car_data['type'] == selected_type)]
st.write(filtered_data)

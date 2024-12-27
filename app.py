import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# lectura de datos
car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

# encabezado principal
st.header('Data and Vehicles')

# primeras filas de los datos
st.write("### Datos cargados")
st.write(car_data.head())

st.write("### Relación entre odómetro y precio")
# grafico de dispersion
scatter_button = st.button('Construir gráfico de dispersión')  # crear botón
if scatter_button:
    # mensaje
    st.write(
        'Creación de un gráfico de líneas de dispersión para el conjunto de datos de anuncios de venta de coches')
    # grafico de dispersión
    fig = px.scatter(car_data, x='odometer', y='price',
                     title="Relación entre odómetro y precio",
                     color='purple',
                     grid=True,
                     alpha=0.5)
    st.plotly_chart(fig)
# histograma
hist_button = st.button('Construir histograma')  # crear un botón
if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Filtro de vehículos
st.write("## Filtrar vehículos con menos de 100,000 millas y en excelente estado")
filtered_data = car_data[(car_data['odometer'] < 100000) & (
    car_data['condition'] == 'excellent')]
filtered_button = st.button('Contruir lista')  # crear boton
if filtered_button:
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

import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# lectura de datos
car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

st.header('Data and Vehicles')
car_data['type'].value_counts()  # Contar la cantidad de vehículos por marca
bar_button = st.button('Construir un gráficon de barras')  # crear botón
if bar_button:
    # mensaje
    st.write(
        'Creación de un gráfico de barras para el conteo de los tipos de automóviles')
    # grafico de barras
    fig = px.bar(car_data, x='type')
    st.plotly_chart(fig, use_container_width=True)

hist_button = st.button('Construir histograma')  # crear un botón
if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# lectura de datos
car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

st.header('Data and Vehicles')

fig = px.box(car_data, x='model', y='price',
             title="Distribución de precios por modelo")
fig.show()

hist_button = st.button('Construir histograma')  # crear un botón
if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

st.header("Explorador de anuncios de vehículos usados")

st.write("Bienvenido. Esta aplicación te permite visualizar información del conjuto de datos de vehículos usados")

if st.button("Mostrar histograma de precios"):
    st.write("Distribución de precios:")
    fig_hist = px.histogram(df, x='price', nbins=50, title='Precios de vehículos')
    st.plotly_chart(fig_hist)
    
if st.button("Mostrar grafico de disperción de precios contra kilometraje"):
    st.write("Relación entre el precio y el kilometraje")
    fig_scatter = px.scatter(df, x='odometer', y='price', title="Precio vs Kilometraje", trendline='ols')
    st.plotly_chart(fig_scatter)
import streamlit as st
import pandas as pd



header = st.container()
registro = st.container()



with header:
    st.title('Pagina numero 3')
    st.text('En este proyecto realizamos una extraccion de datos para entrenar un modelo de prediccion...')

with registro:
    st.header('Si quieres recibir las notificaciones, ingresa tus datos aqui')
    st.text('Al ingresar tus datos podremos enviarte las alertas de los sismos en tu localidad')

    reg_col, reg_disp_col = st.columns(2)


    input_nombre = reg_col.text_input('Ingrese su nombre y apellido', 'Nombre y Apellido')
    input_numero = reg_col.text_input('Ingrese su numero de celular', 'EJ: +57123456789')
    input_correo = reg_col.text_input('Ingrese su correo electronico', 'correo@dominio.com')
    input_ubicacion = reg_col.selectbox('Ingrese su pais', options=['Argentina', 'Colombia', 'Peru', 'Venezuela'])
import streamlit as st
from pandas import DataFrame

st.set_page_config(page_title="Alertas Sismicas",
                   page_icon="bar_chart:",
                   layout="wide")


st.title("Formulario de Registro")
menu = ['Home', 'About']
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.subheader("Formulario")

    with st.form(key='formulario'):
        nombre = st.text_input("Nombre y Apellido")
        correo = st.text_input("Correo Electronico")
        celular = st.text_input("Numero de Telefono Celular")
        pais = st.selectbox('Ingrese su pais', options=['Argentina', 'Colombia', 'Peru', 'Venezuela'])

        boton = st.form_submit_button(label='Subir')


    if boton:
        st.success(f"Hola {nombre}, has subido tu informacion con exito")


























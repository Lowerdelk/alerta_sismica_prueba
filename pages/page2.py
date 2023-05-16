import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

st.set_page_config(page_title="Alertas Sismicas",
                   page_icon="bar_chart:",
                   layout="wide")



header = st.container()
dataset = st.container()
achievement = st.container()
features = st.container()
model_training = st.container()
registro = st.container()

df = pd.read_csv('df_final.csv', index_col=False)

# --- SIDEBAR ---
st.sidebar.header("Filtrar por parametros:")
pais = st.sidebar.multiselect(
    "Escoge el pais:",
    options=df['country'].unique(),
    default=df['country'].unique())


df_selection = df.query("country == @pais")

with header:
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.header("A cat")
    with col2:
        st.header("A dog")
    with col3:
        st.header("A bunny")
    st.title('Bienvenidos a nuestro proyecto grupal de Data Science!')
    st.text('En este proyecto realizamos una extraccion de datos para entrenar un modelo de prediccion...')




with dataset:
    st.header('Datos recolectados')
    st.text('Los datos los hemos conseguido de las paginas sismologicas de USA, Japon y Chile')

    
    st.write(df.head())

    st.subheader('Distribucion de magnitud de los sismos')
    st.bar_chart(df_selection['mag'])


     

with achievement:
    st.header('Header de Prueba')

    st.markdown('* **Probando Markdown:** Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras in diam a sapien varius commodo id id tellus. Praesent nec mi laoreet, efficitur purus et, dapibus turpis. Phasellus ac dapibus orci, et bibendum diam. Nulla fringilla, erat ut tincidunt maximus, sem urna ultricies eros, at tempor mi lorem at mi. Pellentesque sit amet nibh at leo ultricies egestas. Donec suscipit odio nec leo molestie, eget molestie dolor pulvinar')
    st.markdown('* **Tambien probando:** Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras in diam a sapien varius commodo id id tellus. Praesent nec mi laoreet, efficitur purus et, dapibus turpis. Phasellus ac dapibus orci, et bibendum diam. Nulla fringilla, erat ut tincidunt maximus, sem urna ultricies eros, at tempor mi lorem at mi. Pellentesque sit amet nibh at leo ultricies egestas. Donec suscipit odio nec leo molestie, eget molestie dolor pulvinar')
    st.markdown('* **Estamos Mejorando:** Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras in diam a sapien varius commodo id id tellus. Praesent nec mi laoreet, efficitur purus et, dapibus turpis. Phasellus ac dapibus orci, et bibendum diam. Nulla fringilla, erat ut tincidunt maximus, sem urna ultricies eros, at tempor mi lorem at mi. Pellentesque sit amet nibh at leo ultricies egestas. Donec suscipit odio nec leo molestie, eget molestie dolor pulvinar')


with features:
    st.header('Las cosas que hemos hecho!')
    st.markdown('* **Extraccion de datos:** Esto es un texto de prueba')

    '''columnas = ['latitude', 'longitude']
    df = df[columnas]

    df = df.drop(df.loc[df['longitude']=='00.8098.5'].index)
    df = df.drop(df.loc[df['longitude']=='06.0112.0'].index)
    df = df.dropna()


    df['latitude'] = df['latitude'].astype('float')
    df['longitude'] = df['longitude'].astype('float')'''

    st.map(df)




with model_training:
    st.header('Nuestro modelo entrenado!')
    st.text('Aqui escoges los parametros para ver su desempeño')

    sel_col, disp_col = st.columns(2)

    max_mag = sel_col.slider('Cual debe ser la magnitud maxima?',
                             min_value=1,
                             max_value=8,
                             step=1)

    n_estimators = sel_col.selectbox('Cuantos sismos quieres ver?',
                                     options=[10, 20, 30 , 40, 50, 'Sin limite'],
                                     index = 0)

    sel_col.text('Aqui hay una lista de las columnas en la data:')
    sel_col.write(df.columns)
  
    input_feature = sel_col.text_input('Escriba una columna', 'mag')



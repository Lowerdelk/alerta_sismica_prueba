import streamlit as st
from PIL import Image

st.set_page_config(page_title="Alertas Sismicas",
                   page_icon="bar_chart:",
                   layout="wide")




# CSS style for the header
header_style = """
    <style>
        .header {
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: red;
            color: white;
            padding: 20px;
            font-size: 24px;
            font-weight: bold;
            border-radius: 15px;
        }

        .header .image {
            width: 40px;
            height: 40px;
        }

        .header span {
            font-size: 48px;
        }
        
        @media (max-width: 728px) {
            .header {
                flex-wrap: wrap;
                padding: 5px;
            }

            .header span {
                font-size: 20px
            }

            .header .image {
                margin-bottom: 5px;
            }
        }
    </style>
"""

# Picture paths
icono1 = Image.open('src/alert_icon.png')

# Display the header
st.markdown(header_style, unsafe_allow_html=True)
st.markdown(
    f'''
    <div class="header">
        <div class="image">
            <img src="{icono1}" alt="Alert Icon">
        </div>
        <span>ALERTA DE SISMO FUERTE</span>
        <div class="image">
            <img src="{icono1}" alt="Alert Icon">
        </div>
    </div>
    ''',
    unsafe_allow_html=True
)

# CSS style for the split Markdown sections
split_markdown_style = """
    <style>
        .split-markdown {
            display: flex;
            justify-content: center;
        }
        .left-section {
            flex: 1 1 50%;
            max-width: 400px;
            background-color: teal;
            padding: 20px;
            text-align: center;
            border-radius: 15px;
            margin-right: 20px;
            margin-bottom: 20px;
        }
        .right-section {
            flex: 1 1 50%;
            max-width: 400px;
            background-color: orange;
            padding: 20px;
            text-align: center;
            border-radius: 15px;
            margin-left: 20px;
            margin-bottom: 20px;
        }
        .split-markdown h2 {
            font-size: 80px;
            color: black;
        }
        .split-markdown p {
            font-size: 44px;
            color: black;
        }
        @media (max-width: 728px) {
            .left-section, .right-section {
                width: 100%;
                max-width: none;
                margin-right: 0;
                margin-left: 0;
            }
            .split-markdown h2 {
                font-size: 34px;
            }
            .split-markdown p {
                font-size: 20px;
                color: black;
            }
        }
    </style>
"""

# Display the split Markdown sections
st.markdown(split_markdown_style, unsafe_allow_html=True)
st.markdown(
    '''
    <div class="split-markdown">
        <div class="left-section">
            <h2>3.5</h2>
            <p>MAGNITUD</p>
        </div>
        <div class="right-section">
            <h2>12KM</h2>
            <p>PROFUNDIDAD</p>
        </div>
    </div>
    ''',
    unsafe_allow_html=True
)
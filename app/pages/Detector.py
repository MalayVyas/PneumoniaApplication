import streamlit as st
import numpy as np
import cv2
# from streamlit_extras.switch_page_button import switch_page
import numpy as np
import tensorflow as tf
import h5py as h5py
import plotly.graph_objects as go
import matplotlib.pyplot as plt


st.set_page_config(initial_sidebar_state="collapsed", layout="wide")

st.markdown(""" <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style> """, unsafe_allow_html=True)



@st.cache_resource
def img_to_array(image, data_format=None):
    # Convert image to array
    img_array = np.array(image)

    # Adjust data format if specified
    if data_format == 'channels_first':
        img_array = np.moveaxis(img_array, -1, 0)

    return img_array


# @st.cache_resource
def load_model(filepath, compile=True):
    model = tf.keras.models.load_model(filepath, compile=compile)
    if compile:
        model.compile()
    return model


st.markdown("""
        <style>
    body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
        display: flex;
        justify-content: flex-end;
    }
    nav {
        overflow: hidden;
        position:absolute;
        top:0px;
        right:0px;    
    }
    nav a {
        float: left;
        display: block;
        color: white;
        text-align: center;
        padding: 4px 20px;
        text-decoration: none;
    }
    nav a:hover {
        color: 00ffff;
    }
    </style>
    </head>
    <body>
    <nav>
    <a target = "_self" href="Overview">Overview</a>
    <a target = "_self" href="Login">Logout</a>
    </nav>        
    
    """, unsafe_allow_html=True)
st.markdown('# Detection page')
st.markdown(
    """
    <style>
        [data-testid="collapsedControl"] {
            display: none
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.write("### Hello world. This is an Pneumonia Detector")


file = st.file_uploader(label="Upload your Image.", type=[
                        "jpg", "png", "jpeg"], accept_multiple_files=False)
if file is not None:

    file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)
    opencv_image1 = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
    image2 = np.array(opencv_image1, dtype=np.uint8)

    c1, c2, c3 = st.columns(3)
    with c2:
        st.image(opencv_image1)

    predict_button = st.button(label="Predict")

    img = cv2.resize(image2, (256, 256))
    img_array = img_to_array(img)

    img_array = np.expand_dims(img, axis=0)
    img_array = img_array.astype(np.float32)

    img_array /= 255.0

    if predict_button:
        model = load_model(
            'D:\\Coding\\Projects\\PnuemoniaDetection\\app\\model\\cmod_with_batch64_acc98_valacc98_testacc95_25epoch.h5', compile=False)
        model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=[
                      'acc', tf.keras.metrics.Precision(name='precision'), tf.keras.metrics.Recall(name='recall')])
        result = model.predict(img_array, verbose=0)

        result = result[0][0]
        result = round(result, 3)
        fig = go.Figure(go.Bar(
            x=[1.0],
            y=['Pneumonia'],
            orientation='h',
            width=[0.5]
        ))

        fig.update_layout(
            title='Pneumonia Chance',
            xaxis=dict(title='Percentage Chance'),
            yaxis=dict(title=''),
            width=1000,
            height=210
        )

        if float(result) > 0.68:

            fig.add_trace(go.Bar(
                x=[result],
                y=['Pneumonia'],
                orientation='h',
                marker=dict(color='red'),
                width=[1.5]
            ))
            st.plotly_chart(fig, use_container_width=True)

        else:
            fig.add_trace(go.Bar(
                x=[result],
                y=['Pneumonia'],
                orientation='h',
                marker=dict(color='green'),
                width=[1.5]
            ))
            st.plotly_chart(fig, use_container_width=True)

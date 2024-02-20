import streamlit as st
from PIL import Image

st.set_page_config(initial_sidebar_state="collapsed", layout="wide")


st.markdown(""" <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style> """, unsafe_allow_html=True)


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
    <a target = "_self" href="Detector">Predictor</a>
    <a target = "_self" href="Login">Logout</a>
    </nav>        
    
    """, unsafe_allow_html=True)

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

title_alignment = """
    <style>
    #the-title {
    text-align: center
    }
    </style>
    """
st.markdown(title_alignment, unsafe_allow_html=True)


st.title("Overview")

st.write("""Pneumonia is a significant worldwide health and wellness
    concern that creates considerable health issues plus
    fatality, highlighting the importance of promptly and
    accurately detecting and treating it. Despite the
    improvements in imaging innovation, the hand-operated
    evaluation of chest radiographs by radiologists remains
    the fundamental technique for spotting pneumonia,
    bringing about hold-ups in medical diagnosis together
    with therapy. This research suggests a pneumonia
    discovery technique that utilizes deep learning strategies
    to automate the procedure.""")
st.write("\n")
st.write("""By harnessing an extensive
    data source of classified chest radiographs the
    recommended design intends to precisely determine
    locations influenced by pneumonia, making it possible for
    better and more efficient medical diagnosis and therapy.
    The design uses a custom convolutional neural network
    (CNN) that undergoes training on a wide range of
    pneumonia-positive and pneumonia-negative instances
    from various healthcare organizations. Before educating
    the design, various pre-processing actions were taken for
    the chest radiographs to boost integrity along with
    efficiency. This research study adds to the growth of an
    automated, coupled with a trusted, pneumonia discovery
    system, which has the potential to enhance individual
    results and boost healthcare effectiveness.""")

st.write("# \n\n\n")

# st.image("/app/images/normal.jpg")

c1, c2, c3, c4, c5 = st.columns([1, 5, 1, 5, 1])
with c1:
    st.write(" ")
with c2:

    st.markdown("<h4 style='text-align: center; color: Green;'>Normal</h4>",
                unsafe_allow_html=True)
    img1 = Image.open(
        r"D:\\Coding\\Projects\\PnuemoniaDetection\\app\\images\\normal.jpg")
    st.image(image=img1, use_column_width=True)
    st.write("\n \n")
    st.write("This is a normal image")

with c3:
    st.write(" ")

with c4:

    st.markdown("<h4 style='text-align: center; color: Red;'>Pneumonia</h4>",
                unsafe_allow_html=True)
    img2 = Image.open(
        "D:\\Coding\\Projects\\PnuemoniaDetection\\app\\images\\pneumonia.jpeg")
    st.image(image=img2, use_column_width=True)
    st.write("\n \n")
    st.write("This is a pneumonia image")
with c5:
    st.write(" ")

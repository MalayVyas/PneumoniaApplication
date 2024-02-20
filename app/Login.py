import streamlit as st
from db import DataBase_User
from streamlit_extras.switch_page_button import switch_page

st.set_page_config("ChexNet", initial_sidebar_state='collapsed', layout="wide")
st.session_state['loggedIn'] = False


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
  <a target = "_self" href="SignUp">Sign Up</a>
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


st.title("ChexNet")
st.write("### Login Page")
username = st.text_input(label="Username", type="default",
                         placeholder="Enter your Username")
password = st.text_input(label="Password", type="password",
                         placeholder="Enter your Password")
submit = st.button("Submit")


db = DataBase_User()
conn, cursor = db.connect()
cursor = conn.cursor()

if submit:
    st.session_state["loggedIn"] = db.search_from_table_up(username, password)
    if st.session_state["loggedIn"]:
        st.write("Correct Credentials")
    if not st.session_state["loggedIn"]:
        st.write("Please enter correct Credentials")

if st.session_state["loggedIn"] and submit:
    switch_page("Overview")

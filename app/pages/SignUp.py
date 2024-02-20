import streamlit as st
import time
from db import DataBase_User
from streamlit_extras.switch_page_button import switch_page

st.set_page_config("Hello", initial_sidebar_state='collapsed', layout="wide")
st.session_state['loggedIn'] = False

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
  <a target = "_self" href="Login">Login</a>
</nav>
""", unsafe_allow_html=True)


st.title("ChexNet")
st.write("### Sign In for the ChexNet App")
username = st.text_input(label="Username", type="default",
                         placeholder="Enter your Username")
password = st.text_input(label="Password", type="password",
                         placeholder="Enter your Password")
submit = st.button("Submit")


db = DataBase_User()
conn, cursor = db.connect()
cursor = conn.cursor()

if submit:
    if not db.search_from_table(username):
        st.session_state["loggedIn"] = db.insert_into_table(username, password)
        if not st.session_state["loggedIn"]:
            st.write("Please enter correct Credentials")
    else:
        st.write("Username already exists. Please try another name.")
if st.session_state["loggedIn"] and submit:
    st.write("SignUp Successfully. PLease Login.")
    time.sleep(1)
    switch_page("Login")

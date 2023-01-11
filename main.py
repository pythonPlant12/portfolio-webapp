import streamlit as st
st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Nikita Lutsai")
    content = """
    Hi, i am Nikita! I am a Python programmer. I graduated in Associate's Degree in Marketing and International Trade. Beside these studies I realized that my true passion is programming. I quited my regular job in order to be able to study as much as possible and get a job where I can really enjoy what I am doing. 
    """
    st.info(content)
content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.caption(content2)


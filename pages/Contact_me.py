import streamlit as st
from send_email import send_email

st.set_page_config(layout="wide")
st.header("Contact me")

with st.form(key="email_form"):
    user_email = st.text_input("Enter your email")
    row_message = st.text_area("Your message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{row_message}"""
    button = st.form_submit_button()
    if button:
        send_email(message)
        st.info("Your email was sent successfully")
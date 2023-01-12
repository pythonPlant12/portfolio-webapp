import streamlit as st
import pandas
from send_email import send_mail

topic_options = []
st.set_page_config(layout="wide")
st.header("Contact me")
df = pandas.read_csv("/Users/nikitalutsai/PycharmProjects/portfolio-app/pages/topics.csv")
for index, item in df.iterrows():
    topic_options.append(item["topic"])

with st.form(key="email_form"):
    user_email = st.text_input("Enter your email")
    topic = st.selectbox("What's your purpose of contacting me", topic_options)
    row_message = st.text_area("Your message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
Topic: {topic}
{row_message}"""
    button = st.form_submit_button()
    if button:
        send_mail(message)
        st.info("Your email was sent successfully")
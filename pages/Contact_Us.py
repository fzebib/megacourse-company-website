import streamlit as st
import pandas
from send_email import send_email

df = pandas.read_csv("topics.csv")

st.header("Contact us")

with st.form(key="email_form", clear_on_submit=True):
    user_email = st.text_input(key="email_input", label="Your Email address")
    topic = st.selectbox("What topics do you want to discuss?", df["topic"])
    raw_message = st.text_area(label="Your message")
    submitted = st.form_submit_button("Submit")
    if submitted:
        message = f"""\
Subject: {topic} from {user_email}

{raw_message}
"""
        send_email(message)

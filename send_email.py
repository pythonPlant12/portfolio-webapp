import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "tugganinternethelper@gmail.com"
password = "pbfswkewstwwtcwa"

receiver = "tugganinternethelper@gmail.com"

message = """\
Subject: Hi!
How are you?
Bye!
"""
context = ssl.create_default_context()

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, username, message)
